#Z pliku dane_c.txt wypisz liczby większe od 499_999
#no, pora wklepać kod poniżej:

plik = open('dane_c.txt', "r")

for line in plik:
    if int(line) > 499999:
        print(line.strip())