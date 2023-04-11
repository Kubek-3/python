import os
import glob

try:
    os.mkdir('zadanie1_przeniesione')
except FileExistsError:
    print("Folder 'zadanie1_przeniesione' już istnieje.")

pliki = glob.glob('zadanie1/*')

for plik in pliki:
    nazwa_pliku = os.path.basename(plik)
    pierwsza_litera = nazwa_pliku[0].upper()
    try:
        os.mkdir(f'zadanie1_przeniesione/{pierwsza_litera}')
    except FileExistsError:
        pass
    os.rename(plik, f'zadanie1_przeniesione/{pierwsza_litera}/{nazwa_pliku}')