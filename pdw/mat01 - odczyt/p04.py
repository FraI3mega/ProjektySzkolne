#Z pliku dane_c.txt wypisz liczby parzyste
pp = open('dane_c.txt')
#tutaj nie ma potrzeby wczytania do listy
#idziemy po pliku i jednorazowo coś wyliczamy
for linia in pp:
    x = int(linia)
    if x % 2 == 0:
        print(x)
#jednak wczytanie najpierw do listy jest praktycznie
#zawsze dobrym pomysłem