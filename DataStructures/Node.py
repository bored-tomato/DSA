class Node:
    def __init__(self, val):
        self.val = val

class LinkedNode(Node):
    def __init__(self, val, prev = None, next = None):
        super().__init__(val)
        self.prev = prev
        self.next = next
        
    def __str__(self):
        return f"{self.val}"
    
class GraphNode(Node):
    def __init__(self, key, val):
        super().__init__(val)
        self.key = key

    def __str__(self):
        return f"{self.key}: {self.val}"