def fib(n: int) -> int:
    if n == 1 or n == 2:
        return n - 1
    res = fib(n - 1) + fib(n - 2)
    return res

def fib_tail(n, a, b): #a: n = 1, b: n = 2
    if n == 1:
        return a
    if n == 2:
        return b
    print(f"n-1:{n-1}, {a}, {b}")
    return fib_tail(n - 1, b, a+b)


if __name__ == "__main__":
    n = 7
    result = fib(n)
    print(result)

    result = fib_tail(n, 0, 1)
    print(result)