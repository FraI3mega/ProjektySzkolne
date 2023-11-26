#Z pliku dane_c.txt wypisz liczby, których cyfra
#jedności jest mniejsza od 5 (użyj modulo 10)

plik = open('dane_c.txt', "r")

for line in plik:
    if int(line) % 10 < 5:
        print(line.strip())