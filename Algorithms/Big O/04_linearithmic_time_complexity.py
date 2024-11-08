import time
import matplotlib.pyplot as plt


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


input_sizes = [10, 100, 1000, 2000, 3000]
times = []

for size in input_sizes:
    arr = list(range(size, 0, -1))
    total_time = 0
    for _ in range(100):
        start_time = time.time()
        merge_sort(arr)
        end_time = time.time()
        total_time += (end_time - start_time)

    elapsed_time_ms = (total_time / 5) * 1000
    times.append(elapsed_time_ms)

plt.plot(input_sizes, times, marker='o')
plt.title("O(n log n) Time Complexity - Merge Sort")
plt.xlabel("Input Size (n)")
plt.ylabel("Average Time (milliseconds)")
plt.xscale("linear")
plt.yscale("linear")
plt.grid(True)
plt.show()
