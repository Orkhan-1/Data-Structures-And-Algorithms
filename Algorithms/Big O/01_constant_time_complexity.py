import time
import matplotlib.pyplot as plt


def access_element(arr, index):
    return arr[index]


input_sizes = [10, 100, 1000, 10000]
times = []

for size in input_sizes:
    arr = list(range(size))
    index = size // 2

    start_time = time.time()
    access_element(arr, index)
    end_time = time.time()

    elapsed_time_ms = (end_time - start_time) * 1000
    times.append(elapsed_time_ms)

plt.plot(input_sizes, times, marker='o')
plt.title("O(1) Time Complexity")
plt.xlabel("Input Size")
plt.ylabel("Time (milliseconds)")
plt.show()
