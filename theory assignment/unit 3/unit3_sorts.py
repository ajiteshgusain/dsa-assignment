"""task 4"""

"""
Unit 3 Sorting Algorithms Implementation
Student: Ajitesh Singh Gusain
"""

def insertion_sort(a):
    """
    Purpose: Sorts a list using the Insertion Sort algorithm.
    Time Complexity: Best: O(n), Avg: O(n^2), Worst: O(n^2)
    Extra Space: O(1) (In-place)
    Stable: Yes
    """
    arr = a[:] # Creating a copy to avoid unintended side effects
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(a):
    """
    Purpose: Divide and conquer sorting.
    Time Complexity: Best/Avg/Worst: O(n log n)
    Extra Space: O(n) (Out-of-place)
    Stable: Yes
    """
    if len(a) <= 1:
        return a
    
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    
    return _merge(left, right)

def _merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        # The <= ensures stability (maintains relative order)
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(a):
    """
    Purpose: Partition-based sorting using the last element as pivot.
    Time Complexity: Best/Avg: O(n log n), Worst: O(n^2)
    Extra Space: O(log n) (Recursive stack)
    Stable: No
    """
    if len(a) <= 1:
        return a
    
    arr = a[:]
    _quick_sort_helper(arr, 0, len(arr) - 1)
    return arr

def _quick_sort_helper(arr, low, high):
    if low < high:
        p = _partition(arr, low, high)
        _quick_sort_helper(arr, low, p - 1)
        _quick_sort_helper(arr, p + 1, high)

def _partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def heap_sort(a):
    """
    Purpose: Binary heap based sorting.
    Time Complexity: Best/Avg/Worst: O(n log n)
    Extra Space: O(1)
    Stable: No
    """
    arr = a[:]
    n = len(arr)

    # Build maxheap
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)

    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        _heapify(arr, i, 0)
    return arr

def _heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest)



# #task 5
# # Task 5: Stability Test
# P = [(2, "A"), (1, "X"), (2, "B"), (2, "C"), (1, "Y")]

# # Test with a stable sort
# print("Insertion Sort Result:", insertion_sort(P)) 

# # Test with an unstable sort
# print("Quick Sort Result:", quick_sort(P))