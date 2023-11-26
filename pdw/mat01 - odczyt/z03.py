# Wypisz sumę liczb z pliku dane_c.txt

sum = 0

plik = open("dane_c.txt", "r")

for line in plik:
    sum += int(line)

print(sum)
