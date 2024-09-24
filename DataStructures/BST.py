from collections import deque

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, new_node):
        if new_node.val <= self.val:
            if self.left:
                self.left.insert(new_node)
            else:
                self.left = new_node
        else:
            if self.right:
                self.right.insert(new_node)
            else:
                self.right = new_node

    @staticmethod
    def inorder_traversal(node, cb = None):
        if node:
            TreeNode.inorder_traversal(node.left, cb)
            cb(node) if cb else print(node, end=" ")
            TreeNode.inorder_traversal(node.right, cb)

    @staticmethod
    def preorder_traversal(node, cb = None):
        if node:
            cb(node) if cb else print(node, end=" ")
            TreeNode.preorder_traversal(node.left, cb)
            TreeNode.preorder_traversal(node.right, cb)
    
    @staticmethod
    def postorder_traversal(node, cb = None):
        if node:
            TreeNode.postorder_traversal(node.left, cb)
            TreeNode.postorder_traversal(node.right, cb)
            cb(node) if cb else print(node, end=" ")

    @staticmethod
    def inorder_traversal_iterative(node, cb = None):
        curr = node
        stack = deque()

        while(True):
            if curr:
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                cb(curr) if cb else print(curr, end=" ")
                curr = curr.right
            else: break

    @staticmethod
    def preorder_traversal_iterative(node, cb = None):
        curr = node
        stack = deque()
        while True:
            if curr:
                cb(curr) if cb else print(curr, end=" ")
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                curr = curr.right
            else: break

    @staticmethod
    def level_order_traversal(node, cb = None):
        curr = None
        queue = deque([node])

        while queue:
            curr = queue.popleft()
            cb(curr) if cb else print(curr, end=" ")
            queue.append(curr.left) if curr.left else None
            queue.append(curr.right) if curr.right else None

    def __str__(self):
        return f"{self.val}"