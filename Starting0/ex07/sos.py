import sys


def main():
    try:
        assert len(sys.argv) == 2
        assert all(c == ' ' or c.isalpha() for c in sys.argv[1])

        text = sys.argv[1].upper()
        nested_morse = {
            " ": "/ ",
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
            "Z": "--.."
        }
    
        output_list = [nested_morse[c] for c in text if c in nested_morse]
        output = ' '.join(output_list)
        print (output)

    except AssertionError:
        print ("AssertionError: the arguments are bad")
    return


if __name__ == "__main__":
    main()