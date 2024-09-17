from Node import Node

class SinglyLinkedList:
    def __init__(self, head = None):
        self.count = 0
        self.head = head
    
    def find(self, target_key):
        temp = self.head
        target_node = None

        while(temp):
            if(temp.key == target_key):
                target_node = temp
                break
            temp = temp.next

        return target_node if target_node else None

    def insert_at_head(self, key, val):
        self.count += 1
        new_node = Node(key, val)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, target_key, key, val):
        temp = self.head
        target_node = self.find(target_key)

        if (not target_node):
            return
        
        new_node = Node(key, val)
        new_node.next = target_node.next
        target_node.next = new_node
    
    def insert_at_end(self, key, val):
        temp = self.head

        if(not self.head):
            self.head = new_node
            return

        while(temp.next):
            temp = temp.next

        new_node = Node(key,val)
        temp.next = new_node

    def remove_from_head(self):
        if(not self.head): return

        newHead = self.head.next
        self.head = newHead
        
        self.count -= 1

    def remove_from_middle(self, target_key):

        if(not(self.head)): return

        temp = self.head
        target_node = None

        while(temp.next):
            if(temp.next.key == target_key):
                target_node = temp.next
                break
            temp = temp.next

        if(not(target_node)): return

        temp.next = target_node.next

        self.count -= 1

    def remove_from_end(self):
        if(not self.head): return
        if(not self.head.next):
            self.head = None
            return

        second_last = self.head
        while(second_last.next.next):
            second_last = second_last.next

        second_last.next = None

        self.count -= 1

    def is_empty(self):
        return True if self.count == 0 else False
    
    def __str__(self):
        if(not(self.head)):
            return "Linked list is empty"
        
        temp = self.head
        output_list = []
        while(temp):
            output_list.append(str(temp))
            temp = temp.next

        return " -> ".join(output_list)


    