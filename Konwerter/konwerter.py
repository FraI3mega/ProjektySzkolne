import logging


base = int(input('Podaj podstawę sytemu: '))
sel =  input('Wybierz operację: \n1. Z systemu obcego na sytem dziesiętny \n2. Z systemu dziesiętnego na system obcy \n')

def toAlien(input):
    cur = input
    result = ''
    if base != 1:
        # Gdy podstawa systemu nie jest cyfrą jeden
        while cur > 0:
            result += str(cur % base)
            cur = cur // base
    else:
        # Gdy podstawa jest cyfrą jeden dodaj do wyniki tyle jedynek jaką ma wartość wejściowa
        while cur > 0:
            result += '1'
            cur -= 1
    print(result[::-1])

def toDec(input):
    #TODO: Zrobić to
    print('TODO')

if sel == 1:
    alien = str(input('Podaj liczbę w sytemie obcym: '))
else:
    dec = int(input('Podaj liczbę w sytemie dziesiętnym: '))
    toAlien(dec)




