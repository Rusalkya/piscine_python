"""Program that filters words longer than a given length."""

import sys

from ft_filter import ft_filter


def parse_arguments(arguments):
    """Validate and convert command-line arguments."""
    if len(arguments) != 2:
        return None, None

    text = arguments[0]

    try:
        length = int(arguments[1])
    except ValueError:
        return None, None

    return text, length


def filter_words(text, minimum_length):
    """Return the words in text that are longer than minimum_length."""

    def predicate(word):
        return len(word) > minimum_length

    words = text.split(" ")
    return ft_filter(predicate, words)


def main():
    """Run the filtering program and handle argument errors."""
    text, minimum_length = parse_arguments(sys.argv[1:])

    if text is None:
        print("AssertionError: the arguments are bad")
        return

    print(filter_words(text, minimum_length))


if __name__ == "__main__":
    main()
