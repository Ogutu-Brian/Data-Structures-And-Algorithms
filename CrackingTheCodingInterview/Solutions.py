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

# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­ drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)


def palindrome_permutation(input):
    def is_palindrome(input_string):
        input_string = input_string.lower().strip().replace(' ', '')
        str_len = len(input_string)

        for index in range(str_len):
            if(input_string[index] != input_string[str_len - (index+1)]):
                return False

        return True
    # To do: Develop an an algorithm that uses the function


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

# Queue Data structure


class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

# Stack Data structure


class Stack:
    def __init__(self):
        self .items = []

    def __str__(self):
        return str(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items) - 1]

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

# Form a Queue from two stacks


class QueueFromTwoStacks:
    def __init__(self):
        self.newest_stack = Stack()
        self.oldest_stack = Stack()

    def enqueue(self, item):
        self.newest_stack.push(item)

    def peek(self):
        return self.oldest_stack.top()

    def dequeue(self, item):
        self.shift_stacks()
        return self.oldest_stack.pop()

    def size(self):
        return self.oldest_stack.size() + self.newest_stack.size()

    def is_empty(self):
        self.shift_stacks()
        return self.oldest_stack.is_empty()

    def shift_stacks(self):
        if(self.oldest_stack.is_empty()):
            while not self.newest_stack.is_empty():
                self.oldest_stack.push(self.newest_stack.pop())

# Detecting cycles in a linked list


class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, value=None):
        self.root = Node(value)
        self.size = 1

    def insert_at_index(self, index, value):
        if self.size - 1 < index:
            return

        node = Node(value)
        
        if index == 0:
            next_node = self.root
            self.root = node
            self.root.next = next_node
            self.root.next.previous = self.root
            self.size += 1
        else:
            current_node = self.root.next
            
            for i in range(1, index+1):
                if i == index:
                    previous_node = current_node.previous
                    next_node = current_node.next
                    previous_node.next = node
                    previous_node.next.next = current_node
                    current_node.previous = previous_node.next.next
                    self.size = self.size + 1
                    return 
                
                current_node = current_node.next
                
    def print_linked_list(self):
        linked_list = []
        current_node = self.root
        
        while True:
            linked_list.append('{}->'.format(current_node.value))

            if not current_node.next:
                break
            current_node = current_node.next
        
        print((' ').join(linked_list))
    
    def pre_pend(self,value):
        root_node = self.root
        node = Node(value)
        self.root = node
        self.root.next = root_node
        self.root.next.previous = self.root
        self.size += 1
    
    def append(self,value):
        current_node = self.root

        while True:
            if not current_node.next:
                current_node.next = Node(value)
                current_node.next.previous = current_node
                self.size += 1
                return
            
            current_node = current_node.next
    
    def delete_at_index(self,index):
        if index not in range(self.size):
            return
        
        if index == 0:
            current_node = self.root
            self.root = current_node.next
            self.root.previous = None
            self.size -= 1
            return
        
        current_node = self.root.next
        
        for i in range(self.size):
            if index == i:
                self.delete_node(current_node)
                self.size -= 1
                return
                
        current_node = current_node.next
    
    def delete_node(self,node):
        previous_node = node.previous
        next_node = node.next
        previous_node.next = next_node
        previous_node.next.previous = previous_node
    
    def search_from_root(self,node,value):
        if node.value == value:
            return node.value
        
        if not node.next:
            return
        return self.search_from_root(node.next,value)
    
    def search(self,value):
        return self.search_from_root(self.root,value)
    
    def deletion_by_value(self,node,value):
        if value == node.value:
            previous_node = node.previous
            next_node = node.next
            if node.previous:
                previous_node.next = next_node
            previous_node.next.previous = previous_node
        
        if not node.next:
            return
        
        return self.deletion_by_value(node.next,value)
    
    def delete_by_value(self,value):
        return self.deletion_by_value(self.root,value)
        
        
    
linked_list = DoublyLinkedList(0)
linked_list.insert_at_index(0,2)
linked_list.insert_at_index(0,3)
linked_list.insert_at_index(0,4)
linked_list.insert_at_index(2,6)
linked_list.insert_at_index(4,45)
linked_list.pre_pend(10)
linked_list.pre_pend(30)
linked_list.append(100)
linked_list.print_linked_list()
linked_list.delete_at_index(1)
linked_list.print_linked_list()
linked_list.delete_by_value(10)
print(linked_list.search(10))
linked_list.print_linked_list()