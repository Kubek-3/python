def wyswietl_plansze(plansza):
    pustaPlansza = """
 ----------------
 |  1 |  2 |  3 |
 ----------------
 |  4 |  5 |  6 |
 ----------------
 |  7 |  8 |  9 |
 ----------------
 """
    for i in range(1,10):
        if (plansza[i] == 'O' or plansza[i] == 'X'):
            pustaPlansza = pustaPlansza.replace(str(i), plansza[i])
        else:
            continue
    print(pustaPlansza)

def wprowadzenie_gracza():
    gracz1 = input("Wybierz 'X' lub 'O' ")
    while True:
        if gracz1.upper() == 'X':
            gracz2='O'
            print("Wybrales " + gracz1.upper() + ". Drugi gracz jest " + gracz2)
            return gracz1.upper(),gracz2
        elif gracz1.upper() == 'O':
            gracz2 = 'X'
            print("Wybrales " + gracz1.upper() + ". Drugi gracz jest " + gracz2)
            return gracz1.upper(),gracz2
        else:
            gracz1 = input("Wybierz 'X' lub 'O' ")

def place_marker(plansza, znak, pozycja):
    plansza[pozycja] = znak
    return plansza

def czy_wolne(plansza, pozycja):
    return plansza[pozycja] == '#'

def czy_plansza_pelna(plnsza):
    return len([x for x in plnsza if x == '#']) == 1

def spr_wygrana(plansza, znak):
    if plansza[1] == plansza[2] == plansza[3] == znak:
        return True
    if plansza[4] == plansza[5] == plansza[6] == znak:
        return True
    if plansza[7] == plansza[8] == plansza[9] == znak:
        return True
    if plansza[1] == plansza[4] == plansza[7] == znak:
        return True
    if plansza[2] == plansza[5] == plansza[8] == znak:
        return True
    if plansza[3] == plansza[6] == plansza[9] == znak:
        return True
    if plansza[1] == plansza[5] == plansza[9] == znak:
        return True
    if plansza[3] == plansza[5] == plansza[7] == znak:
        return True
    return False

def wybor_gracza(plansza):
    wybor = input("Wybierz puste miejsce z numerem1 od 1 do 9: ")
    while not czy_wolne(plansza, int(wybor)):
        wybor = input("To miejsce jest zajete wybierz inne: ")
    return wybor

def ponowna_gra():
    playAgain = input("Chcesz zagrac ponownie (T/N) ? ")
    if playAgain.upper() == 'T':
        return True
    if playAgain.upper() == 'N':
        return False

if __name__ == "__main__":
    print('Witamy w grze kolko i krzyzyk!')
    i = 1
    gracze = wprowadzenie_gracza()
    plansza = ['#'] * 10
    wyswietl_plansze(plansza)

    while True:
        graj_dalej = czy_plansza_pelna(plansza)
        while not graj_dalej:
            pozycja = wybor_gracza(plansza)
            if i % 2 == 0:
                marker = gracze[1]
            else:
                marker = gracze[0]
            place_marker(plansza, marker, int(pozycja))
            wyswietl_plansze(plansza)
            i += 1
            if spr_wygrana(plansza, marker):
                print("Wygrales!")
                break
            graj_dalej = czy_plansza_pelna(plansza)
        if not ponowna_gra():
            break
        else:
            plansza = ['#'] * 10
            wyswietl_plansze(plansza)
            wprowadzenie_gracza()
            gracze = wybor_gracza(plansza)
            i = 1
            