def count_in_list(lst, item):
    """
    Count occurrences of an item in a list.

    Args:
       lst (list): list to search in
       item: value to count

    Returns:
       int: number of occurrences
    """
    if not isinstance(lst, list):
        raise TypeError(f"\'{type(lst).__name__}\' object is not a list")
    counter = 0
    for element in lst:
        if element == item:
            counter += 1
    return counter

#
# def main():
#     try:
#         print(count_in_list(None, 3))
#     except Exception as e:
#         print(e)
#     try:
#         print(count_in_list(set([1, 2, 3]), 3))
#     except Exception as e:
#         print(e)
#     try:
#         print(count_in_list((1, 2, 3), 3))
#     except Exception as e:
#         print(e)
#     try:
#         print(count_in_list([], 3)) # empty list - 0
#         print(count_in_list([1, 2, 3, 4, 5], None)) # empty item - 0
#         print(count_in_list([1, 2, 3, 4, 5], 10)) # item not in the list - 0
#         print(count_in_list([1, 2, 3, 2, 1], 3)) # valid item - 1
#         print(count_in_list([1, 2, 3, 2, 1], 2)) # valid item - 2
#     except Exception as e:
#         print(e)
#
#
# if __name__ == '__main__':
#     main()