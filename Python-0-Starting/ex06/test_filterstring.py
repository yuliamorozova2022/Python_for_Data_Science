# import pytest
from filterstring import calculate_words


def test_basic_case():
    """Returned words longer than n"""
    assert calculate_words("Hello the world", 4) == ["Hello", "world"]
    assert calculate_words("Hello the world", -4) == ["Hello", "the", "world"]
    assert calculate_words("one two three", 3) == ["three"]


def test_empty_result():
    """Return empty list if no word matches."""
    assert calculate_words("", 4) == []
    assert calculate_words("Hello world", 94) == []
