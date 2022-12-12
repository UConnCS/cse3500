def sum_unique_rows(m, n):
    below = [0] * m

    for i in range(n - 1):
        above = [0] * m
        # go backwards
        for j in range(m - 1, -1):
            above[j] = above[j + 1] + below[j]
        below = above
    
    return result