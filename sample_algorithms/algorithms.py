"""
Sample Basic Algorithms
"""
from math import sqrt


def insertion_sort(input_array):
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


def euclideanAlgorithm(m, n):
    """
    Ecuclidean algorithm for finding the gcd of two numbers
    """
    if(n == 0):
        return m
    else:
        remainder = m % n
        return euclideanAlgorithm(n, remainder)


def consucetive_integer_checking_algorithm(m, n):
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


def is_prime(number):
    if number < 2:
        return False

    boundary = int(sqrt(number))

    for i in range(2, boundary + 1):
        if number % i == 0:
            return False

    return True


def sieve_of_eratosthenese(limit):
    boundary = int(sqrt(limit))
    list_content = list(range(limit+1))

    for i in range(2, boundary + 1):
        if list_content[i] != 0:
            j = i**2

            while j <= limit:
                list_content[j] = 0
                j += i

    return [x for x in list_content if x >= 2]


def fibunacci(value):
    def fib(n, memo):
        if n == 0 or n == 1:
            return n

        if not memo.get(n):
            memo[n] = fib(n-1, memo) + fib(n-2, memo)

        return memo.get(n)

    return fib(value, {})
