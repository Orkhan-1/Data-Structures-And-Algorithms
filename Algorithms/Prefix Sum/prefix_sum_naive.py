def sum_range(arr, i, j):
    total = 0
    for index in range(i, j + 1):
        total += arr[index]
    return total