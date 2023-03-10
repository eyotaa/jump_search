from random import randint
import os

os.system("cls")

def mergesort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left_data = data[:mid]
        right_data = data[mid:]

        mergesort(left_data)
        mergesort(right_data)

        """
        i = 0 #indeks untuk array kiri 
        j = 0 #indeks untuk array kanan
        k = 0 #indeks untuk penggabungnya
        """      
         
        i=j=k=0
        
        while i < len(left_data) and j < len (right_data):
            if left_data[i] < right_data[j]:
                data[k]= left_data[i]
                i += 1
                k += 1

            else:
                data[k] = right_data[j]
                j += 1
                k += 1

        while i < len(left_data):
            data[k] = left_data[i]
            i += 1
            k += 1

        
        while j < len(right_data):
            data[k] = right_data[j]
            j += 1
            k += 1

data = [randint(0,20) for i in range(10)]
print("MERGE SORT")
print(f"sebelum : {data}")
#proses sorting
mergesort(data)
# sesudah sorting
print(f"sesudah : {data}")

def quicksort(arr):
    # Jika array kosong atau hanya memiliki satu elemen, return array tersebut
    if len(arr) <= 1:
        return arr
    
    # Pilih pivot dan pisahkan elemen yang lebih kecil dan lebih besar daripada pivot
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print(f"mid : {middle}")
    print(f"kiri: {left}")
    print(f"kanan: {right}")
    
    # Rekursif panggil quicksort pada elemen yang lebih kecil dan lebih besar
    return quicksort(left) + middle + quicksort(right)

angka = [randint(0,20) for i in range (10)]
print("\nQUICK SORT")
print('Sebelum partitioning:',angka)
hasil = quicksort(angka)
print('Setelah partitioning:',hasil)
