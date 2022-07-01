# try:
#     p = int(input("masukkan angka 1 = "))
#     l = int(input("masukkan angka 2 = "))

#     luas = p * l
#     print(luas)
# except:
#     print("Maaf bu/pak, ini error.")

try:
    a = int(input("Masukkan a = "))
    b = int(input("Masukkan b = "))
    print(a / b)
    
except ValueError:
    print("Harus bentuk angka, kalau tidak error.")
except ZeroDivisionError:
    print("Error, karena Anda memasukkan 0 di b.")