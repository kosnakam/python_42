import sys


def main():
    try:
        assert len(sys.argv) == 2, "Please provide exactly one argument."
        print("The text contains", count_char(sys.argv[1]), "characters:")
        print(count_upper(sys.argv[1]), "upper letters")
        print(count_lower(sys.argv[1]), "lower letters")
        print(count_punctuation(sys.argv[1]), "punctuation marks")
        print(count_spaces(sys.argv[1]), "spaces")
        print(count_digits(sys.argv[1]), "digits")
    except AssertionError as e:
        print(f"Error: {e}")
        return


def count_char(s: str) -> int:
    try:
        return len(s)
    except Exception as e:
        print(f"Error: {e}")
        return 0


def count_upper(s: str) -> int:
    try:
        return sum(1 for char in s if char.isupper())
    except Exception as e:
        print(f"Error: {e}")
        return 0


def count_lower(s: str) -> int:
    try:
        return sum(1 for char in s if char.islower())
    except Exception as e:
        print(f"Error: {e}")
        return 0


def count_punctuation(s: str) -> int:
    try:
        return sum(1 for char in s if char in '.,;:!?\'"()-')
    except Exception as e:
        print(f"Error: {e}")
        return 0


def count_spaces(s: str) -> int:
    try:
        return sum(1 for char in s if char.isspace())
    except Exception as e:
        print(f"Error: {e}")
        return 0


def count_digits(s: str) -> int:
    try:
        return sum(1 for char in s if char.isdigit())
    except Exception as e:
        print(f"Error: {e}")
        return 0


if __name__ == "__main__":
    main()
