def for_loop(n: int) -> int:
    result = 0
    for i in range(1, n + 1):
        result += i
        print(f"i={i}, result={result}")
    return result

if __name__ == "__main__":
    n = 5
    result = for_loop(n)
    print(result)