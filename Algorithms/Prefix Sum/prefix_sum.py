prefix_sum = None

def calculate_prefix_sum(arr):
    global prefix_sum
    prefix_sum = [0] * (len(arr) + 1)
    for k in range(1, len(arr) + 1):
        prefix_sum[k] = prefix_sum[k - 1] + arr[k - 1]

def sum_range(arr, i, j):
    global prefix_sum
    if prefix_sum is None:
        calculate_prefix_sum(arr)
    return prefix_sum[j + 1] - prefix_sum[i]
