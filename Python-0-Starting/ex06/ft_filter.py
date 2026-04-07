# print(filter.__doc__)
"""
according documentation, original filter() returns iterator
but according task, list comprehension is required -> ft_filter() returns list
"""


def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return a list of items of iterable for which function(item)
is true. If function is None, return the items that are true.
"""
    if iterable is None:
        raise TypeError('Iterable is required')
    if function is None:
        return [item for item in iterable if item]  # list comprehension
    return [item for item in iterable if function(item)]
