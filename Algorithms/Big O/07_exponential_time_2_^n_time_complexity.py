import time
import matplotlib.pyplot as plt

# Recursive Fibonacci Function
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

input_sizes = [20, 21, 22, 23, 24]
times = []

for size in input_sizes:
    total_time = 0
    for _ in range(5):
        start_time = time.time()
        fibonacci(size)
        end_time = time.time()
        total_time += (end_time - start_time)

    elapsed_time_ms = (total_time / 5) * 1000
    times.append(elapsed_time_ms)

# Plot the graph
plt.plot(input_sizes, times, marker='o')
plt.title("O(2ⁿ) Time Complexity - Recursive Fibonacci")
plt.xlabel("Input Size (n)")
plt.ylabel("Average Time (milliseconds)")
plt.xscale("linear")
plt.yscale("log")
plt.grid(True)
plt.show()
