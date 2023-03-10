import math

def jump_search(lst, x):
    panjang = len(lst)
    step = int(math.sqrt(panjang))
    prev = 0
    while lst[min(step, panjang)-1] < x:
        prev = step
        step += int(math.sqrt(panjang))
        if prev >= panjang:
            return -1
    while lst[prev] < x:
        prev += 1
        if prev == min(step, panjang):
            return -1
    if lst[prev] == x:
        return prev
    return -1

def flatten(lst):
    flat_lst = []
    for item in lst:
        if isinstance(item, list):
            flat_lst.extend(flatten(item))
        else:
            flat_lst.append(item)
    return flat_lst

var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

# Mencari posisi data Arsel, Avivah, dan Daiva
cariin_arsel = jump_search(var, "Arsel")
cariin_avivah = jump_search(var, "Avivah")
cariin_daiva = jump_search(flatten(var), "Daiva")
print("1. Arsel di Index {}, Avivah di Index {}, Daiva di Index {}".format(cariin_arsel, cariin_avivah, cariin_daiva))

# Mencari posisi data Wahyu di kolom 0
cariin_wahyu = jump_search(var[3], "Wahyu")
print("2. Wahyu di Index {} pada kolom 0".format(cariin_wahyu + 3))

# Mencari posisi data Wibi di kolom 1
cariin_wibi = jump_search(var[3], "Wibi")
print("3. Wibi di Index {} pada kolom 1".format(cariin_wibi + 2))
