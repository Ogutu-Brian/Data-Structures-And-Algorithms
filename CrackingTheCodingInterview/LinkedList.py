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

    def pre_pend(self, value):
        root_node = self.root
        node = Node(value)
        self.root = node
        self.root.next = root_node
        self.root.next.previous = self.root
        self.size += 1

    def append(self, value):
        current_node = self.root

        while True:
            if not current_node.next:
                current_node.next = Node(value)
                current_node.next.previous = current_node
                self.size += 1
                return

            current_node = current_node.next

    def delete_at_index(self, index):
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

    def delete_node(self, node):
        previous_node = node.previous
        next_node = node.next
        previous_node.next = next_node
        previous_node.next.previous = previous_node

    def search_from_root(self, node, value):
        if node.value == value:
            return node.value

        if not node.next:
            return
        return self.search_from_root(node.next, value)

    def search(self, value):
        return self.search_from_root(self.root, value)

    def deletion_by_value(self, node, value):
        if value == node.value:
            previous_node = node.previous
            next_node = node.next
            if node.previous:
                previous_node.next = next_node
            previous_node.next.previous = previous_node

        if not node.next:
            return

        return self.deletion_by_value(node.next, value)

    def delete_by_value(self, value):
        self.size -= 1
        return self.deletion_by_value(self.root, value)

    def introduce_cycle(self):
        current_node = self.root
        last_node = None

        while True:
            if not current_node.next:
                current_node.next = self.root
                self.root.previous = current_node
                return

            current_node = current_node.next


    # Detecting cycles in a linked list
    def has_cycles(self):
        current_node = self.root
        fast = current_node.next
        slow = current_node

        while fast.next and slow.next:
            if not current_node.next:
                return False

            if fast == slow:
                return True
            
            fast = fast.next.next
            slow = slow.next

        return False
    
# linked_list = DoublyLinkedList(0)
# linked_list.insert_at_index(0, 2)
# linked_list.insert_at_index(0, 3)
# linked_list.insert_at_index(0, 4)
# linked_list.insert_at_index(2, 6)
# linked_list.insert_at_index(4, 45)
# linked_list.pre_pend(10)
# linked_list.pre_pend(30)
# linked_list.append(100)
# linked_list.print_linked_list()
# linked_list.delete_at_index(1)
# linked_list.print_linked_list()
# linked_list.delete_by_value(10)
# print(linked_list.search(10))
# linked_list.print_linked_list()
# linked_list.introduce_cycle()
# print(linked_list.has_cycles())
