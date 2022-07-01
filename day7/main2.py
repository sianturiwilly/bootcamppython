data = range(1, 101)

i = 0

while i < len(data):
    i += 1
    if data[i] % 2 == 0:
        break
    print(data[i])