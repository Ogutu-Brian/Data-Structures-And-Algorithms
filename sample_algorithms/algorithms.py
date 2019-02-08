from typing import List, Tuple


def swap_values(a, b)->Tuple:
    """Swaps input values"""
    return b, a


def insertion_sort(input_list: List)->List:
    """Sorts a list and returns the sorted list"""
    i = 1
    for item in input_list:
        j = i+1
        while j < len(input_list)-1:
            if(input_list[j-1] > input_list[j]):
                new_values = swap_values(input_list[j-1], input_list[j])
                input_list[j-1] = new_values[0]
                input_list[j] = new_values[1]
            J += 1
        i += 1
