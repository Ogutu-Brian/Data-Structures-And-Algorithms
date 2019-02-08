from typing import List, Tuple


def insertion_sort(input_list: List)->None:
    """Sorts a list and returns the sorted"""
    i = 1
    list_length = len(input_list)-1
    while(i < list_length):
        j = i
        while(j < list_length):
            if(input_list[j] < input_list[j-1]):
                temp = input_list[j]
                input_list[j] = input_list[j-1]
                input_list[j-1] = temp
            j += 1
        i += 1
