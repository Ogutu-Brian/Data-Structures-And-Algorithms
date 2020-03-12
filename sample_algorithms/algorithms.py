"""
Sample Basic Algorithms
"""
from typing import List


def insertion_sort(input_array: List) -> List:
    j = 1
    while j <= (len(input_array)-1):
        key = input_array[j]
        i = j - 1

        while i >= 0 and input_array[i] > key:
            input_array[i + 1] = input_array[i]
            i -= 1

        input_array[i + 1] = key
        j += 1

    return input_array


def euclideanAlgorithm(m: int, n: int):
    """
    Ecuclidean algorithm for finding the gcd of two numbers
    """
    if(n == 0):
        return m
    else:
        remainder = m % n
        return euclideanAlgorithm(n, remainder)


def consucetive_integer_checking_algorithm(m: int, n: int) -> int:
    """
    Using consucutive integer checking algorithm for gcd of two numbers
    """
    result = max(m, n)
    t = min(m, n)

    if t != 0:
        while (m % t != 0 or n % t != 0):
            t -= 1
        result = t

    return result
