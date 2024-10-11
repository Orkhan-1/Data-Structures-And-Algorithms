import time
import matplotlib.pyplot as plt


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


input_sizes = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
times = []

for size in input_sizes:
    arr = list(range(size))
    target = size - 1

    # For better accuracy measuring time over multiple runs
    total_time = 0
    for _ in range(100):
        start_time = time.time()
        binary_search(arr, target)
        end_time = time.time()
        total_time += (end_time - start_time)

    elapsed_time_ms = (total_time / 100) * 1000
    times.append(elapsed_time_ms)

plt.plot(input_sizes, times, marker='o')
plt.title("O(log n) Time Complexity")
plt.xlabel("Input Size")
plt.ylabel("Average Time (milliseconds)")
plt.xscale("linear")
plt.yscale("log")
plt.grid(True)
plt.show()
