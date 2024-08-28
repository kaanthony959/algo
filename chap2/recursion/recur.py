def recur(n: int) -> int:
    if n == 1:
        return 1
    res = recur(n - 1)
    return n + res

if __name__ == "__main__":
    result = recur(5)
    print(result)