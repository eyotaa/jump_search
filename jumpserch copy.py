def jump_search(arr, x):
    """
    Searches for the element x in the given sorted array using the Jump search algorithm.
    Returns the index of the element if found, else returns -1.
    """
    n = len(arr)
    # Calculate the optimal jump size
    jump_size = int(n ** 0.5)
    
    # Find the block that contains the element x
    block_start = 0
    block_end = jump_size
    while block_end < n and arr[block_end] <= x:
        block_start = block_end
        block_end += jump_size
    
    # Linear search in the block containing x
    for i in range(block_start, min(block_end, n)):
        if arr[i] == x:
            return i
    
    # Element not found
    return -1


arr = [1, 3, 4, 7, 9, 10, 14, 16, 19, 22, 25, 28, 31, 35]
x = 16
result = jump_search(arr, x)

if result == -1:
    print("Elemen", x, "tidak ditemukan dalam array.")
else:
    print("Elemen", x, "ditemukan pada indeks", result)
