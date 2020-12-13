def count(S, m, n):

    # If n is 0 then there is 1
    # solution (do not include any coin)
    print("S ", S, "m ", m, "n ", n)
    if (n == 0):
        print("solution ", 1)
        return 1

    # If n is less than 0 then no
    # solution exists
    if (n < 0):
        print("solution ", 0)
        return 0

    # If there are no coins and n
    # is greater than 0, then no
    # solution exist
    if (m <= 0 and n >= 1):
        print("solution ", 0)
        return 0

    # count is sum of solutions (i)
    # including S[m-1] (ii) excluding S[m-1]
    return count(S, m - 1, n) + count(S, m, n-S[m-1])


# {1, 1, 1, 1}, {1, 1, 2}, {2, 2}, {1, 3}
arr = [1, 2, 3]
m = len(arr)
print(count(arr, m, 4))
