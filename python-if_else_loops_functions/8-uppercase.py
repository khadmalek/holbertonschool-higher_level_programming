#!/usr/bin/python3
def uppercase(str):
    """
    Convertit une chaîne de caractères en majuscules et l'affiche.
    """
    for c in str:
        if ord("a") <= ord(c) <= ord("z"):
            # Convertir le caractère minuscule en majuscule
            upper_c = chr(ord(c) - 32)
        else:
            upper_c = c
        print("{}".format(upper_c), end="")
    print()
