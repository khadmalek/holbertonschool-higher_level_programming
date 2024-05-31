#!/usr/bin/python3

"""
This module provides functionality to serialize a Python dictionary to XML
format and to deserialize XML data to recreate a Python dictionary using the
xml.etree.ElementTree module.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): A Python dictionary containing the data.
        filename (str): The name of the output XML file.
    """
    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)
    print(f"Dictionary serialized to {filename}")


def deserialize_from_xml(filename):
    """
    Load and deserialize an XML file to recreate a Python dictionary.

    Args:
        filename (str): The name of the input XML file.

    Returns:
        dict: A Python dictionary with the deserialized XML data from the file.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        data = {}
        for child in root:
            data[child.tag] = child.text

        print(f"Data deserialized from {filename}")
        return data
    except Exception as e:
        print(f"An error occurred during deserialization: {e}")
        return None
    