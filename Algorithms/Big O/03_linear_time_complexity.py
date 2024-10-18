import time
import matplotlib.pyplot as plt


# O(n) Example
def linear_search(arr, target):
    for item in arr:
        if item == target:
            return True
    return False


input_sizes = [10, 100, 1000, 10000, 100000]
times = []

for size in input_sizes:
    arr = list(range(size))
    target = size - 1

    start_time = time.time()
    linear_search(arr, target)
    end_time = time.time()

    # Convert time to milliseconds
    elapsed_time_ms = (end_time - start_time) * 1000
    times.append(elapsed_time_ms)

# Plot the graph
plt.plot(input_sizes, times, marker='x')
plt.title("O(n) Time Complexity")
plt.xlabel("Input Size")
plt.ylabel("Time (milliseconds)")
plt.show()
