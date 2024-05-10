#!/usr/bin/python3
def islower(c):
    """
    Vérifie si un caractère est en minuscule.
    Retourne True si c'est le cas, sinon False.
    """
    return ord('a') <= ord(c) <= ord('z')
