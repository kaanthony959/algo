def for_loop(n : int) -> int:
    res = 0
    for i in range(1, n + 1):
        res += i
    return res

def while_loop(n: int) -> int:
    res = 0
    i = 1
    while i <= n:
        res += i
        i += 1
    return res

def while_loop_ii(n: int) -> int:
    res = 0
    i = 1
    while i <= n:
        res += i 
        i += 1
        i *= 2
    return res

def nested_for_loop(n: int) -> str:
    res = ""
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            res += f"{i}, {j}\n"
    return res


if __name__ == "__main__":
    n = 5
    for_loop_res = for_loop(n)
    print(f"for loop result: {for_loop_res}")

    while_loop_res = while_loop(n)
    print(f"while loop result: {while_loop_res}")

    while_loop_ii_res = while_loop_ii(n)
    print(f"while loop ii result: {while_loop_ii_res}")

    nested_for_res = nested_for_loop(n)
    print(f"nested for loop result:{nested_for_res}")