class TreeNode:
    def __init__(self,val=0):
        self.val=val
        self.left=None
        self.right=None
def inorder(node):
    if node:
        inorder(node.left)
        print(node.val, end=" ")
        inorder(node.right)
def preorder(node):
    if node:
        print(node.val, end=" ")
        preorder(node.left)
        preorder(node.right)
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.val, end=" ")
from collections import deque

def level_order(root):
    if not root:
        return

    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = BSTNode(val)
        else:
            self._insert_recursive(self.root, val)

    def _insert_recursive(self, current, val):
        if val < current.val:
            if current.left is None:
                current.left = BSTNode(val)
            else:
                self._insert_recursive(current.left, val)
        else:
            if current.right is None:
                current.right = BSTNode(val)
            else:
                self._insert_recursive(current.right, val)

    def search(self, target) -> bool:
        current = self.root
        while current:
            if target == current.val:
                return True
            elif target < current.val:
                current = current.left
            else:
                current = current.right
        return False