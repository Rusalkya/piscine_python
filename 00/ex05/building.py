"""docstring: python program that counts each type of characters and return its number."""
import string
import sys

def get_text(arguments):
	"""Return the text to analyze, prompting the user if needed."""
	if len(arguments) == 0 or arguments[0] == "":
		print("What is the text to count?")
		return sys.stdin.readline()
	return arguments[0]


def count_text(text):
	"""Count upper, lower, punctuation, space, and digit characters."""
	counts = {
		"upper": 0,
		"lower": 0,
		"punctuation": 0,
		"spaces": 0,
		"digits": 0,
	}

	for character in text:
		if character.isupper():
			counts["upper"] += 1
		elif character.islower():
			counts["lower"] += 1
		elif character in string.punctuation:
			counts["punctuation"] += 1
		elif character.isspace():
			counts["spaces"] += 1
		elif character.isdigit():
			counts["digits"] += 1

	return counts


def display_counts(text):
	"""Display the character statistics for a text."""
	counts = count_text(text)

	print(f"The text contains {len(text)} characters:")
	print(f"{counts['upper']} upper letters")
	print(f"{counts['lower']} lower letters")
	print(f"{counts['punctuation']} punctuation marks")
	print(f"{counts['spaces']} spaces")
	print(f"{counts['digits']} digits")


def main():
	"""Run the program and handle command-line argument validation."""
	arguments = sys.argv[1:]

	if len(arguments) > 1:
		print("AssertionError: more than one argument is provided")
		return

	text = get_text(arguments)
	display_counts(text)


if __name__ == "__main__":
	main()