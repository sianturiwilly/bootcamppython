# Pertemuan 3 Bootcamp Python
# Tanggal: 24 Maret 2022

# mystr = "juaracoding!"
# print("mystr = ", mystr)
# print(mystr[1:5])
# print(mystr[5:2])
# print(mystr[5:11])
# print(mystr[5:0])
# print(mystr[5:-2])
# print(mystr[5:-3])

# txt = "hello, and welcome to my world."
# print(txt.capitalize())
# print(txt.title())
# print(txt.upper())

from tabnanny import check


txt = "    banana   "
print(txt.strip())

txt2 = ",,,,rrttgg....banana...rrr"
x = txt2.strip("rtg.,")

txt3 = '###semangka,,$$$'

txt4 = "I love apples, apple678 apple are my favorite fruit"
x = txt4.count("apple")
print(x)

txt5 = "Muhammad Radja Brojas"
txt6 = "Muhammad Reja Maulana"
check = "Muhammad"

x = txt6.startswith(check)
print(x)

x = txt6.endswith("Brojas")

x = txt6.replace("Reja", "Raja")\
    .replace("Maulana", "Santi")\
    .replace("Muhammad", "Brojas")

print(x)