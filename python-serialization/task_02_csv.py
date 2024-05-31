#!/usr/bin/python3

"""
This module provides functionality to convert data from CSV format to JSON
format using serialization techniques.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to a JSON file.

    Args:
        csv_filename (str): The name of the input CSV file.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    