"""
Sample Basic Algorithms
"""


def insertion_sort(input_list):
    """
    Sorts a list and returns the sorted in ascending order
    """
    i = 0
    list_length = len(input_list)-1
    while(i <= list_length):
        j = 0
        while(j <= list_length):
            if(input_list[i] < input_list[j]):
                temp = input_list[i]
                input_list[i] = input_list[j]
                input_list[j] = temp
            j += 1
        i += 1


def euclideanAlgorithm(m, n):
    """
    Ecuclidean algoruthm for finding the gcd of two numbers
    """
    if(n == 0):
        return m
    else:
        remainder = m % n
        return euclideanAlgorithm(n, remainder)
