"""Morse code encoder.

This program accepts a single string argument and prints its Morse code
representation. Supported characters: letters A-Z, digits 0-9 and space.
A space is encoded as '/'. Morse letters are separated by a single space.
If the arguments are invalid the program prints an AssertionError message.
"""

import sys


NESTED_MORSE = {
	"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
	"F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
	"K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
	"P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
	"U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
	"Z": "--..",
	"0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
	"5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
	" ": "/",
}


def is_valid_text(text):
	"""Return True if all characters in text are supported.

	The check is case-insensitive for letters.
	"""
	if not isinstance(text, str):
		return False
	for ch in text.upper():
		if ch not in NESTED_MORSE:
			return False
	return True


def encode_morse(text):
	"""Encode a valid text into Morse code and return the string."""
	upper = text.upper()
	morse_list = [NESTED_MORSE[ch] for ch in upper]
	return " ".join(morse_list)


def main():
	"""Parse arguments, validate input and print Morse encoding.

	On invalid arguments prints: AssertionError: the arguments are bad
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