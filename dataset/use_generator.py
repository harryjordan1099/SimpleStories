#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
SimpleStories generator usage example.
This script loads the OpenAI API key from a configuration file.
"""

from pathlib import Path
import sys

# Import the generator
from data_generation_config import DEFAULT_MODEL
from story_generation import SimpleStoriesGenerator

# Import API key from configuration file
try:
    from api_config import OPENAI_API_KEY
except ImportError:
    print("Error: api_config.py not found or missing OPENAI_API_KEY.")
    print("Please create api_config.py with your API key.")
    sys.exit(1)

def main():
    """Main function to demonstrate the SimpleStoriesGenerator."""
    # Initialize the generator
    generator = SimpleStoriesGenerator(api_key=OPENAI_API_KEY)

    # Generate a single story completion
    print("Generating stories...")
    result = generator.generate_stories(model=DEFAULT_MODEL)

    # Print the generated stories
    print(f"\nGenerated {len(result['stories'])} stories:")
    for i, story in enumerate(result['stories']):
        print(f"\n--- Story {i+1} ---")
        print(story)
        print("The End.")

    # Print metadata
    print("\nGeneration metadata:")
    for key, value in result['metadata'].items():
        print(f"- {key}: {value}")

    # Print token usage
    print(f"\nToken usage: {result['usage']['total_tokens']} tokens")

if __name__ == "__main__":
    main()