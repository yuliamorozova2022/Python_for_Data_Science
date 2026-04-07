# this file indicates that this directory is a python package
# file can be empty, but this line:

from .count_in_list import count_in_list

__all__ = ["count_in_list"]
# This explicitly declares the symbol as part of the package
# public API, so the import is recognized as intentional.

# allows to do import somewhere as
#    from ft_package import count_in_list
# instead of case for empty __init__.py file:
#    from ft_package.count_in_list import count_in_list
