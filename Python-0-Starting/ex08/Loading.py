'''The yield keyword turns a function into a function generator.
    The function generator returns an iterator.
    - The code inside the function is not executed when they are first called, but are divided 
    into steps, one step for each yield, and each step is only executed when iterated upon.
    - Unlike the return keyword which stops further execution of the function, the yield keyword 
    returns the result so far, and continues to the next step.
    - The return value will be a list of values, one item for each yield.
'''
import os


def ft_tqdm(lst: range)-> None:
    """Function that reproduces tqdm progress bar"""
    try:
        it = iter(lst)
    except TypeError:
        raise TypeError(f"\'{type(lst).__name__}\' object is not iterable")
    total = len(lst)
    for i, item in enumerate(lst, 1):
        # enumerate(lst, 1) - so visible progress starts from 1 and not 0,
        # enumerate returns pair (index; value)
        percent = int((i / total) * 100)
        bar_length = os.get_terminal_size().columns - 42 # 42 is space for text info, selected manually
        filled = int(bar_length * i / total)
        if filled == 0:
            bar = ">" + "-" * (bar_length - 1)
        elif filled < bar_length:
            bar = "=" * (filled - 1) + ">" + "-" * (bar_length - filled)
        else:
            bar = "=" * (bar_length - 1) + ">"
        print(f"\r{percent}%|[{bar}]| {i}/{total}", flush=True, end='')
        # \r moves cursor to the beginning of the line on EACH iteration
        # flush=True forces the line to be printed immediately
        # end='' prevents from adding a new line
        # EACH iteration OVERWRITES the previous text on the screen on the same line
        yield item
    print()
