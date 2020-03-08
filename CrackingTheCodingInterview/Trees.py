class Node(object):
    def __init__(self, value):
        self.data = value
        self.children = []

class Tree:
    def __init__(self):
        self.root = None