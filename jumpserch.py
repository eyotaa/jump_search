def jump_search(arr, x):
    n = len(arr)
    jump = int(n ** 0.5)
    left, right = 0, 0
    
    # Menentukan blok tempat elemen mungkin berada
    while right < n and arr[right] < x:
        left = right
        right += jump
        
    # Melakukan pencarian linear dalam blok yang ditentukan
    for i in range(left, min(right+1, n)):
        if arr[i] == x:
            return i
        
    return -1  # Jika elemen tidak ditemukan dalam array
    
arr = [1, 3, 4, 7, 9, 10, 14, 16, 19, 22, 25, 28, 31, 35]
x = 16
result = jump_search(arr, x)

if result == -1:
    print("Elemen", x, "tidak ditemukan dalam array.")
else:
    print("Elemen", x, "ditemukan pada indeks", result)
