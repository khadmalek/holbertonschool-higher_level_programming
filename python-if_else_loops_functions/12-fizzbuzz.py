#!/usr/bin/python3
def fizzbuzz():
    """
    Imprime les nombres de 1 à 100 en remplaçant
    certains par Fizz, Buzz, ou FizzBuzz.
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end=" ")
        elif number % 3 == 0:
            print("Fizz", end=" ")
        elif number % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(number, end=" ")
