# Assuming your classes (DynamicArray, SinglyLinkedList, Stack, Queue) 
# are in unit2_linear_ds.py
from unit2_linear_ds import DynamicArray, SinglyLinkedList, Stack, Queue

def run_tests():
    # T1: DynamicArray
    print("--- T1: DynamicArray ---")
    da = DynamicArray()
    for i in range(1, 6):
        da.append(i)
        print(f"Appended {i}: Size={da.size()}, Capacity={da.capacity()}")
    da.pop()
    da.pop()
    print("After popping twice:", [da.get(i) for i in range(da.size())])
    # Note: insert/delete methods implemented in DynamicArray as per Task 3.1
    
    # T2: Singly Linked List
    print("\n--- T2: Singly Linked List ---")
    sll = SinglyLinkedList()
    for x in [3, 2, 1]: sll.insert_at_beginning(x)
    for x in [4, 5]: sll.insert_at_end(x)
    print("Traverse:", sll.traverse()) # Expected: [1, 2, 3, 4, 5]
    sll.delete_by_value(3)
    print("After deleting 3:", sll.traverse()) # Expected: [1, 2, 4, 5]
    print("Search 4:", sll.search(4)) # Expected: True
    print("Search 100:", sll.search(100)) # Expected: False

    # T3: Stack
    print("\n--- T3: Stack ---")
    st = Stack()
    for x in [10, 20, 30]: st.push(x)
    print("Peek:", st.peek()) # Expected: 30
    st.pop(); st.pop()
    print("Peek after popping twice:", st.peek()) # Expected: 10

    # T4: Queue
    print("\n--- T4: Queue ---")
    q = Queue()
    for x in [7, 8, 9]: q.enqueue(x)
    print("Front:", q.front()) # Expected: 7
    q.dequeue(); q.dequeue()
    print("Front after dequeuing twice:", q.front()) # Expected: 9

    # T5: Parentheses Checker (Implement this in unit2_linear_ds.py)
    print("\n--- T5: Parentheses Checker ---")
    def is_balanced(s):
        stack = Stack()
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in "({[":
                stack.push(char)
            elif char in mapping:
                top = stack.pop()
                if top != mapping[char]: return False
        return stack.is_empty()

    for test in ["([])", "([)]", "(((", ""]:
        print(f"'{test}': {is_balanced(test)}")

if __name__ == "__main__":
    run_tests()