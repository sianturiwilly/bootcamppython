import requests, pprint, statistics

r = requests.get("https://data.covid19.go.id/public/api/prov.json")

# print(r.status_code)
data_covid = r.json()
print(data_covid)
print(data_covid['last_date'])
print(data_covid['current_data'])
data_wilayah = data_covid['list_data'][:5]
data_wilayah_bersih = []

# pprint.pprint(data_wilayah)

for data in data_wilayah:
    data_wilayah_bersih.append(
        [data['key'], data['jumlah_kasus'], data['jumlah_sembuh'],
         data['jumlah_meninggal'], data['jumlah_dirawat']]
    )

kolom_jumlah_kasus = []
kolom_jumlah_sembuh = []
kolom_jumlah_meninggal = []
kolom_jumlah_dirawat = []

for data in data_wilayah_bersih:
    kolom_jumlah_kasus.append(data[1])
    kolom_jumlah_sembuh.append(data[2])
    kolom_jumlah_meninggal.append(data[3])
    kolom_jumlah_dirawat.append(data[4])

# pprint.pprint(data_wilayah_bersih)
# pprint.pprint(kolom_jumlah_kasus)
# pprint.pprint(kolom_jumlah_sembuh)
# pprint.pprint(kolom_jumlah_meninggal)
# pprint.pprint(kolom_jumlah_dirawat)

print("Mean untuk kasus: ", statistics.mean(kolom_jumlah_kasus))
print("Mean untuk sembuh: ", statistics.mean(kolom_jumlah_sembuh))
print("Mean untuk meninggal: ", statistics.mean(kolom_jumlah_meninggal))