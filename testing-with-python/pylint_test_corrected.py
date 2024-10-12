"""
Module to encode and decode strings based on a shift cipher.
"""

import string

SHIFT = 3
CHOICE = input("Would you like to encode or decode? ")
WORD = input("Please enter text: ")
LETTERS = string.ascii_letters + string.punctuation + string.digits
encoded = ''  # pylint: disable=invalid-name

if CHOICE == "encode":
    for letter in WORD:
        if letter == ' ':
            encoded += ' '
        else:
            index = (
                LETTERS.index(letter) + SHIFT
            )  # pylint: disable=invalid-name
            encoded += LETTERS[index]  # pylint: disable=invalid-name
elif CHOICE == "decode":
    for letter in WORD:
        if letter == ' ':
            encoded += ' '
        else:
            index = (
                LETTERS.index(letter) - SHIFT
            )  # pylint: disable=invalid-name
            encoded += LETTERS[index]  # pylint: disable=invalid-name

print(encoded)
