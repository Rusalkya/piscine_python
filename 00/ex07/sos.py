"""Morse code encoder.

This program accepts a single string argument and prints its Morse
translation.

Supported characters:
- letters A-Z
- digits 0-9
- space

A space is encoded as '/'.
Morse letters are separated by a single space.

If the arguments are invalid, the program prints an AssertionError
message.
"""

import sys


MORSE_TRANSLATION = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/",
}


def is_valid_text(text):
    """Return True if all characters in text are supported.

    The check is case-insensitive for letters.
    """
    if not isinstance(text, str):
        return False

    for char in text.upper():
        if char not in MORSE_TRANSLATION:
            return False

    return True


def encode_morse(text):
    """Encode valid text into Morse code."""
    upper = text.upper()
    morse_list = [MORSE_TRANSLATION[char] for char in upper]
    return " ".join(morse_list)


def main():
    """Parse arguments and print Morse encoding.

    On invalid arguments:
    AssertionError: the arguments are bad
    """
    args = sys.argv[1:]

    if len(args) != 1:
        print("AssertionError: the arguments are bad")
        return

    text = args[0]

    if not is_valid_text(text):
        print("AssertionError: the arguments are bad")
        return

    print(encode_morse(text))


if __name__ == "__main__":
    main()
