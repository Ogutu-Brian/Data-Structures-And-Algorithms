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


def bubble_sort(values):
    values_length = len(values)

    if values_length <= 2:
        if values_length == 0:
            return values

        if values_length == 1:
            return values

        if values[0] > values[1]:
            return [values[1], values[0]]
        return values

    has_swaps = True

    while has_swaps:
        contains_swaps = False
        count = 1

        for i in range(values_length):
            if i + 1 == values_length:
                break

            if values[i] > values[i+1]:
                contains_swaps = True
                temp = values[i]
                values[i] = values[i+1]
                values[i+1] = temp

        has_swaps = contains_swaps

    return values


def selection_sort(items):
    sorted_items = []

    while len(items) > 0:
        min_element = min(items)
        sorted_items.append(min_element)
        items.remove(min_element)

    return sorted_items


def merge_sort(items):
    def merge(left_items, right_items):
        copy_array = []

        while len(left_items) or len(right_items):
            if len(left_items) and len(right_items):
                if left_items[0] > right_items[0]:
                    value = right_items[0]
                    copy_array.append(value)
                    right_items.remove(value)
                else:
                    value = left_items[0]
                    copy_array.append(value)
                    left_items.remove(value)
            else:
                if not len(left_items):
                    copy_array.extend(right_items)
                    return copy_array
                else:
                    copy_array.extend(left_items)
                    return copy_array

    if len(items) <= 1:
        return items

    mid = int(len(items)/2)
    left = merge_sort(items[0:mid])
    right = merge_sort(items[mid:])

    return merge(left, right)


def quick_sort(items):
    items_length = len(items)

    if items_length <= 1:
        return items

    if items_length == 2:
        return [items[0], items[1]] if items[0] < items[1] else [items[1], items[0]]

    pivot = items[items_length-1]
    exact = [x for x in items if x == pivot]
    left = quick_sort([x for x in items if x < pivot])
    right = quick_sort([x for x in items if x > pivot])

    cumulative = []

    if left:
        cumulative.extend(left)

    cumulative.extend(exact)

    if right:
        cumulative.extend(right)

    return cumulative
