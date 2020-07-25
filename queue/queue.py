"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
from singly_linked_list import LinkedList 
from singly_linked_list import Node  

class ArrQueue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.append(value)
        self.size += 1

    def dequeue(self):
        if self.size < 1:
            return
        self.size -= 1
        return self.storage.pop(0)
    
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size 

    def enqueue(self, value):
        new_node = Node(value)
        if self.storage.head == None:
            self.storage.head = new_node
            self.storage.tail = new_node
            self.size += 1
        else:
            self.storage.add_to_tail(value)
            self.size += 1


    def dequeue(self):
        if self.storage.head == None:
            return
        self.size -= 1
        return self.storage.remove_head()

q = Queue()
q.enqueue(3)
print(q.storage.head.value)
print(q.storage.tail.value)
q.enqueue(2)
print(q.storage.head.value)
print(q.storage.tail.value)
# print(q.dequeue())
# print(len(q))