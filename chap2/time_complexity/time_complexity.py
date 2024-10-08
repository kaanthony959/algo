def constant(n: int) -> int: #O(1)
    count = 0
    size = 100000
    for _ in range(size):
        count += 1
    return count

def linear(n: int) -> int: #O(n)
    count = 0
    for _ in range(n):
        count += 1
    return count

def array_traversal(nums: list[int]) -> int: #O(n)
    count = 0
    for num in nums:
        count += 1
    return count

def quadratic(n: int) -> int: #O(n^2)
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count

def exponential(n: int) -> int: #O(2^n)
    count = 0
    base = 1
    for _ in range(n):
        for _ in range(base):
            count += 1
        base *= 2
    return count

def exp_recur(n: int) -> int: #O(2^n)
    if n == 1:
        return 1
    return exp_recur(n - 1) + exp_recur(n - 1) + 1
    
def logarithmic(n: int) -> int: #O(log n)
    count = 0
    while n > 1:
        n = n / 2
        count += 1
    return count

def log_recur(n: int) -> int: #O(log n )
    if n <= 1:
        return 0
    return log_recur(n / 2) + 1

def linear_log_recur(n: int) -> int: #O(n log n)
    if n < 1:
        return 1
    count = linear_log_recur(n // 2) + linear_log_recur(n // 2)
    for _ in range(n):
        count += 1
    return count

def factorial_recur(n: int) -> int: #O(n!)
    if n == 0:
        return 1
    count = 0 
    for _ in range(n):
        count += factorial_recur(n - 1)
    return count


if __name__ == "__main__":
    constant_res = constant(10)
    print(f"constant result: {constant_res}")

    linear_res = linear(100000)
    print(f"linear result: {linear_res}")

    num_list = [1,2,3,4,5,6,7,8,9,10]
    arr_trav_res = array_traversal(num_list)
    print(f"array traversal result: {arr_trav_res}")

    quad_res = quadratic(10)
    print(f"quadratic result: {quad_res}")

    exp_res = exponential(10)
    print(f"exponetial result: {exp_res}")

    exp_recur_res = exp_recur(10)
    print(f"exp recur result: {exp_recur_res}")

    log_res = logarithmic(10)
    print(f"logarithmic result: {log_res}")

    log_recur_res = log_recur(10)
    print(f"log recursion result: {log_recur_res}")

    lin_log_rec_res = linear_log_recur(10)
    print(f"linear log recursion result: {lin_log_rec_res}")

    fac_recur_res = factorial_recur(10)
    print(f"factorial recursion result: {fac_recur_res}")

