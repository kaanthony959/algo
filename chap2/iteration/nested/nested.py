def nested_for_loop(n :int) -> str:
    res = ""
    for i in range(1, n + 1):
        for j in range (1, n + 1):
            res += f"{i}, {j}\n"
    return res

if __name__ == "__main__":
    n = 5
    result = nested_for_loop(n)
    print(result)