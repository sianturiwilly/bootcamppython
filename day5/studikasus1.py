# Program Peminjaman Kendaraan

from datetime import datetime, timedelta

sekarang = datetime.now()

print("Aplikasi Peminjaman Motor")
print("Hari Ini Tanggal:", sekarang.strftime("%d %B %Y"))

durasi = input("Masukkan Durasi Pinjaman Dalam Hari: ")
jatuh_tempo = sekarang + timedelta(days=int(durasi))

print("Data berhasil disimpan.")
print("Anda dapat meminjam kendaraan sampai tanggal:", jatuh_tempo.strftime("%d %B %Y"))