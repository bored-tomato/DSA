import LinkedList
from Node import LinkedNode

class Queue:
    def __init__(self, value=None):
        if value: self.ll = LinkedList.LinkedList(LinkedNode(value))
        else: self.ll = LinkedList.LinkedList()

    def enqueue(self, value):
        return self.ll.insert_at_end(LinkedNode(value))

    def dequeue(self):
        return self.ll.remove_from_head()
    
    def peek(self):
        return self.ll.head
    
    def rear(self):
        return self.ll.tail
    
    def is_empty(self):
        return self.ll.is_empty()
    
    def __str__(self):
        return f"FRONT -- {self.ll} -- BACK"
