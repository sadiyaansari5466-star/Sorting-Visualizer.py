import time

def print_array(arr):
    print(arr)
    time.sleep(0.5)


# -------- Bubble Sort --------
def bubble_sort(arr):
    n = len(arr)
    print("\nBubble Sort:")
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print_array(arr)


# -------- Merge Sort --------
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            print_array(arr)

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            print_array(arr)

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            print_array(arr)


# -------- Quick Sort --------
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        print_array(arr)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Run
data = [5, 3, 8, 4, 2]

bubble_sort(data.copy())
merge_sort(data.copy())
quick_sort(data.copy(), 0, len(data) - 1)