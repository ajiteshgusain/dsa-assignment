# unit1_analysis_demo.py
from unit1_recursion import factorial, fib_memo, hanoi, binary_search_rec

print("--- T1: Factorial ---")
print(f"Input: 0 | Expected: 1   | Output: {factorial(0)}")
print(f"Input: 5 | Expected: 120 | Output: {factorial(5)}\n")

print("--- T2: Fibonacci ---")
print(f"Input: 0  | Expected: 0  | Output: {fib_memo(0)}")
print(f"Input: 1  | Expected: 1  | Output: {fib_memo(1)}")
print(f"Input: 10 | Expected: 55 | Output: {fib_memo(10)}\n")

print("--- T3: Tower of Hanoi (n=3) ---")
hanoi(3, 'A', 'B', 'C')
print("")

print("--- T4: Binary Search ---")
arr = [1, 3, 5, 7, 9, 11]
print(f"Target 7 | Expected Index: 3 | Output: {binary_search_rec(arr, 7, 0, len(arr)-1)}")
print(f"Target 2 | Expected: -1      | Output: {binary_search_rec(arr, 2, 0, len(arr)-1)}")