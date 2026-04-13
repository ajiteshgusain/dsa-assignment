# unit1_recursion.py

def factorial(n):
    """
    Computes the factorial of n recursively.
    Base Case: n == 0 or n == 1 returns 1.
    Time Complexity: O(n) - n recursive calls are made.
    Space Complexity: O(n) - due to the recursion stack.
    """
    if n < 0: return None
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fib_naive(n):
    """
    Computes the nth Fibonacci number using pure recursion.
    Base Case: n == 0 returns 0, n == 1 returns 1.
    Time Complexity: O(2^n) - exponential growth due to redundant calls.
    Space Complexity: O(n) - maximum depth of the recursion tree.
    """
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

def fib_memo(n, memo=None):
    """
    Computes the nth Fibonacci number using top-down DP (memoization).
    Base Case: n in memo returns the stored value.
    Time Complexity: O(n) - each value is calculated only once.
    Space Complexity: O(n) - to store the memo dictionary and recursion stack.
    """
    if memo is None: memo = {0: 0, 1: 1}
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

def hanoi(n, src, aux, dst):
    """
    Solves the Tower of Hanoi problem and prints moves.
    Base Case: n == 1 moves the single disk directly to dst.
    Time Complexity: O(2^n) - doubles the work with each disk.
    Space Complexity: O(n) - depth of the recursion stack.
    """
    if n == 1:
        print(f"Move disk 1 from {src} to {dst}")
        return
    hanoi(n - 1, src, dst, aux)
    print(f"Move disk {n} from {src} to {dst}")
    hanoi(n - 1, aux, src, dst)

def binary_search_rec(a, target, lo, hi):
    """
    Performs binary search on a sorted list recursively.
    Base Case: lo > hi (not found) or a[mid] == target (found).
    Time Complexity: O(log n) - the search space is halved each step.
    Space Complexity: O(log n) - stack depth is logarithmic.
    """
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if a[mid] == target:
        return mid
    elif a[mid] > target:
        return binary_search_rec(a, target, lo, mid - 1)
    else:
        return binary_search_rec(a, target, mid + 1, hi)




def factorial_iterative(n):
    """
    Computes factorial using a loop.
    Space Complexity: O(1) - only uses a few variables regardless of n.
    Recursive version uses O(n) space due to the call stack.
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result



import time

print("--- Bonus: Fibonacci Timing (n=35) ---")
n_val = 35

# Timing Naive
start = time.time()
fib_naive(n_val)
end = time.time()
naive_time = end - start
print(f"Naive Recursion Time: {naive_time:.4f} seconds")

# Timing Memoization
start = time.time()
fib_memo(n_val)
end = time.time()
memo_time = end - start
print(f"Memoization Time: {memo_time:.8f} seconds")