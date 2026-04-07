import pytest
from ft_filter import ft_filter


def is_even(n):
    """Return True if n is even."""
    return n % 2 == 0


def test_list_filter():
    """Filter even numbers from list."""
    assert ft_filter(is_even, [1, 2, 3, 4]) == [2, 4]
    assert ft_filter(is_even, []) == []
    assert ft_filter(is_even, [-10]) == [-10]
    assert ft_filter(is_even, [1]) == []


def test_none_function():
    """Filter truthy values when function is None."""
    assert ft_filter(None, [1, 2, 3, 4]) == [1, 2, 3, 4]  # all nbrs are true
    assert ft_filter(None, [0, 1, False, 2]) == [1, 2]
    # test for None function and set
    result = ft_filter(None, {0, 1, False, 2})
    assert sorted(result) == [1, 2]  # sorted() because set is UNORDERED
    # test for dictionary, iterated by key
    result_none = ft_filter(None, {0: "a", 1: "b", 2: "c"})
    assert result_none == [1, 2]


def test_tuple():
    """Filter tuple input."""
    assert ft_filter(is_even, (1, 2, 3, 4)) == [2, 4]
    assert ft_filter(None, (1, 2, 3, 4)) == [1, 2, 3, 4]


def test_set():
    """Filter set input."""
    data = {1, 2, 3, 4}
    result = ft_filter(is_even, data)
    assert sorted(result) == [2, 4]  # sorted() because set is UNORDERED


def test_dict():
    """Filter dictionary input (should iterate over keys) -> returns keys"""
    result = ft_filter(is_even, {1: "a", 2: "b", 3: "c", 4: "hello"})
    assert result == [2, 4]


def test_string():
    """Filter string input."""
    assert ft_filter(print, "abc") == []  # print("a") returns None → falsy.
    assert ft_filter(None, "abc") == ["a", "b", "c"]


def test_type_error_inside_function():
    """Raise TypeError when function fails."""
    with pytest.raises(TypeError):
        ft_filter(is_even, [1, "2", None, 4])
        ft_filter(is_even, (1, "2", None, 4))
        ft_filter(is_even, set(1, "2", None, 4))


def test_error():
    """Raise TypeError when iterable is None."""
    with pytest.raises(TypeError):
        ft_filter(is_even, None)


def test_set_against_builtin():
    """Compare set behaviour with built-in filter."""
    data = {1, 2, 3, 4}
    assert sorted(ft_filter(is_even, data)) == sorted(filter(is_even, data))


def test_dict_against_builtin():
    """Compare dict behaviour with built-in filter."""
    data = {1: "a", 2: "b", 3: "c", 4: "d"}
    assert ft_filter(is_even, data) == list(filter(is_even, data))
    # convertion to list because original filter returns iterator, not list!
    print(filter(is_even, [-2, 0, 14, 25, 23, 44]))
