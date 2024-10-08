import LinkedList
from Node import LinkedNode

class Stack:
    def __init__(self, value=None):
        if value: self.ll = LinkedList.LinkedList(LinkedNode(value))
        else: self.ll = LinkedList.LinkedList()

    def push(self,value):
        return self.ll.insert_at_head(LinkedNode(value))

    def pop(self):
        return self.ll.remove_from_head()

    def peek(self):
        return self.ll.head

    def is_empty(self):
        return self.ll.is_empty()
    
    def __str__(self):
        return f"TOP --- {self.ll} --- BOTTOM"
