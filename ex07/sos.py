"""
Author: asimon (Arthur Simon)
Date: 21/10/2025 15:55:48
File: sos.py
School: 42 Paris
"""

import sys


NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
}


def convert_morse(user_input: str):
    return " ".join(NESTED_MORSE.get(char.upper()) for char in user_input)


def main():
    try:
        assert len(sys.argv) == 2, "Wrong number of arguments"
        assert sys.argv[1].isalpha(), "Programme only accept aplha char"
        result = convert_morse(sys.argv[1])
        print(f"{result}")
    except AssertionError as e:
        print(f"AssertionError: {e}")
    return 1


if __name__ == "__main__":
    main()
