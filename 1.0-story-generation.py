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

# %%
number_of_stories = 12
number_of_paragraphs = 2
story_ending = "The End."
theme = "Responsibility"
topic = "secret societies"
style = "lyric"
narrative_feature = "inner monologue"
grammar_feature = "progressive aspect"
author_persona = "someone curious"

list_of_names = ["Harry", 
                 "George", 
                 "Giada", 
                 "Maria", 
                 "Ben", 
                 "Julia", 
                 "Matthew", 
                 "Suzanne", 
                 "Callum", 
                 "Priyanka", 
                 "James", 
                 "Matt",
                 "Marcea",
                 "Tina",
                 "Zaen",
                 "Joe"]
list_of_names_input = ", ".join(list_of_names)

letter_frequencies = {
        'A': 11.7, 'B': 4.4, 'C': 5.2, 'D': 3.2, 'E': 2.8,
        'F': 4.0, 'G': 1.6, 'H': 4.2, 'I': 7.3, 'J': 0.51,
        'K': 0.86, 'L': 2.4, 'M': 3.8, 'N': 2.3, 'O': 7.6,
        'P': 4.3, 'Q': 0.22, 'R': 2.8, 'S': 6.7, 'T': 16.0,
        'U': 1.2, 'V': 0.82, 'W': 5.5, 'X': 0.045, 'Y': 0.76,
        'Z': 0.045
}


# %%
story_generation_prompt_template = f"""
Write {number_of_stories} short stories ({number_of_paragraphs} paragraphs each) using very basic words. Do not number each
story or write a headline. Make the stories diverse by fully exploring the theme, but each story
should be self-contained. Separate the stories by putting {story_ending} in between. Make the
stories as qualitatively distinct to each other as possible. In particular, never start two stories the
same way! Each story should be about {theme}, include {topic}, be {style} in
its writing style and ideally feature {narrative_feature}. The most important thing is to write
an engaging easy story, but where it makes sense, demonstrate the use of {grammar_feature}.
Write from the perspective of {author_persona}. If you need to use proper names, make them
from space-separated common words. Either don’t give characters a name, or select from {list_of_names_input}. 
Complex story structure is great, but please remember to only use very simple words!
If you can, start the story with {a noun} that begins with the letter {p}.
"""
