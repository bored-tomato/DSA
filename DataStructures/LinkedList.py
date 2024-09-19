class Node:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        
    def __str__(self):
        return f"({self.key}:{self.val})"
    
class LinkedList:
    def __init__(self, head = None):
        self.count = 0
        self.head = head
        self.tail = head

    def _traverse_forward_operation(self, node):
        return node.next if node else None
    
    def _traverse_backward_operation(self, node):
        return node.prev if node else None
    
    def _traverse(self, target_key, start_node, _traverse_op_cb):
        temp = start_node
        target_node = None

        while(temp):
            if(temp.key == target_key):
                target_node = temp
                break
            temp = _traverse_op_cb(temp)

        return target_node if target_node else None
    
    def traverse_forward(self, target_key):
        return self._traverse(target_key, self.head, self._traverse_forward_operation)
    
    def traverse_backward(self, target_key):
        return self._traverse(target_key, self.tail, self._traverse_backward_operation)

    def insert_at_head(self, new_node):
        if not(self.head or self.tail):
            self.head, self.tail = new_node, new_node
        else:
            self.head.prev, new_node.next = new_node,self.head
            self.head = new_node
        self.count += 1

        return new_node

    def insert_after(self, target_key, new_node):
        target_node = self.traverse_forward(target_key)

        if not(target_node):
            return None

        if(self.tail == target_node):
            self.insert_at_end(new_node)
        else:
            new_node.prev, new_node.next = target_node, target_node.next
            target_node.next = new_node

            if new_node.next:
                new_node.next.prev = new_node

        self.count += 1
        return new_node
    
    def insert_at_end(self, new_node):
        if not(self.head or self.tail):
            self.head, self.tail = new_node, new_node
        else:
            new_node.prev = self.tail
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1
        return new_node

    def remove_from_head(self):
        removed_node = self.head
        if(self.head == self.tail):
            self.head, self.tail = None, None
        else:
            new_head = self.head.next
            new_head.prev = None
            self.head = new_head

        self.count -= 1
        return removed_node

    def remove_from_middle(self, target_key):
        target_node = self.traverse_forward(target_key)

        if not(target_node): return None
        elif target_node == self.head: self.remove_from_head()
        elif target_node == self.tail: self.remove_from_tail()
        else: target_node.prev.next, target_node.next.prev = target_node.next, target_node.prev
        
        self.count -= 1
        return target_node

    def remove_from_tail(self):
        removed_node = self.tail

        if(self.head == self.tail):
            self.head, self.tail = None, None
        else:
            new_tail = self.tail.prev
            new_tail.next = None
            self.tail = self.tail.prev

        self.count -= 1
        return removed_node

    def is_empty(self):
        return True if self.count == 0 else False
    
    def __str__(self):
        if not(self.head):
            return "Linked list is empty"
        
        temp = self.head
        output_list = []
        while(temp):
            output_list.append(str(temp))
            temp = temp.next

        return " -> ".join(output_list)