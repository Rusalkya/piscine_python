import sys


def main():
    if len(sys.argv) == 1:
        return

    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")

    arg = sys.argv[1]

    try:
        number = int(arg)
    except ValueError:
        print("argument is not an integer")
        return

    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    main()
