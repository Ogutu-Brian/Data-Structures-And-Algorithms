# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
# Hints: #44, #7 7 7, #732

def is_unique(example_string):
    index = 1

    for character in example_string:
        if character in example_string[index:]:
            return False
        index += 1
        
    return True
