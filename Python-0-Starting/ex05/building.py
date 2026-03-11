import sys


def calculate_characters(text):
    """Return counts for different kinds of characters in *text*.

    The returned list has the following elements in order:
    [total, upper_case, lower_case, punctuation, spaces, digits].
    Newlines and carriage returns are treated as spaces so that
    the carriage return counts as a space as specified by the task.
    """
    upper_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_set = "abcdefghijklmnopqrstuvwxyz"
    punctuation_set = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    spaces_set = " \t\r\n"
    digits_set = "0123456789"
    arr = [len(text), 0, 0, 0, 0, 0]
    for c in text:
        if c in upper_set:
            arr[1] += 1
        elif c in lower_set:
            arr[2] += 1
        elif c in punctuation_set:
            arr[3] += 1
        elif c in spaces_set:
            arr[4] += 1
        elif c in digits_set:
            arr[5] += 1
    return arr


def print_message(arr):
    """Display the counts produced by :func:`calculate_characters`.

    *arr* is the list returned by :func:`calculate_characters`.
    arr[0] is the total number of characters.
    """
    print(f"The text contains {arr[0]} characters:\n"
          f"{arr[1]} upper letters\n"
          f"{arr[2]} lower letters\n"
          f"{arr[3]} punctuation marks\n"
          f"{arr[4]} spaces\n"
          f"{arr[5]} digits")

def main():
    """Parse arguments, prompt if necessary, and call helper functions.

    The only condition that is explicitly handled is an argument count
    exceeding two; it is converted into an :class:`AssertionError` which is
    caught immediately.  No other exception is caught, so any unexpected
    error will propagate and cause a crash (invalidating the exercise).
    """

    # validate argument count
    try:
        assert len(sys.argv) <= 2, "Too many arguments."
    except AssertionError as e:
        # only the deliberately raised AssertionError is caught here; the
        # program exits cleanly with status 1 and no traceback is shown.
        print(f"AssertionError: {e}")
        sys.exit(1)

    # collect text and handle any unexpected I/O/processing errors
    try:
        if len(sys.argv) == 1:
            print('What is the text to count?')
            # sys.stdin.read() behaviour described in docstring above
            text = sys.stdin.read()
        else:  # exactly two elements
            text = sys.argv[1]

        # omit blank line if input didn't end in newline (keeps output separate)
        if not text.endswith("\n"):
            print()
        print_message(calculate_characters(text))

    except (Exception, KeyboardInterrupt) as e:
        # catch IOError, KeyboardInterrupt, bugs, etc.;
        # newline in case the interrupted input left the cursor on the same line
        print()
        # only include the exception message if it is non‑empty
        msg = "Unexpected error"
        if e:
            msg += f": {e}"
        print(msg)
        sys.exit(1)


if __name__ == '__main__':
    main()


"""
import sys


def calculate_characters(text):
    upper_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_set = "abcdefghijklmnopqrstuvwxyz"
    punctuation_set = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    spaces_set = " \t\r\n"
    digits_set = "0123456789"
    arr = [len(text), 0, 0, 0, 0, 0]
    for c in text:
        if c in upper_set:
            arr[1] += 1
        elif c in lower_set:
            arr[2] += 1
        elif c in punctuation_set:
            arr[3] += 1
        elif c in spaces_set:
            arr[4] += 1
        elif c in digits_set:
            arr[5] += 1
    return arr


def print_message(arr):
    print(f"The text contains {arr[0]} characters:\n"
          f"{arr[1]} upper letters\n"
          f"{arr[2]} lower letters\n"
          f"{arr[3]} punctuation marks\n"
          f"{arr[4]} spaces\n"
          f"{arr[5]} digits")

def main():
    try:
        if len(sys.argv) == 1:
            text = input('What is the text to count?\n')
        elif len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            raise AssertionError('Too many arguments.')
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return
    print_message(calculate_characters(text))


if __name__ == '__main__':
    main()
"""