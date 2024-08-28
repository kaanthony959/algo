def tail_recur(n, res):
    print(f"n={n}, res={res}")
    if n == 0:
        return res
    return tail_recur(n - 1, res + n)

if __name__ == "__main__":
    n = 5
    result = tail_recur(5, 0)
    print(result)