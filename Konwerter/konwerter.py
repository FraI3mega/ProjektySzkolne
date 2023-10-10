''' Konwerter systemów liczbowych
    DEC <-> do HEX
    FraI3mega @ 2023
'''

toDecL = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}

base = 0
char_table = '0123456789ABCDEF'

def toAlien(input,podstawa):
    """Zamienia liczbę z systemu dziesiętnego na obcy

    Args:
        input (int): Liczba która ma być zamieniona na system obcy
        podstawa (int): podstawa
    """
    cur = input
    result = ''
    if base != 1:
        # Gdy podstawa systemu nie jest cyfrą jeden
        while cur > 0:
            result += char_table[cur % base]
            cur = cur // podstawa
    else:
        # Gdy podstawa jest cyfrą jeden dodaj do wyniki tyle jedynek jaką ma wartość wejściowa
        while cur > 0:
            result += '1'
            cur -= 1
    return result[::-1]

def toDec(input,podstawa):
    """Zamienia liczbę z systemu obcego na dzisiętny

    Args:
        input (string): Liczba która ma być zamieniona
        podstawa (int): podstawa
    """

    result = 0
    for x in str(input):
        result = result * podstawa + toDecL[x.upper()]
    return result

#Głowna pętla programu

print('''Konwerter systemów liczbowych
    DEC <-> do HEX
    FraI3mega@2023\n''')

while True:
    if base == 0:
        base = int(input('Podaj podstawę sytemu: '))
    
    sel = int(input('Wybierz operację: \n1. Z systemu obcego na sytem dziesiętny \n2. Z systemu dziesiętnego na system obcy \n3. Zmień podstawę systemu\n4. Wyjdź z programu\n> '))

    if sel == 1:
        alien = str(input('Podaj liczbę w sytemie obcym: '))
        print('Wynik: ' + str(toDec(alien,base)) + "\n")

    elif sel == 2:
        dec = int(input('Podaj liczbę w sytemie dziesiętnym: '))
        print('Wynik: ' + toAlien(dec,base) + "\n")
    
    elif sel == 3:
        base = int(input('Podaj podstawę sytemu: '))
    
    elif sel == 4:
        break

    else:
        print('Błedny wybór\n')