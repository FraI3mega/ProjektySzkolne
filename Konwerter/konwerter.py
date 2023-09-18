import logging


base = int(input('Podaj podstawę sytemu: '))
sel =  input('Wybierz operację: \n1. Z systemu obcego na sytem dziesiętny \n2. Z systemu dziesiętnego na system obcy \n')

def toAlien(input):
    #FIXME: system jedynkowy
    cur = input
    result = ''
    while cur > 0:
        result += str(cur % base)
        cur = cur // base
    print(result[::-1])

def toDec(input):
    #TODO: Zrobić to
    print('test')

if sel == 1:
    alien = str(input('Podaj liczbę w sytemie obcym: '))
else:
    dec = int(input('Podaj liczbę w sytemie dziesiętnym: '))
    toAlien(dec)




