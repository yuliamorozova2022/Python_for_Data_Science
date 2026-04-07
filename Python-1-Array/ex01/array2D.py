def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a 2D array (list of lists) from start to end index.

    :param family: 2D list, all inner lists must have the same length
    :param start: start index for slicing
    :param end: end index for slicing
    :return: truncated 2D list
    """
    # check if it's a list
    if not isinstance(family, list):
        raise TypeError('Family must be a list')
    # check if all elements are lists
    if not all(isinstance(row, list) for row in family):
        raise TypeError("Each element of input must be a list")
    # check if start is int
    if not isinstance(start, int):
        raise TypeError('Start must be an integer')
    # check if end is int
    if not isinstance(end, int):
        raise TypeError('End must be an integer')
    # if empty list -just return empty list
    if len(family) == 0:
        return []
    # check for list length (all elements have to be equal)
    row_length = len(family[0])
    if not all(len(row) == row_length for row in family):
        raise ValueError('Family elements must have the same length')
    # print shape of original list
    print(f"My shape is : ({len(family)}, {row_length})")
    # new list by slicing (start - included, end - excluded)
    new_family = family[start: end]
    print(f"My new shape is : ({len(new_family)}, {row_length})")
    return new_family
