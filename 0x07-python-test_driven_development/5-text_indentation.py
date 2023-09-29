#!/usr/bin/python3
"""
This is the '5-text_indentation' module.
"""


def text_indentation(text):
    """This the text_indentation function.
    Args:
        -text (str): text to be printed.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    limit = len(text)
    i = 0
    if text[len(text) - 1] == ' ':
        limit -= 1
    if text[0] == ' ':
        i += 1
    while i < limit:
        if text[i] in ['.', '?', ':']:
            print(f"{text[i]}\n")
            if i + 1 < len(text) - 1:
                if text[i + 1] == ' ':
                    i += 1
        else:
            print(text[i], end="")
        i += 1
