def recu(n: int) -> int:
    if n == 1:
        return 1
    res = recu(n - 1)
    return n + res

def tail_recur(n, res):
    if n == 0:
        return res
    return tail_recur(n - 1, n + res)

def fib(n: int) -> int:
    if n == 1 or n == 2:
        return n - 1
    res = fib(n - 1) + fib(n - 2)
    return res

def for_loop_recur(n: int) -> int:
    stack = []
    res = 0
    for i in range(n, 0 , -1):
        stack.append(i)
    
    while stack:
        res += stack.pop()
    return res


if __name__ == "__main__":
    n = 5
    result = recu(n)
    print(f"recusion result: {result}")

    result = tail_recur(n, 0)
    print(f"tail recusion result: {result}")

    result = fib(5)
    print(f"Fibonacci result: {result}")

    result = for_loop_recur(n)
    print(f"using for loop simlate recursion result: {result}")