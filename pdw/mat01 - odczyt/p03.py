#dane często warto najpierw umieścić w liście
#aby potem mieć do nich swobodny dostęp
pp = open('dane_b.txt')
dane = []
for linia in pp:
    #do listy dane dołącz
    #wynik zamiany na liczbę linii tekstu
    dane.append(int(linia))

for elem in dane:
    print(elem * 2, elem*3, elem*4)
print('--- teraz inne obliczenia na tych danych ---')
for elem in dane:
    if elem >= 30:
        print(elem)