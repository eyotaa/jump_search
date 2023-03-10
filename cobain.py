import math

# fungsi jump search, digunakan untuk mencari nilai pada daftar (list) dengan kompleksitas logaritmik
def jump_search(lst, val):
    n = len(lst)
    step = int(math.sqrt(n))  # menghitung ukuran langkah
    prev = 0  # inisiasi variabel penunjuk sebelumnya
    while lst[min(step, n)-1] < val:  # melakukan pencarian nilai hingga parameter ditemukan atau dilewati
        prev = step  # menyimpan posisi sebelumnya
        step += int(math.sqrt(n))  #menentukan titik loncatan berikutnya
        if prev >= n:   # apabila objek tidak ditemukan
            return -1 
    while lst[prev] < val:   # Melakukan pencarian terhadap data yang tepat, memberikan keluaran index terakhir yang memenuhi parameter
        prev += 1   # bergerak ke depan secara linear melalui bagian sublist saat ini
        if prev == min(step, n): #tentukan hasil keluaran jika mencapai batas penelusuran tahap.
            return -1  
    if lst[prev] == val: #tentukan hasil keluaran jika kelas berhasil dijumper
        return prev
    return -1   #final check.


# fungsi flatten() bertujuan untuk meratakan list
def flatten(lst):
    flat_lst = []   # menginisialisasi list kosong sebagai output
    for item in lst:    
         #cek setiap item, apakah adalah sublist 
        if isinstance(item, list):  
            flat_lst.extend(flatten(item))   # rekursif pemanggilan fungsi flatten()
        else:
            flat_lst.append(item)   
    return flat_lst  #mengembalikan list baru yang sudah diproses

var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

# Mencari posisi data Arsel, Avivah, dan Daiva
arsel_idx = jump_search(var, "Arsel")  # Melakukan pencarian posisi dari "Arsel" dalam var menggunakan fungsi jump_search()
avivah_idx = jump_search(var, "Avivah")  # Melakukan pencarian posisi dari "Avivah" dalam var menggunakan fungsi jump_search()
daiva_idx = jump_search(flatten(var), "Daiva") # Melakukan rata-rata pada var dan mencari posisi dari "Daiva" dalam var menggunakan fungsi jump_search()
print("1. Arsel di Index {}, Avivah di Index {}, Daiva di Index {}".format(arsel_idx, avivah_idx, daiva_idx))

# Mencari posisi data Wahyu di kolom 0
wahyu_idx = jump_search(var[3], "Wahyu")  # Melakukan pencarian dari posisi ke-0 pada var[3] untuk menemukan "Wahyu"
print("2. Wahyu di Index {} pada kolom 0".format(wahyu_idx + 3))

# Mencari posisi data Wibi di kolom 1
wibi_idx = jump_search(var[3], "Wibi")   # Melakukan pencarian dari posisi ke-1 pada var[3] untuk menemukan "Wibi"
print("3. Wibi di Index {} pada kolom 1".format(wibi_idx + 2))