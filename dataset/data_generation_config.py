"""
Configuration file for SimpleStories dataset generation.
Contains all parameters used in the story generation process.
"""

# Theme options for stories
THEMES = [
    "Friendship", "Courage", "Contradiction", "Coming of age", "Kindness", 
    "Amnesia", "Adventure", "Imagination", "Family", "Perseverance", 
    "Curiosity", "Honesty", "Romance", "Teamwork", "Responsibility", 
    "Strategy", "Magic", "Discovery", "Betrayal", "Deception", 
    "Generosity", "Creativity", "Self-Acceptance", "Helping Others", 
    "Hardship", "Agency", "Power", "Revenge", "Independence", 
    "Problem-Solving", "Resourcefulness", "Long-Term Thinking", 
    "Optimism", "Humor", "Love", "The Five Senses", "Tradition", 
    "Innovation", "Hope", "Dreams", "Belonging", "Travel", "Overcoming", 
    "Trust", "Morality", "Happiness", "Consciousness", "Failure", 
    "Conflict", "Cooperation", "Growth", "Loss", "Celebration", 
    "Transformation", "Scheming", "Challenge", "Planning", "Wonder", 
    "Surprises", "Conscience", "Intelligence", "Logic", "Resilience"
]

# Topic options for stories
TOPICS = [
    "talking animals", "fantasy worlds", "time travel", 
    "a deadline or time limit", "space exploration", "mystical creatures", 
    "underwater adventures", "dinosaurs", "pirates", "superheroes", 
    "fairy tales", "outer space", "hidden treasures", "magical lands", 
    "enchanted forests", "secret societies", "robots and technology", 
    "sports", "school life", "holidays", "cultural traditions", 
    "magical objects", "lost civilizations", "subterranean worlds", 
    "bygone eras", "invisibility", "giant creatures", "miniature worlds", 
    "alien encounters", "haunted places", "shape-shifting", 
    "island adventures", "unusual vehicles", "undercover missions", 
    "dream worlds", "virtual worlds", "riddles", "sibling rivalry", 
    "treasure hunts", "snowy adventures", "seasonal changes", 
    "mysterious maps", "royal kingdoms", "living objects", "gardens", 
    "lost cities", "the arts", "the sky"
]

# Writing style options
STYLES = [
    "whimsical", "playful", "epic", "fairy tale-like", "modern", 
    "classic", "lyric", "mythological", "lighthearted", "adventurous", 
    "heartwarming", "humorous", "mystical", "action-packed", 
    "fable-like", "surreal", "philosophical", "melancholic", "noir", 
    "romantic", "tragic", "minimalist", "suspenseful"
]

# Narrative feature options
NARRATIVE_FEATURES = [
    "dialogue", "in medias res", "a moral lesson", 
    "absence indicating a presence", "a story told through letters", 
    "a twist ending", "an unreliable narrator", "foreshadowing", "irony", 
    "inner monologue", "symbolism", "a MacGuffin", "a non-linear timeline", 
    "a reverse timeline", "circular narrative structure", "a flashback", 
    "a nested structure", "a story within a story", "a Red Herring", 
    "multiple perspectives", "Checkhov's gun", "the fourth wall", 
    "a cliffhanger", "an anti-hero", "juxtaposition", "climactic structure"
]

# Grammar feature options (used in 50% of stories)
GRAMMAR_FEATURES = [
    "present tense", "past tense", "future tense", "progressive aspect", 
    "perfect aspect", "passive voice", "conditional mood", 
    "imperative mood", "indicative mood", "relative clauses", 
    "prepositional phrases", "indirect speech", "exclamatory sentences", 
    "comparative forms", "superlative forms", "subordinate clauses", 
    "ellipsis", "anaphora", "cataphora", "wh-questions", "yes-no questions", 
    "gerunds", "participle phrases", "inverted sentences", 
    "non-finite clauses", "determiners", "quantifiers", "adjective order", 
    "parallel structure", "discourse markers", "appositive phrases"
]

# Author persona options (used in 33% of stories)
AUTHOR_PERSONAS = [
    "an explorer archetype", "a rebellious author", "a powerful leader", 
    "a wise, old person who wants to teach the young", "an innocent author", 
    "a moralistic teacher", "a hopeless romantic", 
    "a hurt, ill-intentioned person", "an academic", "a jester archetype", 
    "a poet", "a philosopher", "a mother", "a father", "someone curious", 
    "someone evil", "someone who wants to prove a point", "a child", 
    "a pedant", "the everyman", "the oppressed", "a cruel person", 
    "someone who loves order and structure"
]

# List of allowed character names
NAMES = [
    "Harry", "George", "Giada", "Maria", "Ben", "Julia", "Matthew", 
    "Suzanne", "Callum", "Priyanka", "James", "Matt", "Marcea", 
    "Tina", "Zaen", "Joe"
]

# Letter frequency distribution from reference corpus
LETTER_FREQUENCIES = {
    'A': 11.7, 'B': 4.4, 'C': 5.2, 'D': 3.2, 'E': 2.8,
    'F': 4.0, 'G': 1.6, 'H': 4.2, 'I': 7.3, 'J': 0.51,
    'K': 0.86, 'L': 2.4, 'M': 3.8, 'N': 2.3, 'O': 7.6,
    'P': 4.3, 'Q': 0.22, 'R': 2.8, 'S': 6.7, 'T': 16.0,
    'U': 1.2, 'V': 0.82, 'W': 5.5, 'X': 0.045, 'Y': 0.76,
    'Z': 0.045
}

# Parts of speech for story starting constraints
PARTS_OF_SPEECH = ["a noun", "an adjective", "an adverb", "a preposition"]

# Generation parameters
GRAMMAR_FEATURE_PROBABILITY = 0.5  # 50% of stories include a grammar feature
AUTHOR_PERSONA_PROBABILITY = 0.33  # 33% of stories include an author persona
MIN_PARAGRAPH_COUNT = 1
MAX_PARAGRAPH_COUNT = 9

# OpenAI API parameters
DEFAULT_MODEL = "gpt-4o-mini"
DEFAULT_TEMPERATURE = 1.0
DEFAULT_TOP_P = 0.9  # Nucleus sampling parameter
DEFAULT_MAX_TOKENS = 4000

# Story count mapping (inversely proportional to paragraph count)
# More paragraphs = fewer stories per completion to manage token usage
STORY_COUNT_MAPPING = {
    1: 12, 2: 12, 3: 12,
    4: 8, 5: 8,
    6: 5, 7: 5,
    8: 3, 9: 3
}

# Name selection parameters
MIN_NAME_COUNT = 3
MAX_NAME_COUNT = 5

# Dataset generation parameters
DEFAULT_SAVE_INTERVAL = 100  # Save progress every N completions
DEFAULT_RETRY_COUNT = 3
DEFAULT_RATE_LIMIT_DELAY = 1  # Seconds between API calls