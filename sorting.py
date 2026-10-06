# bubble_sort...

# arr=[12,43,65,55,33,44,]

# n=len(arr)
# for i in range(n):
#     for j in range(0,n-i-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
# print("Bubble Sort:",arr)


#insertion sort...
arr = [64, 34, 25, 12, 22, 11, 90]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

print("Insertion Sort:", arr)


#selection sort...
arr = [64, 23,45,65,32,43,44,55]

for i in range(len(arr)):
    min_index = i

    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Selection Sort:", arr)

#merge_sort,....
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

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


arr = [64, 34, 25, 12, 55,33,12,34]

merge_sort(arr)

print("Merge Sort:", arr)

#quick_sort...
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


arr = [
    33,56,34,12, 22, 11, 90]

arr = quick_sort(arr)

print("Quick Sort:", arr)


#heap_sort....
def heapify(arr, n, i):
    largest = i

    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


arr = [62,45,76,78, 22, 11, 90]

heap_sort(arr)

print("Heap Sort:", arr)


#countin_sort..
def counting_sort(arr):
    max_value = max(arr)

    count = [0] * (max_value + 1)

    for num in arr:
        count[num] += 1

    result = []

    for i in range(len(count)):
        result += [i] * count[i]

    return result


arr = [76,56,33,44,22,12,]

arr = counting_sort(arr)

print("Counting Sort:", arr)


#radix_sort...
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


arr = [64, 34, 25, 12, 22, 11, 90]

radix_sort(arr)

print("Radix Sort:", arr)


#shell_sort....
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2


arr = [33,44,65,78,34,66,54,]

shell_sort(arr)

print("Shell Sort:", arr)