# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
# Hints: #44, #777, #732

def is_unique(example_string):
    example_string = example_string.lower()
    index = 1

    for character in example_string:
        if character in example_string[index:]:
            return False
        index += 1

    return True

# Check Permutation: Given two strings,write a method to decide if one is a permutation of the
# other.
def check_permutation(first_string, last_string):
    if(len(first_string) != len(last_string)):
        return False

    first_char_list = list(first_string.lower())
    last_char_list = list(last_string.lower())
    array_length = len(first_char_list)

    first_char_list.sort()
    last_char_list.sort()

    for index in range(array_length):
        if first_char_list[index] != last_char_list[index]:
            return False

    return True

# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters,and that you are given the "true" length of the string. (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith "
# Output: "Mr%20John%20Smith"

def urlify(input):
    return input.strip().replace(' ','%20')
