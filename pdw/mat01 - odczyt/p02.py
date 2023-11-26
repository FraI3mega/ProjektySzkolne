#praca z liczbami

#parametr 'r' jest domyślny i można go pominąć
plik = open('dane_b.txt')

for linia in plik:
    #linia będzie zamieniona na typ liczbowy
    x = int(linia)
    print(x *2, x*3, x*4)

#zawartość pliku możemy traktować jakby kolejne
#dane podawane przez UŻ