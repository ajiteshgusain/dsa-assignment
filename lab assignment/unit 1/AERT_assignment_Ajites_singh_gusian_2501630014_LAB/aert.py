class ADT_Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
    def seek(self):
        return self.items
    



#PART A
# here  i have created an   instance of my stack
searching_stack = ADT_Stack()

def binary_search(arr, key, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    # TASK REQUIREMENT: Storing the mid-index in the StackADT 
    searching_stack.push(mid)
    
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, key, low, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, high)


# # test case1
# arr = [1, 3, 5, 3, 9, 11, 13,7]
# key=7
# low=0
# high=len(arr)-1

# print(binary_search(arr, key, low, high))
# print(searching_stack.seek())
# # Test case 2
# # arr = [1, 3, 5, 7, 9, 11, 13], searching for
# # key=2


#PART B
#Factorial (Recursive)
def factorial(n):
    # Reject negative inputs gracefully
    if n < 0:
        return "Error: Input must be >= 0"
    
    # Base Case: 0! = 1
    if n == 0:
        return 1
    
    # Recursive Step: n * (n-1)!
    return n * factorial(n - 1)


# Fibonacci (Two Versions)
fibo_counter=0
def fibonacci(n):
    global fibo_counter
    fibo_counter+=1
    if n <=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    

dict={}
counter_2=[]
def fib_using_dict(n):
    """Recursive Fibonacci with memoization (Linear Time)"""
    global counter_2
    counter_2+= 1  # Increment every time function is entered
    
    # Check if value is already in 'memory'
    if n in dict:
        return dict[n]
    
    # Base case
    if n <= 1:
        return n
    
    # Store result in memo before returning
    dict[n] = fib_using_dict(n - 1) + fib_using_dict(n - 2)
    return dict[n]
    

# n=int(input("enter your index for fibonacci sequence:"))
# print(f"value at index {n}:{fibonacci(n)}")

def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    
    # Move top n-1 disks from source to auxiliary
    hanoi(n - 1, source, destination, auxiliary)
    
    # Move the nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")
    
    # Move the n-1 disks from auxiliary to destination
    hanoi(n - 1, auxiliary, source, destination)

# Running for N = 3
# hanoi(3, 'A', 'B', 'C')





# testing function is testing cases for  all the cases
def tester_function():
    global fibo_counter
    global counter_2


    


    print("============================================================================================")


    print()
    print("--- PART B: Factorial Test Cases ---")
    for n in [0, 1, 5, 10]:
        print(f"Factorial({n}) = {factorial(n)}")
    print("============================================================================================")
    print("\n--- Fibonacci Test Cases ---")
    for n in [5, 10, 20, 30]: 
        # Reset counters for each test
        fibo_counter=0
        recur_fibo=fibonacci(n)
        print(f"n={n} | Result: {recur_fibo}")
        print(f"  recursive fibonacci Calls: {fibo_counter}")
    print("============================================================================================")
    print("\n---Fibonacci using meiosiation Test Cases ---")
    for n in [5, 10, 20, 30]: 
        # Reset counters for each test
        counter_2=0
        recur_meo_fibo=fib_using_dict(n)
        print(f"n={n} | Result: {recur_meo_fibo}")
        print(f"  recursive fibonacci Calls: {counter_2}")


    print("\n--- PART C (Hanoi) ---")
    hanoi(3, 'A', 'B', 'C')



    print("\n--- PART D: Binary Search Test Cases ---")
    arr = [1, 3, 5, 7, 9, 11, 13]
    for key in [7, 1, 13, 2]:
        idx = binary_search(arr, key, 0, len(arr) - 1)
        print(f"Search {key} in {arr}: Found at index {idx}")
    
    # Edge case: Empty list
    print(f"Search 5 in []: {binary_search([], 5, 0, -1)}")

print("============================================================================================")


       

print(tester_function())