#!/usr/bin/python3

"""
This module provides functionality to serialize a Python dictionary to a JSON
file and to deserialize a JSON file to recreate a Python dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): A Python dictionary containing the data.
        filename (str): The name of the output JSON file. If the output file
                        already exists, it should be replaced.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize a JSON file to recreate a Python dictionary.

    Args:
        filename (str): The name of the input JSON file.

    Returns:
        dict: A Python dictionary with the deserialized JSON data from the
              file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
    