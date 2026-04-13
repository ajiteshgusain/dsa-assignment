# #task 3
# #"======================================================================================"
class DynamicArray:


    def __init__(self):
        self._n = 0                  # Current number of elements [ 54, 60]
        self._capacity = 1           # Current storage capacity [ 54, 60]
        self.A = self._make_array(self._capacity)

    def size(self):
        return self._n               # Returns current size [ 60]

    def capacity(self):
        return self._capacity        # Returns current capacity [60]

    def _make_array(self, c):
        return [None] * c            # Creates a new list of capacity c

    def get(self, i):
        if not 0 <= i < self._n:
            return "Index out of bounds"
        return self.A[i]             # Access element at index i [ 57]

    def set(self, i, x):
        if 0 <= i < self._n:
            self.A[i] = x            # Update element at index i [cite: 57]

    def append(self, x):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)  # Double capacity if full [55]
        self.A[self._n] = x
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)      # Create larger array [55, 61]
        for k in range(self._n):
            B[k] = self.A[k]         # Copy existing elements [ 61]
        self.A = B
        self._capacity = c

    def pop(self):
        if self._n == 0:
            return "Array is empty"
        value = self.A[self._n - 1]
        self.A[self._n - 1] = None
        self._n -= 1                 # Remove from end [ 56]
        return value

#task 4
#"======================================================================================"
#task 4.1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def delete_by_value(self, x):
        curr = self.head
        if curr and curr.data == x:
            self.head = curr.next
            return
        prev = None
        while curr and curr.data != x:
            prev = curr
            curr = curr.next
        if curr: # Found the value
            prev.next = curr.next
        else: # Value not found
            print(f"Value {x} not found in the list.")

    def search(self, x):
        # Returns True if found, False otherwise
        curr = self.head
        while curr:
            if curr.data == x:
                return True
            curr = curr.next
        return False

    def traverse(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result
    
# #"======================================================================================"
# #task 4.2

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # Added for Doubly Linked List

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_after_node(self, key, x):
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        if curr:
            new_node = Node(x)
            new_node.next = curr.next
            new_node.prev = curr
            if curr.next:
                curr.next.prev = new_node
            curr.next = new_node
        else:
            print(f"Key {key} not found.")

    def delete_at_position(self, pos):
        if not self.head:
            return
        curr = self.head
        for _ in range(pos):
            if curr:
                curr = curr.next
        if curr:
            if curr.prev:
                curr.prev.next = curr.next
            else:
                self.head = curr.next
            if curr.next:
                curr.next.prev = curr.prev
        else:
            print("Position out of range.")



# #"======================================================================================"
# #task 5


class Stack:
    def __init__(self):
        self.storage = SinglyLinkedList() # Using your SinglyLinkedList

    def push(self, x):
        self.storage.insert_at_beginning(x) # O(1)

    def pop(self):
        if self.is_empty(): return None
        val = self.storage.head.data
        self.storage.head = self.storage.head.next # O(1)
        return val

    def peek(self):
        return self.storage.head.data if not self.is_empty() else None

    def is_empty(self):
        return self.storage.head is None
    

#task 5.2
class Queue:
    def __init__(self):
        self.head = None # For dequeue
        self.tail = None # For enqueue

    def enqueue(self, x):
        new_node = Node(x)
        if not self.tail:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if not self.head: return None
        val = self.head.data
        self.head = self.head.next
        if not self.head: self.tail = None
        return val

    def front(self):
        return self.head.data if self.head else None


