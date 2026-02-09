"""
Utility functions for Jupyter notebooks.
"""

import os
import getpass
from IPython.display import clear_output

def get_api_key_safely():
    """
    Safely prompt for and get an API key in a Jupyter notebook.
    The key will not be stored in notebook history.

    Returns:
        str: The API key
    """
    # Try to get from environment first
    api_key = os.environ.get("OPENAI_API_KEY")

    # If not in environment, prompt securely
    if not api_key:
        print("API key not found in environment variables.")
        api_key = getpass.getpass("Enter your OpenAI API key: ")

    # Clear output to hide the API key input prompt
    clear_output()

    return api_key