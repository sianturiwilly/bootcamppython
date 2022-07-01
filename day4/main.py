# Bootcamp Python Pertemuan 4

# List
buah = ["apel", "melon", "semangka", "jambu"]
print(buah[1])

a = ["kopi", "susu", "teh"]
b = ["jus apel", "jus melon", "jus jeruk"]
c = ["es kopi", "es campur", "es teler"]

# d = [a, b, c]

d = [
    tuple(["kopi", "susu", "teh"]),
    tuple(["jus apel", "jus melon", "jus jeruk"]),
    tuple(["es kopi", "es campur", "es teler"]),
    23.4,
    "Willy"
]

print(d[1][1])
print(d[2][2])
print(d[1][2])

# Tuple
x = (1, 2, 3, 4, 3)
# print(len(d[0]))
print(len(x))
print(x.count(3))
print(len(x))

data = [1, 2, 3, 2]

data.remove(2)
data.remove(2)
print(data)

a = 3
b = 4
c = 8

a, b, c = 3, 4, 8

print(a)
print(b)
print(c)

identitas = {
    "nama": "Willi",
    "umur": 29,
    "hobi" : ["Sepakbola", "Mendengarkan Musik", "Olahraga"],
    "sosmed": {
        "facebook": "https://www.facebook.com/prajudi.william",
        "twitter": "https://twitter.com/williesianturie"
    },
    "alamat": "Bekasi",
    "email": "prajudiwilliam10@gmail.com",
    "ipk": 3.14,
    "teman": ["Darwis", "Hariston", "Akbar", "Robertus"]
}
identitas["ipk"]=3.5
print(identitas)

print(identitas["nama"])
print(identitas["umur"])
print(identitas["hobi"][1])
print(identitas["sosmed"]["twitter"])
print(identitas["hobi"][0])
print(identitas["sosmed"]["facebook"])
print(identitas["ipk"]+4)
print(identitas["teman"])
print(len(identitas["teman"]))

# x = 60
# x = int(input("Masukkan data: "))
# print(x)
# print(type(x))

# Dino mengatakan bahwa ia sudah mengerjakan PR-nya sebesar 80% dari 40 soal
# yang diberikan bu Tika. Berapa soal yang sudah dikerjakan Dino?
soal = int(input("Berapa jumlah soal yang tersedia: "))
progress = int(input("Berapa persen yang sudah dikerjakan: "))
jumlah_bagian = int((progress/100) * soal)

print(f"Jumlah soal adalah {soal}")
print(f"Sudah dikerjakan {progress}%, yaitu {jumlah_bagian} soal")
print(f"Sisanya ada {soal - jumlah_bagian} soal")