import sys

"""
Author: Asimon
Date: Oct 20 2025
School: 42Paris

This module provides a function to analyze a string and count
the number of uppercase letters, lowercase letters, digits,
punctuation characters, and whitespace characters.
"""


def building(user_input: str):
    """
    Input:
        - This function expect 1 argument (string)
    Behaviour:
        Take the string given as parameter and count the number of:
        - digits
        - spaces
        - punctuations
        - lower and upper case char
    """
    upper_case = 0
    lower_case = 0
    digit = 0
    space = 0
    punctuation = 0
    punctuation_chars = ".,!?;:'\"-()[]{}<>/\\@#$%^&*_+=~`"

    for c in user_input:
        if c.isupper():
            upper_case += 1
        elif c.islower():
            lower_case += 1
        elif c.isdigit():
            digit += 1
        elif c in punctuation_chars:
            punctuation += 1
        elif c.isspace():
            space += 1

    print(f"{upper_case} upper letters")
    print(f"{lower_case} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")
    return 1


def ask_argument():
    'Function to ask user to input a string'

    while True:
        user_input = sys.stdin.readline()
        if len(user_input) > 0:
            break
        else:
            print("Invalid string please try again.")
    return user_input


def main():
    """
    Main Function.

    Input:
        - Expected 1 argument: string

    Behavior:
        - If no argument is provided programme
        ask you a string until you quite (CTR + C)

        - If more than 1 argument is provided,
          an AssertionError is thrown
    """
    try:
        assert len(sys.argv) <= 2, (
            "Error, building.py await only 1 string,"
            f"given: {len(sys.argv) - 1}")
        if (len(sys.argv) < 2):
            print("What is the text to count ?")
            user_input = ask_argument()
        else:
            user_input = sys.argv[1]
        building(user_input)
    except AssertionError as e:
        print(f"Assertion error: {e}")
    return 0


if __name__ == "__main__":
    main()
