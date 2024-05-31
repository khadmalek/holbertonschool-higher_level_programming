#!/usr/bin/python3

"""
This module provides functionality to serialize and deserialize custom Python
objects using the pickle module. It defines a class `CustomObject` with methods
to display its attributes, serialize itself to a file, and deserialize an
instance from a file.
"""

import pickle


class CustomObject:
    """
    A custom Python class to demonstrate serialization and deserialization
    using the pickle module.

    Attributes:
        name (str): The name of the object.
        age (int): The age of the object.
        is_student (bool): The student status of the object.
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Print out the object's attributes in the specified format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance of the object and save it to the
        provided filename using the pickle module.

        Args:
            filename (str): The name of the file where the object should be
                            serialized.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            print(f"Object serialized to {filename}.")
        except Exception as e:
            print(f"Serialization failed: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Load and return an instance of CustomObject from the provided filename
        using the pickle module.

        Args:
            filename (str): The name of the file from which the object should
                            be deserialized.

        Returns:
            CustomObject: An instance of CustomObject if deserialization is
                          successful, None otherwise.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            print(f"Object deserialized from {filename}.")
            return obj
        except Exception as e:
            print(f"Deserialization failed: {e}")
            return None
        