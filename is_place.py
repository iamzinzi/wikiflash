#!/usr/bin/python3
"""is_place module"""
import wikipedia


def is_place(place_name):
    """is_place takes a string argument, creates a wikipedia object,
    and checks if it's a city, state, or country. Returns True if string
    argument is a city, state, or country. False otherwise.
    """
    filters = ['city', 'state', 'country']

    try:
        place = wikipedia.page(place_name)
    except wikipedia.exceptions.DisambiguationError as e:
        place = wikipedia.page(e.options[0])
    first_paragraph = place.summary.split('\n')[0]
    for f in filters:
        if f in first_paragraph:
            return True
    return False
