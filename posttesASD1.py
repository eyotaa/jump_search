

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    print(f"kiri: {left}")
    print(f"kanan: {right}")
    print(20*("-"))
    merge_sort(left)
    merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    left = quick_sort(left)
    right = quick_sort(right)
    print(f"kiri: {left}")
    print(f"kanan: {right}")
    print(20*("-"))
    return left + [pivot] + right


def merge_quick_sort(arr):
    if len(arr) <= 5:
        return quick_sort(arr)

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_quick_sort(left)
    right = merge_quick_sort(right)
    print(f"kiri: {left}")
    print(f"kanan: {right}")
    print(20*("-"))

    return merge(left, right)


arr = [3, 2, 1, 5, 4, 7, 6, 8, 9, 0]
sorted_arr = merge_quick_sort(arr)
print(sorted_arr)