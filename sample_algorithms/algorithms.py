from typing import List


def insertion_sort(input_list: List)->None:
    """Sorts a list and returns the sorted in ascending order"""
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
