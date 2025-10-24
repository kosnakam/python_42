import sys
from ft_filter import ft_filter


def main():
    """Main function to filter strings based on length."""
    try:
        assert len(sys.argv) == 3
        assert sys.argv[2].isdigit()
        input_string = sys.argv[1].split()
        filtered = list(
            ft_filter(lambda x: len(x) > int(sys.argv[2]), input_string)
            )
        if not len(filtered):
            print("[]")
        else:
            print("['", "', '".join(filtered), "']", sep="")

    except AssertionError:
        print("AssertionError: the arguments are bad")
    return


if __name__ == "__main__":
    main()
