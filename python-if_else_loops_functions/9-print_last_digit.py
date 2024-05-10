#!/usr/bin/python3
def print_last_digit(number):
    """
    Affiche et retourne le dernier chiffre d'un nombre.
    """
    # Le dernier chiffre d'un nombre positif ou négatif
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
