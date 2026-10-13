#heap-mini
def heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)


def min_heap_sort(arr):
    n = len(arr)


    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    result = []

    for i in range(n):
        result.append(arr[0])

        arr[0], arr[n - i - 1] = arr[n - i - 1], arr[0]

        heapify(arr, n - i - 1, 0)

    return result


arr = list(map(int, input("Enter elements: ").split()))

print("Sorted array:", min_heap_sort(arr))
