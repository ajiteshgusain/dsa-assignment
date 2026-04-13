import time
import random
import sys

from unit3_sorts import insertion_sort, merge_sort, quick_sort, heap_sort

# Set a high recursion limit for Quick Sort on sorted/reverse data 
sys.setrecursionlimit(20000)

def run_required_tests():
    """Implementation of Required Test Cases T1-T4 [cite: 111-122]."""
    print("="*40)
    print("MANDATORY TEST EVIDENCE (T1-T4)")
    print("="*40)

    # T1. Correctness on duplicates 
    dup_list = [5, 1, 3, 3, 2, 5, 0]
    print(f"T1. Duplicates: {dup_list} -> {merge_sort(list(dup_list))}")

    # T2. Correctness on negatives 
    neg_list = [-2, 5, -1, 0, -2, 3]
    print(f"T2. Negatives:  {neg_list} -> {merge_sort(list(neg_list))}")

    # T3. Edge cases 
    print(f"T3. Edge Cases:")
    print(f"   - Empty list: [] -> {merge_sort([])}")
    print(f"   - Single element: [7] -> {merge_sort([7])}")
    print(f"   - Already sorted: [1,2,3,4,5] -> {merge_sort([1,2,3,4,5])}")
    print(f"   - Reverse sorted: [5,4,3,2,1] -> {merge_sort([5,4,3,2,1])}")

    # T4. Stability test (Mandatory) 
    P = [(2, "A"), (1, "X"), (2, "B"), (2, "C"), (1, "Y")]
    print(f"\nT4. Stability Test (Input P): {P}")
    print(f"   - Insertion Sort (Stable): {insertion_sort(list(P))}")
    print(f"   - Quick Sort (Unstable):  {quick_sort(list(P))}")
    print("="*40 + "\n")

def perform_benchmarking():
    """Task 6: Performance Report Generation ]."""
    print("="*40)
    print("TASK 6: BENCHMARKING RESULTS")
    print("="*40)
    
    sizes = [1000, 5000, 10000] #
    algos = [
        ("Insertion", insertion_sort),
        ("Merge", merge_sort),
        ("Quick", quick_sort),
        ("Heap", heap_sort)
    ]
    
    # Header for the results table 
    print(f"{'Algorithm':<12} | {'Input Type':<10} | {'n=1000':<10} | {'n=5000':<10} | {'n=10000':<10}")
    print("-" * 70)

    for name, func in algos:
        for dtype in ["Random", "Sorted", "Reverse"]: # 
            row_times = []
            for n in sizes:
                # Generate datasets per instructions 
                if dtype == "Random": data = [random.randint(0, n) for _ in range(n)]
                elif dtype == "Sorted": data = list(range(n))
                else: data = list(range(n, 0, -1))
                
                # Measure time (average of 3 runs) 
                run_times = []
                for _ in range(3):
                    data_copy = list(data)
                    start = time.perf_counter()
                    func(data_copy)
                    run_times.append(time.perf_counter() - start)
                
                avg_time = sum(run_times) / len(run_times)
                row_times.append(f"{avg_time:.4f}s")
            
            print(f"{name:<12} | {dtype:<10} | {row_times[0]:<10} | {row_times[1]:<10} | {row_times[2]:<10}")

if __name__ == "__main__":
    run_required_tests()
    perform_benchmarking()