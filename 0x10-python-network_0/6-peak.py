#!/usr/bin/python3
""" module finds the peak of a number """


# find the peak
def find_peak(list_of_integers):
    """
        find the peak of list of numbers

        Args:
            list_of_integers: list of integers

        Returns: the number of the peak
    """

    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
