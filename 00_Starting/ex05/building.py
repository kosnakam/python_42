import sys
import string


def main():
    """Main function to analyze text input from command line arguments."""
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) == 1:
            print("What is the text to count?")
            element = input()
        else:
            element = sys.argv[1]
        print("The text contains", len(element), "characters:")
        print(
            sum(1 for char in element if char.isupper()), "upper letters"
            )
        print(
            sum(1 for char in element if char.islower()), "lower letters"
            )
        print(
            sum(
                1 for char in element if char in string.punctuation
                ), "punctuation marks"
            )
        print(sum(1 for char in element if char.isspace()), "spaces")
        print(sum(1 for char in element if char.isdigit()), "digits")
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Error: {e}")
    return


if __name__ == "__main__":
    main()
