import time

with open('SJP.txt', encoding='utf-8') as plik:
    slownik = {slowo.strip().lower() for slowo in plik}

tekst = input("Wpisz dowolny tekst: ")

if ' ' in tekst:
    print("Wpisany tekst nie jest jednym wyrazem.")
    exit()

wyraz = tekst.lower()
start = time.time()

if wyraz in slownik:
    print(wyraz, "jest słowem zgodnym z SJP.")
else:
    print(wyraz, "nie jest słowem zgodnym z SJP.")

koniec = time.time()
czas = koniec - start

print(f"Czas przetwarzania:", czas, "sekund.")