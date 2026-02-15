import sys
import math
import time
from multiprocessing import Pool

# increase max digits for int->str conversion
sys.set_int_max_str_digits(10000000)

numbers = [50000, 60000, 55000, 45000, 70000]

def compute_factorial(n):
    return math.factorial(n)

def sequential_factorials(nums):
    results = []
    start_seq = time.time()
    for n in nums:
        print(f"Computing factorial({n}) sequentially...")
        res = compute_factorial(n)
        results.append((n, res))
    end_seq = time.time()
    return results, end_seq - start_seq

def multiprocessing_factorials(nums):
    start_mp = time.time()
    with Pool() as pool:
        results = pool.map(compute_factorial, nums)
    end_mp = time.time()
    paired = [(num, res) for num, res in zip(nums, results)]
    return paired, end_mp - start_mp

if __name__ == "__main__":
    # sequential
    seq_results, seq_time = sequential_factorials(numbers)

    # multiprocessing
    mp_results, mp_time = multiprocessing_factorials(numbers)

    print("\n--- Sequential Results ---")
    for num, res in seq_results:
        print(f"Factorial({num}) has {len(str(res))} digits")

    print("\n--- Multiprocessing Results ---")
    for num, res in mp_results:
        print(f"Factorial({num}) has {len(str(res))} digits")

    print("\n--- Timing ---")
    print(f"Sequential time      : {seq_time:.2f} seconds")
    print(f"Multiprocessing time : {mp_time:.2f} seconds")