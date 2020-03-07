class Node:
    def __init__(self,value):
        self.data = value
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.head = None
    
    def insert_node(self,value):
        return self.insert_node(self.head)
    
    def insert(self,node,value):
        if not self.head.data:
            self.head = Node(value)
            return
        if value >= node:
            if not node.right:
                node.right = Node(value)
            else:
                return self.insert(node.right,value)
        else:
            if not node.left:
                node.left = Node(value)
                return
            else:
                return self.insert(node.left,value)
        
    def search_value(self,value):
        pass
        
        