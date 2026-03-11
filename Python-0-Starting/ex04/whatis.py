#!/usr/bin/env python3
import sys

try:
    # Expect exactly one argument
    if len(sys.argv) != 2:
        if len(sys.argv) == 1:
            # no output when no argument provided
            sys.exit(0)
        else:
            raise AssertionError("more than one argument is provided")
    # validate integer input by converting
    try:
        n = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")

except AssertionError as e:
    print(f"AssertionError: {e}")
    sys.exit(1)

# determine odd or even
if n % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
