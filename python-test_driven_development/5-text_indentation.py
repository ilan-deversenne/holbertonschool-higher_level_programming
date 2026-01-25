#!/usr/bin/python3

def text_indentation(text):
    """
        
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.replace(". ", ".\n\n")
    text = text.replace("? ", "?\n\n")
    text = text.replace(": ", ":\n\n")

    print(text)
