import time
import numpy as np
import matplotlib.pyplot as plt


# Floyd-Warshall Algorithm Implementation
def floyd_warshall(graph):
    n = len(graph)
    distance = np.array(graph)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance


input_sizes = [10, 15, 20, 25, 30]
times = []

for size in input_sizes:
    graph = np.random.randint(1, 10, size=(size, size))
    total_time = 0
    for _ in range(5):
        start_time = time.time()
        floyd_warshall(graph)
        end_time = time.time()
        total_time += (end_time - start_time)

    elapsed_time_ms = (total_time / 5) * 1000
    times.append(elapsed_time_ms)

# Plot the graph
plt.plot(input_sizes, times, marker='o')
plt.title("O(n³) Time Complexity - Floyd-Warshall Algorithm")
plt.xlabel("Input Size (n)")
plt.ylabel("Average Time (milliseconds)")
plt.xscale("linear")
plt.yscale("linear")
plt.grid(True)
plt.show()
