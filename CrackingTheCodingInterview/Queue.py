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
