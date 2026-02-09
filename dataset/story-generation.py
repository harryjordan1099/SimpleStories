# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.20.0
#   kernelspec:
#     display_name: Python 3.12
#     language: python
#     name: py312
# ---

# %%
import openai
import random
import json
from typing import List, Dict, Optional
import time

import data_generation_config as config


# %%
class SimpleStoriesGenerator:
    def __init__(self, api_key: str):
        """
        Initialize the generator with OpenAI API key.
        
        Args:
            api_key: OpenAI API key for authentication
        """
        self.client = openai.OpenAI(api_key=api_key)

    def sample_letter(self) -> str:
        """
        Sample a letter based on frequency distribution from reference corpus.
        
        Returns:
            A lowercase letter sampled according to LETTER_FREQUENCIES
        """
        letters = list(config.LETTER_FREQUENCIES.keys())
        weights = list(config.LETTER_FREQUENCIES.values())
        return random.choices(letters, weights=weights, k=1)[0].lower()

    def calculate_story_count(self, paragraph_count: int) -> int:
        """
        Calculate number of stories inversely proportional to paragraph count.
        More paragraphs = fewer stories per completion to manage token usage.
        
        Args:
            paragraph_count: Number of paragraphs per story
            
        Returns:
            Number of stories to generate in this completion
        """
        return config.STORY_COUNT_MAPPING.get(paragraph_count, 5)

    def build_prompt(self) -> Dict[str, any]:
        """
        Build a story generation prompt with randomly selected parameters.
        
        Follows the SimpleStories methodology:
        - Samples theme, topic, style, and narrative feature
        - 50% chance to include grammar feature
        - 33% chance to include author persona
        - Samples starting letter from frequency distribution
        - Selects 3-5 character names from the allowed list
        
        Returns:
            Dictionary containing:
                - prompt: The complete prompt string
                - metadata: All sampled parameters for tracking
        """
        # Sample paragraph count and calculate corresponding story count
        paragraph_count = random.randint(config.MIN_PARAGRAPH_COUNT, 
                                        config.MAX_PARAGRAPH_COUNT)
        story_count = self.calculate_story_count(paragraph_count)
        
        # Sample core parameters
        theme = random.choice(config.THEMES)
        topic = random.choice(config.TOPICS)
        style = random.choice(config.STYLES)
        narrative_feature = random.choice(config.NARRATIVE_FEATURES)
        
        # Conditionally sample grammar feature (50% probability)
        grammar_feature = None
        if random.random() < config.GRAMMAR_FEATURE_PROBABILITY:
            grammar_feature = random.choice(config.GRAMMAR_FEATURES)
        
        # Conditionally sample author persona (33% probability)
        author_persona = None
        if random.random() < config.AUTHOR_PERSONA_PROBABILITY:
            author_persona = random.choice(config.AUTHOR_PERSONAS)
        
        # Sample part of speech and starting letter
        pos = random.choice(config.PARTS_OF_SPEECH)
        starting_letter = self.sample_letter()
        
        # Sample character names (3-5 names from the allowed list)
        name_count = random.randint(config.MIN_NAME_COUNT, config.MAX_NAME_COUNT)
        selected_names = random.sample(config.NAMES, name_count)
        name_list = ", ".join(selected_names)
        
        # Build the prompt following the paper's template
        prompt = f"""Write {story_count} short stories ({paragraph_count} paragraphs each) using very basic words. Do not number each story or write a headline. Make the stories diverse by fully exploring the theme, but each story should be self-contained. Separate the stories by putting "The End." in between. Make the stories as qualitatively distinct to each other as possible. In particular, never start two stories the same way! Each story should be about {theme}, include {topic}, be {style} in its writing style and ideally feature {narrative_feature}."""
        
        # Add grammar feature instruction if sampled
        if grammar_feature:
            prompt += f" The most important thing is to write an engaging easy story, but where it makes sense, demonstrate the use of {grammar_feature}."
        
        # Add author persona instruction if sampled
        if author_persona:
            prompt += f" Write from the perspective of {author_persona}."
        else:
            prompt += " Write from the perspective of a thoughtful storyteller."
        
        # Add name constraints and starting word constraint
        prompt += f""" If you need to use proper names, make them from space-separated common words. Either don't give characters a name, or select from {name_list}. Complex story structure is great, but please remember to only use very simple words! If you can, start the story with {pos} that begins with the letter {starting_letter}."""
        
        # Store all metadata for tracking
        metadata = {
            "story_count": story_count,
            "paragraph_count": paragraph_count,
            "theme": theme,
            "topic": topic,
            "style": style,
            "narrative_feature": narrative_feature,
            "grammar_feature": grammar_feature,
            "author_persona": author_persona,
            "starting_pos": pos,
            "starting_letter": starting_letter,
            "names": selected_names
        }
        
        return {"prompt": prompt, "metadata": metadata}

    def generate_stories(self, 
                        model: str = config.DEFAULT_MODEL,
                        temperature: float = config.DEFAULT_TEMPERATURE, 
                        top_p: float = config.DEFAULT_TOP_P,
                        max_tokens: int = config.DEFAULT_MAX_TOKENS,
                        max_retries: int = config.DEFAULT_RETRY_COUNT) -> Dict:
        """
        Generate stories using OpenAI API with nucleus sampling.
        
        Args:
            model: OpenAI model to use (default: gpt-4o-mini)
            temperature: Sampling temperature (default: 1.0)
            top_p: Nucleus sampling parameter (default: 0.9)
            max_tokens: Maximum tokens in completion
            max_retries: Number of retry attempts on failure
            
        Returns:
            Dictionary containing:
                - stories: List of generated stories
                - metadata: Generation parameters
                - prompt: The prompt used
                - raw_completion: Full API response
                - model: Model used
                - usage: Token usage statistics
        """
        prompt_data = self.build_prompt()
        
        # Retry logic with exponential backoff
        for attempt in range(max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "user", "content": prompt_data["prompt"]}
                    ],
                    temperature=temperature,
                    top_p=top_p,
                    max_tokens=max_tokens
                )
                
                completion = response.choices[0].message.content
                
                # Split stories by "The End." separator
                stories = [s.strip() for s in completion.split("The End.") if s.strip()]
                
                return {
                    "stories": stories,
                    "metadata": prompt_data["metadata"],
                    "prompt": prompt_data["prompt"],
                    "raw_completion": completion,
                    "model": model,
                    "usage": {
                        "prompt_tokens": response.usage.prompt_tokens,
                        "completion_tokens": response.usage.completion_tokens,
                        "total_tokens": response.usage.total_tokens
                    }
                }
            
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:
                    # Exponential backoff
                    time.sleep(2 ** attempt)
                else:
                    raise

    def generate_dataset(self, 
                        num_completions: int, 
                        output_file: str, 
                        save_interval: int = config.DEFAULT_SAVE_INTERVAL,
                        model: str = config.DEFAULT_MODEL) -> List[Dict]:
        """
        Generate a full dataset of stories with periodic saving.
        
        Args:
            num_completions: Number of API completions to generate
            output_file: Path to save the dataset JSON file
            save_interval: Save progress every N completions
            model: OpenAI model to use
            
        Returns:
            List of all generated completions with metadata
        """
        dataset = []
        
        for i in range(num_completions):
            try:
                print(f"Generating completion {i+1}/{num_completions}...")
                result = self.generate_stories(model=model)
                dataset.append(result)
                
                # Periodic saving to avoid data loss
                if (i + 1) % save_interval == 0:
                    self._save_dataset(dataset, output_file)
                    print(f"Saved {i+1} completions to {output_file}")
                
                # Rate limiting (adjust based on your API tier)
                time.sleep(config.DEFAULT_RATE_LIMIT_DELAY)
                
            except Exception as e:
                print(f"Error on completion {i+1}: {e}")
                continue
        
        # Final save
        self._save_dataset(dataset, output_file)
        print(f"Dataset generation complete! Saved to {output_file}")
        print(f"Total completions: {len(dataset)}")
        print(f"Total stories: {sum(len(c['stories']) for c in dataset)}")
        
        return dataset
    
    def _save_dataset(self, dataset: List[Dict], filename: str):
        """
        Save dataset to JSON file.
        
        Args:
            dataset: List of completion dictionaries
            filename: Output file path
        """
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(dataset, f, indent=2, ensure_ascii=False)



