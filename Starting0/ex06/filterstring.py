import sys
from ft_filter import ft_filter

def main():
    try:
        assert len(sys.argv) == 3, "AssertionError: the arguments are bad"
        input_string = sys.argv[1].split()
        filtered = ft_filter(lambda x: len(x) > int(sys.argv[2]), input_string)
        print(filtered)
        print("[", ", ".join(filtered), "]", sep="")

    except AssertionError as e:
        print(f"AssertionError: {e}")
        return


if __name__ == "__main__":
    main()
