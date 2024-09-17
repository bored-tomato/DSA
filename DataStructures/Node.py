class Node:
    def __init__(self, key, val, next = None):
        self.key = key
        self.val = val
        self.next = next
        
    def __str__(self):
        return f"({self.key}:{self.val})"
    