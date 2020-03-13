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
    first_char_list = list(first_string.lower())
    last_char_list = list(last_string.lower())

    first_char_list.sort()
    last_char_list.sort()

    return first_char_list == last_char_list

# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters,and that you are given the "true" length of the string. (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith "
# Output: "Mr%20John%20Smith"


def urlify(input):
    return input.strip().replace(' ', '%20')


def is_palindrome(input_string):
    def is_valid(character):
        return character.isalpha()

    input_string = input_string.lower()
    str_len = len(input_string)

    for index in range(str_len):
        backward_index = str_len - (index + 1)
        if (input_string[index] != input_string[backward_index]) or not is_valid(input_string[index]) or not is_valid(input_string[backward_index]):
            return False

        if backward_index == index:
            return True

# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­ drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)


def palindrome_permutation(data):
    data = list(data.lower())
    container = []

    for item in data:
        if item.isalpha():
            if item in container:
                container.remove(item)
            else:
                container.append(item)

    return len(container) <= 1

# An algorithm for balancing Parentheses in an expression
# Balanced {}()[{}] , [({})], ({[]})
# Unbalanced [({)}], ({[}), ()}[]


def is_balanced(expression):
    tokens = [['{', '}'], ['[', ']'], ['(', ')']]
    expression_length = len(expression)
    stack = []

    if expression_length % 2 != 0:
        return False

    def get_opening_token_index(token):
        closing_tokens = ['}', ']', ')']
        index = 0

        if token in closing_tokens:
            for item in closing_tokens:
                if token == item:
                    return index
                index += 1

        return None

    stack.append(expression[0])

    for token in expression:
        opening_token_index = get_opening_token_index(token)

        if(opening_token_index != None):
            expected_token = stack.pop()

            if tokens[opening_token_index][0] != expected_token:
                return False
        else:
            stack.append(token)

    return True

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


def max_sub_array(nums):
    if len(nums) == 1:
        return nums[0]

    total = nums[0]
    best = nums[0]

    for i in nums[1:]:
        if i > (total + i):
            total = i
        else:
            total += i

        best = max(best, total)

    return best
