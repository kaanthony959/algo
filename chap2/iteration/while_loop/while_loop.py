def while_loop(n: int) -> int:
    result = 0
    i = 1
    while i <= n:
        result += i
        print(f"i={i}, result={result}")
        i += 1
    return result

def while_loop_ii(n: int) -> int:
    result = 0
    i = 1
    while i <= n:
        result += i
        print(f"i={i}, result={result}")
        i += 1
        i *= 2
    return result

if __name__ == "__main__":
    n = 5
    result = while_loop(n)
    print(f"while result:{result}\n")
    result = while_loop_ii(n)
    print(f"while ii result:{result}")