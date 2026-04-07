import sys


def convert_to_morse(text):
    """Converts text to morse code."""
    MORSE_DICT = {'A': '.- ', 'B': '-... ', 'C': '-.-. ', 'D': '-.. ',
                  'E': '. ', 'F': '..-. ', 'G': '--. ', 'H': '.... ',
                  'I': '.. ', 'J': '.--- ', 'K': '-.- ', 'L': '.-.. ',
                  'M': '-- ', 'N': '-. ', 'O': '--- ', 'P': '.--. ',
                  'Q': '--.- ', 'R': '.-. ', 'S': '... ', 'T': '- ',
                  'U': '..- ', 'V': '...- ', 'W': '.-- ', 'X': '-..- ',
                  'Y': '-.-- ', 'Z': '--.. ', ' ': '/ ',
                  '1': '.---- ', '2': '..--- ', '3': '...-- ', '4': '....- ',
                  '5': '..... ', '6': '-.... ', '7': '--... ', '8': '---.. ',
                  '9': '----. ', '0': '----- '
                  }
    result = ""
    for char in text.upper():
        if char in MORSE_DICT:
            result += MORSE_DICT[char]
    return result.rstrip()


def validate_input(text):
    """Checks if input string contains only
    alphanumeric characters and spaces."""
    return all(char.isalnum() or char == " " for char in text)


def main():
    """Program entry point:
    validates input and prints converted to Morse Code words"""
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad.")
        if not validate_input(sys.argv[1]):
            raise AssertionError("the arguments are bad.")
        print(convert_to_morse(sys.argv[1]))
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
