import time
import matplotlib.pyplot as plt


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


input_sizes = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
times = []

for size in input_sizes:
    arr = list(range(size, 0, -1))
    total_time = 0
    for _ in range(10):
        start_time = time.time()
        bubble_sort(arr)
        end_time = time.time()
        total_time += (end_time - start_time)

    elapsed_time_ms = (total_time / 10) * 1000
    times.append(elapsed_time_ms)

# Plot the graph
plt.plot(input_sizes, times, marker='o')
plt.title("O(n²) Time Complexity - Bubble Sort")
plt.xlabel("Input Size")
plt.ylabel("Average Time (milliseconds)")
plt.xscale("linear")
plt.yscale("linear")
plt.grid(True)
plt.show()
