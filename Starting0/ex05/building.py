import sys
import string


def main():
    """
    Main function to analyze text input from command line arguments.
    """
    try:
        assert len(sys.argv) == 2, "Please provide exactly one argument."
        print("The text contains", len(sys.argv[1]), "characters:")
        print(
            sum(1 for char in sys.argv[1] if char.isupper()), "upper letters"
            )
        print(
            sum(1 for char in sys.argv[1] if char.islower()), "lower letters"
            )
        print(
            sum(
                1 for char in sys.argv[1] if char in string.punctuation
                ), "punctuation marks"
            )
        print(sum(1 for char in sys.argv[1] if char.isspace()), "spaces")
        print(sum(1 for char in sys.argv[1] if char.isdigit()), "digits")
    except AssertionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    return


if __name__ == "__main__":
    main()
