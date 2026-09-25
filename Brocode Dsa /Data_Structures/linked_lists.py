class Node:
    def __init__(self,value=0,next=None):
        self.value=value
        self.next=next


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at Head: O(1)
    def push_front(self, val):
        new_node = Node(val, self.head)
        self.head = new_node

    # Insert at Tail: O(n) without tail pointer, O(1) with tail pointer
    def push_back(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    # Delete by Value: O(n)
    def delete(self, val):
        if not self.head:
            return

        # Case 1: Head node holds the value
        if self.head.val == val:
            self.head = self.head.next
            return

        # Case 2: Search for value in remaining nodes
        curr = self.head
        while curr.next and curr.next.val != val:
            curr = curr.next

        if curr.next:
            curr.next = curr.next.next  # Bypass the deleted node

    # Traversal & Display: O(n)
    def display(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(str(curr.val))
            curr = curr.next
        print(" -> ".join(nodes) + " -> None")