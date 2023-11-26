#wypisz liczby z pliku, którego nazwę poda UŻ
filename = input('Podaj nazwę pliku: ')
file = open(filename, 'r')

for line in file:
    if line.strip().isdecimal():
        print(line.strip())