base = int(input('Podaj podstawę sytemu: '))
sel =  input('Wybierz operację: \n1. Z systemu obcego na sytem dziesiętny \n2. Z systemu dziesiętnego na system obcy \n')

toDecL = {
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

toAlienL = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 'A',
    '11': 'B',
    '12': 'C',
    '13': 'D',
    '14': 'E',
    '15': 'F'
}
def toAlien(input):
    cur = input
    result = ''
    if base != 1:
        # Gdy podstawa systemu nie jest cyfrą jeden
        while cur > 0:
            result += toAlienL[str(cur % base)]
            cur = cur // base
    else:
        # Gdy podstawa jest cyfrą jeden dodaj do wyniki tyle jedynek jaką ma wartość wejściowa
        while cur > 0:
            result += '1'
            cur -= 1
    print(result[::-1])

def toDec(input):
    result = 0
    for x in input:
        result = result * base + toDecL[x]
    print(result)

if sel == '1':
    alien = str(input('Podaj liczbę w sytemie obcym: '))
    toDec(alien)
else:
    dec = int(input('Podaj liczbę w sytemie dziesiętnym: '))
    toAlien(dec)