def fibonacci_search(arr, x, n):
    # Inisialisasi variabel awal
    n = len(arr)
    fib2 = 0   # (m-2)'th Fibonacci number
    fib1 = 1   # (m-1)'th Fibonacci number
    fib = fib2 + fib1  # m'th Fibonacci number
 
    # Fibonnaci number terbesar yang lebih kecil atau sama dengan n
    while (fib < n):
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1
 
    # indeks awal untuk pencarian linear
    offset = -1
 
    # saat masih ada elemen untuk diinspeksi
    while (fib > 1):
         
        # cek apakah fib2 cocok dengan posisi yang ingin dicari
        i = min(offset + fib2, n-1)
 
        # jika x lebih besar dari nilai di indeks i
        if (arr[i] < x):
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
 
        # jika x lebih kecil dari nilai di indeks i
        elif (arr[i] > x):
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
 
        # jika x cocok dengan nilai di indeks i
        else:
            return i
 
    # terakhir, cek elemen terakhir dengan x
    if(fib1 and arr[offset+1] == x):
        return offset+1
 
    # jika x tidak ditemukan dalam array
    return -1

# Driver Code
arr = [10, 22, 235, 35, 40, 45, 50,
	80, 82, 85, 90, 100,235]
n = len(arr)
x = 235
ind = fibonacci_search(arr, x, n)
if ind>=0:
    print("Found at index:",ind)

else:
    print(x,"isn't present in the array")
