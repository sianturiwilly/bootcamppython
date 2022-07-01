# Bootcamp Python Pertemuan 5
# Tanggal: 28 Maret 2022

# from datetime import date

# d = date(month=1, day=14, year=2022)
# print(d)

# d = date.today()

# ts = 1326244364
# tgl = date.fromtimestamp(ts)

# print(type(tgl))
# print(d.year)
# print(d.month)
# print(d.day)
# print(f"{d.year}/{d.month}/{d.day}")

# from datetime import date, time

# b = time(11, 34, 56)
# print(b.hour)
# print(b.minute)
# print(b.second)

# print(f"{b.hour}.{b.minute}.{b.second}")

# from datetime import datetime 

# a = datetime(2018, 11, 28)
# print(a)

# b = datetime(2017, 11, 28, 23, 55, 59)
# print(b)
# print(b.year)
# print(b.month)
# print(b.day)
# print(b.hour)
# print(b.minute)
# print(b.second)
# print(b.timestamp())

# from datetime import datetime, timedelta

# check_in = datetime(2008, 8, 18, 20, 30)
# check_out = datetime(2008, 9, 26, 11, 30, 30)

# delta = check_out - check_in
# print(delta.days * 20000)

# sekarang = datetime.now()
# kemerdekaan = datetime(sekarang.year, 8, 17)
# sisa_hari = kemerdekaan - sekarang
# print(sisa_hari)

from datetime import datetime

sekarang = datetime.now()
tgllahir = datetime(sekarang.year+1, 1, 19)
sisahari = tgllahir - sekarang
print(sisahari)

# sekarang = date.today()
# kemerdekaan = datetime(sekarang.year, 8, 17)
# sisa_hari = kemerdekaan - sekarang
# print(sisa_hari.seconds)

# sekarang = date.today()
# kemerdekaan = date(sekarang.year, 8, 17)
# sisa_hari = kemerdekaan - sekarang
# print(sisa_hari)

# willi = datetime(1993, 1, 19)
# nike = datetime(1975, 12, 27)
# print(nike > willi)

# t1 = datetime(2022, 6, 11)
# t2 = datetime(2022, 6, 10)
# print(t1 > t2)

# time_delta_1 = timedelta(days=270, hours=9, minutes=18)
# print(time_delta_1)

# from datetime import datetime, timedelta

# rentang = timedelta(hours=4, minutes=20)
# sekarang = datetime.now()
# akan_datang = sekarang - rentang
# print(akan_datang)

# from datetime import datetime

# sekarang = datetime(2022, 3, 8, 10, 29, 45)
# print(sekarang)
# print(sekarang.strftime("%A, %d %B %Y %I:%M %p"))

# Mar 28 2022 00:00:00

# date_string = "28 March, @2020"
# date_object = datetime.strptime(date_string, "%d %B, @%Y")
# print(date_object)
# print(type(date_object))

# from datetime import datetime
# import pytz

# local = datetime.now()

# tz_ny = pytz.timezone('America/New_York')
# datetime_NY = datetime.now(tz_ny)

# tz_london = pytz.timezone('Europe/London')
# datetime_london = datetime.now(tz_london)

# print(local)
# print(datetime_NY)
# print(datetime_london)

# Studi Kasus Aplikasi Peminjaman Motor