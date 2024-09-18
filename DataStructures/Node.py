class Node:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        
    def __str__(self):
        return f"({self.key}:{self.val})"
    