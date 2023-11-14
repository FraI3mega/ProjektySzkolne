""" Konwerter systemów liczbowych
    DEC <-> do HEX
    FraI3mega @ 2023
"""

base = 0
char_table = "0123456789ABCDEF"


def toAlien(input, podstawa):
    """Zamienia liczbę z systemu dziesiętnego na obcy

    Args:
        input (int): Liczba która ma być zamieniona na system obcy
        podstawa (int): podstawa
    """
    cur = input
    result = ""
    if base != 1:
        while cur > 0:  # Gdy podstawa systemu nie jest cyfrą jeden
            result += char_table[cur % base]
            cur = cur // podstawa
    else:
        while (
            cur > 0
        ):  # Gdy podstawa jest cyfrą jeden dodaj do wyniki tyle jedynek jaką ma wartość wejściowa
            result += "1"
            cur -= 1
    return result[::-1]


def toDec(input, podstawa):
    """Zamienia liczbę z systemu obcego na dzisiętny

    Args:
        input (string): Liczba która ma być zamieniona
        podstawa (int): podstawa
    """

    result = 0
    for x in input:
        result = result * podstawa + char_table.index(x.upper())
    return result


def clean(input):
    """czyści dane wejsćiowe

    Args:
        input (string): dane wejściowe

    Returns:
        string: dane wejściowe bez niepożądanych znaków
    """
    result = ""
    for i in input.upper():
        if i in char_table:
            result += i
    return result


print(
    """Konwerter systemów liczbowych
    DEC <-> do HEX
    FraI3mega@2023\n"""
)

while True:  # Głowna pętla programu
    if base == 0:
        base = int(input("Podaj podstawę sytemu: "))

    sel = int(
        input(
            "Wybierz operację: \n1. Z systemu obcego na sytem dziesiętny \n2. Z systemu dziesiętnego na system obcy \n3. Zmień podstawę systemu\n4. Wyjdź z programu\n> "
        )
    )
    if sel == 1:
        alien = clean(input("Podaj liczbę w sytemie obcym: "))
        print("Wynik: ", toDec(alien, base), "\n")

    elif sel == 2:
        dec = int(clean(input("Podaj liczbę w sytemie dziesiętnym: ")))
        print("Wynik: ", toAlien(dec, base), "\n")

    elif sel == 3:
        base = int(input("Podaj podstawę sytemu: "))

    elif sel == 4:
        break

    else:
        print("Błedny wybór\n")
