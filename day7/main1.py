# Program input hobi

list_hobi = [
    'Sepakbola', 'Mendengarkan Musik', 'Jogging',
]

open = True

while open:
    data = input("Masukkan Hobi: ")
    if len(list_hobi) >= 4:
        break
    else:
        list_hobi.append(data)

print(list_hobi)                                          