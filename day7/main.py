# Bootcamp Python Pertemuan 7

# import time

# data_produk = [
#     ["A", 20000, 3, 1],
#     ["B", 25000, 12, 3]
# ]

# harga_ongkir = 500
# harga_total = 0

# for produk in data_produk:
#     harga_total += (produk[1] * produk[2] + produk[3] * harga_ongkir)

# print(harga_total)

# x, y = 24, (25, 23, 27-4)
# y=[:-1]

# if x in y:
#     print("x bagian dari y")
# elif x not in y[:-1]:
#     print("x bukan bagian dari y")
# else:
#     print("y tidak x")

# a = 0
# a, b, c = 10, 20, a
# ~(a == b)

# Program while
# i = 1
# while i <= 27:
#     if i == 2 != 0;
#         print(i)
#     i += 1

list_kota = [
    'Jakarta', 'Surabaya', 'Depok', 'Bekasi',
    'Tangerang', 'Solo', 'Jogja', 'Semarang'
]

open = True

while open:
    data = input("Masukkan kota: ")
    if data == "x":
        break
    list_kota.append(data)

print(list_kota)

# for kota in list_kota:
#     print(kota)

# i = 0
# while i < len(list_kota):
#     print(list_kota[i])
#     i += 1

# i = 0
# while i < 3:
#     print(i)
#     i += 1