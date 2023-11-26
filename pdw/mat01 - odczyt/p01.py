#odczyt z pliku. plik musi najpierw istnieć
#parametr 'r' oznacza read
plik = open('dane_a.txt', 'r')
#odczytać można na kilka sposobów
#będziemy traktować plik jak zestaw linii tekstu
#użyjemy for-a do przejścia po liniach
for linia in plik:
    print(linia)
#zwróć uwagę na podwójne (puste) linie