# Menghitung huruf vokal

text = input("Masukkan teks: ")
dict_huruf_vokal = {
    'a':0,
    'i':0,
    'u':0,
    'e':0,
    'o':0,
}

print(dict_huruf_vokal.keys())

for huruf_vokal in dict_huruf_vokal.keys():
    dict_huruf_vokal[huruf_vokal] = text.count(huruf_vokal)

print(dict_huruf_vokal)