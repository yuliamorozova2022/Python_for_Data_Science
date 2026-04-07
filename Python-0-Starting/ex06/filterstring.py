import sys
# from ft_filter import ft_filter


def calculate_words(text, number):
    """
    Returns a list of words in 'text' with length greater than 'number'.
    :param text: str - input string
    :param number: int - minimum length
    :return: list of words
    """
    # split the string into words
    words = text.split()
    # use lambda and ft_filter to filter words
    # return ft_filter(lambda w: len(w) > number, words)
    # usage of previously implemented function
    return [w for w in words if (lambda x: len(x) > number)(w)]
    # w for w in words if (Lambda function) - List comprehension
    # (lambda x: len(x) > number) - lambda declaration
    # call of lambda function (lambda x: len(x) > number)(w)


def main():
    """Program entry point: validates input and prints filtered words"""
    try:
        assert len(sys.argv) == 3, "the arguments are bad."
        text = sys.argv[1]
        number = int(sys.argv[2])
        print(calculate_words(text, number))
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"ValueError: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
