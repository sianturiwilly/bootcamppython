# Program Denda Keterlambatan Pengembalian Buku

from datetime import datetime, date

data_buku = [
	["Data Science", 300, "ISBN-001"],
	["Machine Learning", 400, "ISBN-002"],
	["Neural Network", 520, "ISBN-003"],
]

sekarang = date.today()
id_buku = int(input("Masuskkan ID Buku yang Dipinjam (0-2):"))
buku = data_buku[id_buku]

print("Buku Yang Anda Pinjam:")
print(f"      - {buku[0]}")
print(f"      - Rp.{buku[1]}")
print(f"      - {buku[2]}")

print("-" * 40)

tanggal_pinjam = input("Masuskkan Tanggal Pinjaman (Ex: 2020-4-21): ")
tanggal_pinjam = datetime.strptime(tanggal_pinjam, "%Y-%m-%d").date()
sisa = tanggal_pinjam - sekarang

print(f"Pengembalian Telat {abs(sisa.days)} Hari")
print(f"Denda Sebesar Rp.{buku[1]}/Hari")
print(f"Total Denda yang Harus Dibayar Rp.{buku[1] * abs(sisa.days) }")