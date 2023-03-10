#Import library Math digunakan untuk melakukan operasi matematika seperti sqrt (square root)
import math

#Membuat fungsi "jump_search" dengan parameter "lst" (list) dan "val" (nilai yang dicari)
def jump_search(y, x):
    #Mendapatkan panjang (jumlah anggota) dari 'lst'
    n = len(y)
    #Untuk menjalankan algoritma jump search, kita dapat memanfaatkan ukuran blok yang digunakan oleh binary search
    #Dalam hal ini, kita menggunakan nilai akar kuadrat dari panjang list untuk menentukan langkah awal pencarian
    step = int(math.sqrt(n))
    prev = 0
    #Melakukan pencarian dengan melompati beberapa elemen di setiap iterasi sampai nilai yang dicari ditemukan
    while y[min(step, n)-1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    while y[prev] < x:
        prev += 1
        if prev == min(step, n):
            return -1
    #Pengecekan apakah item yang dicari ditemukan pada indeks 'prev'
    if y[prev] == x:
        return prev
    return -1

#Fungsi 'flatten' digunakan untuk membuat 'nested list' menjadi flat (tidak lagi bersarang)
def flatten(lst):
    flat_lst = []
    for item in lst:
        if isinstance(item, list):
            flat_lst.extend(flatten(item))
        else:
            flat_lst.append(item)
    return flat_lst
var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

#List 'var' terdiri dari string dan daftar string yang terbagi lagi satu level; kemudian cari posisi pada index-item berikut:
# "Arsel", "Avivah", dan "Daiva"
arsel_idx = jump_search(var, "Arsel")
avivah_idx = jump_search(var, "Avivah")
daiva_idx = jump_search(flatten(var), "Daiva")
#Cetak hasilnya sesuai format yang ditentukan
print("1. Arsel di Index {}, Avivah di Index {}, Daiva di Index {}".format(arsel_idx, avivah_idx, daiva_idx))

#Kemudian, cari posisi dari 'Wahyu' dan 'Wibi' di dalam list kedua, yaitu pada index ke-0 dan index ke-1 secara berturut-turut 
wahyu_idx = jump_search(var[3], "Wahyu")
wibi_idx = jump_search(var[3], "Wibi")
#Cetak hasilnya sesui format yang ditentukan
print("2. Wahyu di Index {} pada kolom 0".format(wahyu_idx + 3))
print("3. Wibi di Index {} pada kolom 1".format(wibi_idx + 2)) 
