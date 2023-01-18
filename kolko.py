import time
import random
import os
import sys


def main():
    wizualizacja()
    z = kto_zaczyna()
    board(z)


# program mówi o zasadach
def wizualizacja():
    print('Witaj w grze "Kółko i krzyżyk"', end="\n")
    time.sleep(1)
    tablica = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
    for i in tablica:
        print(tablica[i], end="")
        if i % 3 == 0 and i != 9:
            print()
            print("======")
        if i % 3 != 0:
            print("|", end="")
    print(end="\n")
    while True:
        print("\033[1;36mCzy znasz zasady?\033[0m")
        odpowiedz = input("Wpisz Tak/Nie   ").lower()
        if odpowiedz == "nie":
            samouczek()
        elif odpowiedz == "tak":
            return odpowiedz
        else:
            pass


def samouczek():
    print("Serio? xd")
    time.sleep(1)
    while True:
        zapytanie1 = input("tak/nie\n").lower()
        if zapytanie1 == "tak" or zapytanie1 == "nie":
            break
    if zapytanie1 == "tak":
        print("Heh", end="\n")
        print("No ok, więc zaczniemy od najważniejszego!\nCzyli od tego jak wygrywać")
        time.sleep(1)
        while True:
            print(
                "Aby wygrać należy postawić trzy takie same zanki w jednej linii. O to przykład:"
            )
            time.sleep(1)
            tablica = {
                1: "\033[0;33mx\033[0m",
                2: "\033[0;33mx\033[0m",
                3: "\033[0;33mx\033[0m",
                4: " ",
                5: " ",
                6: " ",
                7: " ",
                8: " ",
                9: " ",
            }
            for i in tablica:
                print(tablica[i], end="")
                if i % 3 == 0 and i != 9:
                    print()
                    print("======")
                if i % 3 != 0:
                    print("|", end="")
            print(end="\n")
            time.sleep(1)
            print("x wygrywa ponieważ zajmuje czały pierwszy rząd")
            time.sleep(1)
            print("Proste prawda?")
            time.sleep(1)

            print("Kolejny przykład, tym razem po przekątnych")
            time.sleep(1)
            tablica = {
                1: " ",
                2: " ",
                3: "\033[0;33mx\033[0m",
                4: " ",
                5: "\033[0;33mx\033[0m",
                6: " ",
                7: "\033[0;33mx\033[0m",
                8: " ",
                9: " ",
            }
            for i in tablica:
                print(tablica[i], end="")
                if i % 3 == 0 and i != 9:
                    print()
                    print("======")
                if i % 3 != 0:
                    print("|", end="")
            print(end="\n")
            time.sleep(1)
            print("Oraz przykład na kolumnie")
            time.sleep(1)
            tablica = {
                1: " ",
                2: "\033[0;33mx\033[0m",
                3: " ",
                4: " ",
                5: "\033[0;33mx\033[0m",
                6: " ",
                7: " ",
                8: "\033[0;33mx\033[0m",
                9: " ",
            }
            for i in tablica:
                print(tablica[i], end="")
                if i % 3 == 0 and i != 9:
                    print()
                    print("======")
                if i % 3 != 0:
                    print("|", end="")
            print(end="\n")
            print("Chcesz abym powtórzył jak wgrywać?")
            while True:
                wygrana = input("Tak/Nie\n").lower()
                if wygrana =="nie" or wygrana == "tak":
                    break
            if wygrana == "tak":
                pass
            elif wygrana == "nie":
                break
        print("To teraz krótki informator o tym jak się poruszac")
        time.sleep(0.5)
        print("Każde pole WOLNE pole oznaczone jest za pomocą liczby z przedziału <1,9>")
        time.sleep(0.5)
        tablica = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
        print("tak jak pokazano poniżej")
        for i in tablica:
            print(tablica[i], end="")
            if i % 3 == 0 and i != 9:
                print()
                print("======")
            if i % 3 != 0:
                print("|", end="")
        print(end="\n")
        print("Aby wybrać pole należy wpisać w terminalu interesującą nas cyfrę")
        time.sleep(1)
        print("Teraz wszytko zależy od Ciebie! :)")
        time.sleep(2)
    elif zapytanie1 == "tak":
        return 0


def kto_zaczyna():
    while True:
        try:
            rozpoczecie = input(
                '\nJesli chcesz zacząc wpisz "Ja", jesli chcesz byc drugi wpisz "Komp"\n'
            ).lower()
            if rozpoczecie == "ja":
                return 1
            elif rozpoczecie == "komp":
                return 0
            else:
                ValueError
        except:
            pass


# wypisanie tablicy na ekranie
def board(z):
    j = 0

    tablica = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
    
    if z == 1:
        while j < 5:
            kordy = game(tablica)
            tablica[kordy] = "\033[0;33mx\033[0m"
            wygrana = czy_wygrana(tablica)
            if wygrana != False:
                for i in tablica:
                    print(tablica[i], end="")
                    if i % 3 == 0 and i != 9:
                        print()
                        print("======")
                    if i % 3 != 0:
                        print("|", end="")
                sys.exit(wygrana)
            if j < 4:
                kordy_komp = komp(tablica)
                tablica[kordy_komp] = "\033[0;34mo\033[0m"
                wygrana = czy_wygrana(tablica)
                if wygrana != False:
                    for i in tablica:
                        print(tablica[i], end="")
                        if i % 3 == 0 and i != 9:
                            print()
                            print("======")
                        if i % 3 != 0:
                            print("|", end="")
                    sys.exit(wygrana)
            for i in tablica:
                print(tablica[i], end="")
                if (i % 3 == 0) and (i < 7):
                    print()
                    print("======")
                if i % 3 != 0:
                    print("|", end="")

            j += 1
        print("\n\033[0;31mRemis!\033[0m")

    elif z == 0:
        while j < 5:
            kordy_komp = komp(tablica)
            tablica[kordy_komp] = "\033[0;34mo\033[0m"
            wygrana = czy_wygrana(tablica)
            if wygrana != False:
                for i in tablica:
                    print(tablica[i], end="")
                    if i % 3 == 0 and i != 9:
                        print()
                        print("======")
                    if i % 3 != 0:
                        print("|", end="")
                sys.exit(wygrana)
            for i in tablica:
                print(tablica[i], end="")
                if i % 3 == 0 and i != 9:
                    print()
                    print("======")
                if i % 3 != 0:
                    print("|", end="")
            if j < 4:
                wygrana = czy_wygrana(tablica)
                kordy = game(tablica)
                tablica[kordy] = "\033[0;33mx\033[0m"
                if wygrana != False:
                    for i in tablica:
                        print(tablica[i], end="")
                        if i % 3 == 0 and i != 9:
                            print()
                            print("======")
                        if i % 3 != 0:
                            print("|", end="")
                    sys.exit(wygrana)

            j += 1
        print("\n\033[0;31mRemis!\033[0m")


# program pobiera dane od uzytkownika
def game(t):
    while True:
        dane = input("\nJakie pole wybierasz?\n")
        os.system("cls")
        try:
            dane = int(dane)
            if dane >= 1 and dane <= 9 and t[dane] != "\033[0;33mx\033[0m" and t[dane] != "\033[0;34mo\033[0m":
                return dane
        except:
            print("Złe dane wejsciowe")


# komputer losuje swoje posuniecie
def komp(t):
    # 1.szukaj wygranej
    i = 1
    while i < 4:
        # po kolumnach

        if t[i] == "\033[0;34mo\033[0m" and t[i + 3] == "\033[0;34mo\033[0m" and t[i + 6] != "\033[0;33mx\033[0m" and t[i + 6] != "\033[0;34mo\033[0m":
            return i + 6
        elif t[i + 3] == t[i + 6] and t[i + 3] == "\033[0;34mo\033[0m" and t[i] != "\033[0;33mx\033[0m" and t[i] != "\033[0;34mo\033[0m":
            return i
        elif t[i] == "\033[0;34mo\033[0m" and t[i + 6] == "\033[0;34mo\033[0m" and t[i + 3] != "\033[0;33mx\033[0m" and t[i + 3] != "\033[0;34mo\033[0m":
            return i + 3
        i += 1
    i = 1
    while i < 8:

        # po rzedach
        if t[i] == "\033[0;34mo\033[0m" and t[i + 1] == "\033[0;34mo\033[0m" and t[i + 2] != "\033[0;33mx\033[0m" and t[i + 2] != "\033[0;34mo\033[0m":
            return i + 2
        elif t[i + 1] == t[i + 2] and t[i + 1] == "\033[0;34mo\033[0m" and t[i] != "\033[0;33mx\033[0m" and t[i] != "\033[0;34mo\033[0m":
            return i
        elif t[i] == "\033[0;34mo\033[0m" and t[i + 2] == "\033[0;34mo\033[0m" and t[i + 1] != "\033[0;33mx\033[0m" and t[i + 1] != "\033[0;34mo\033[0m":
            return i + 1
        i += 3
    # po przekatnych
    if t[1] == "\033[0;34mo\033[0m" and t[9] == "\033[0;34mo\033[0m" and t[5] != "\033[0;33mx\033[0m" and t[5] != "\033[0;34mo\033[0m":
        return 5
    elif t[5] == "\033[0;34mo\033[0m" and t[9] == "\033[0;34mo\033[0m" and t[1] != "\033[0;33mx\033[0m" and t[1] != "\033[0;34mo\033[0m":
        return 1
    elif t[1] == "\033[0;34mo\033[0m" and t[5] == "\033[0;34mo\033[0m" and t[9] != "\033[0;33mx\033[0m" and t[9] != "\033[0;34mo\033[0m":
        return 9
    elif t[7] == "\033[0;34mo\033[0m" and t[5] == "\033[0;34mo\033[0m" and t[3] != "\033[0;33mx\033[0m" and t[3] != "\033[0;34mo\033[0m":
        return 3
    elif t[7] == "\033[0;34mo\033[0m" and t[3] == "\033[0;34mo\033[0m" and t[5] != "\033[0;33mx\033[0m" and t[5] != "\033[0;34mo\033[0m":
        return 5
    elif t[5] == "\033[0;34mo\033[0m" and t[3] == "\033[0;34mo\033[0m" and t[7] != "\033[0;33mx\033[0m" and t[7] != "\033[0;34mo\033[0m":
        return 7
    # 2.zablokuj przegraną

    i = 1
    while i < 8:
        # po rzedach
        if i < 8:
            if t[i] == "\033[0;33mx\033[0m" and t[i + 1] == "\033[0;33mx\033[0m" and t[i + 2] != "\033[0;34mo\033[0m" and t[i + 2] != "\033[0;33mx\033[0m":
                return i + 2
            elif (
                t[i + 1] == t[i + 2] and t[i + 1] == "\033[0;33mx\033[0m" and t[i] != "\033[0;34mo\033[0m" and t[i] != "\033[0;33mx\033[0m"
            ):
                return i
            elif (
                t[i] == "\033[0;33mx\033[0m" and t[i + 2] == "\033[0;33mx\033[0m" and t[i + 1] != "\033[0;34mo\033[0m" and t[i + 1] != "\033[0;33mx\033[0m"
            ):

                return i + 1
        i += 3
        # po kolumnach
    i = 1
    while i < 4:

        if t[i] == "\033[0;33mx\033[0m" and t[i + 3] == "\033[0;33mx\033[0m" and t[i + 6] != "\033[0;34mo\033[0m" and t[i + 6] != "\033[0;33mx\033[0m":
            return i + 6
        elif t[i + 3] == t[i + 6] and t[i + 3] == "\033[0;33mx\033[0m" and t[i] != "\033[0;34mo\033[0m" and t[i] != "\033[0;33mx\033[0m":
            return i
        elif t[i] == "\033[0;33mx\033[0m" and t[i + 6] == "\033[0;33mx\033[0m" and t[i + 3] != "\033[0;34mo\033[0m" and t[i + 3] != "\033[0;33mx\033[0m":
            return i + 3
        i += 1
    # po przekatnych
    if t[1] == "\033[0;33mx\033[0m" and t[9] == "\033[0;33mx\033[0m" and t[5] != "\033[0;34mo\033[0m" and t[5] != "\033[0;33mx\033[0m":
        return 5
    elif t[5] == "\033[0;33mx\033[0m" and t[9] == "\033[0;33mx\033[0m" and t[1] != "\033[0;34mo\033[0m" and t[1] != "\033[0;33mx\033[0m":
        return 1
    elif t[1] == "\033[0;33mx\033[0m" and t[5] == "\033[0;33mx\033[0m" and t[9] != "\033[0;34mo\033[0m" and t[9] != "\033[0;33mx\033[0m":
        return 9
    elif t[7] == "\033[0;33mx\033[0m" and t[5] == "\033[0;33mx\033[0m" and t[3] != "\033[0;34mo\033[0m" and t[3] != "\033[0;33mx\033[0m":
        return 3
    elif t[7] == "\033[0;33mx\033[0m" and t[3] == "\033[0;33mx\033[0m" and t[5] != "\033[0;34mo\033[0m" and t[5] != "\033[0;33mx\033[0m":
        return 5
    elif t[5] == "\033[0;33mx\033[0m" and t[3] == "\033[0;33mx\033[0m" and t[7] != "\033[0;34mo\033[0m" and t[7] != "\033[0;33mx\033[0m":
        return 7
    # 3.szukaj przeciecia
    j = 1
    i = 1
    while j < 4 and i < 4:
        if (
            (t[j] != "\033[0;33mx\033[0m" and t[j + 1] != "\033[0;33mx\033[0m" and t[j + 2] != "\033[0;33mx\033[0m")
            and (t[i] != "\033[0;33mx\033[0m" and t[i + 3] != "\033[0;33mx\033[0m" and t[i + 6] != "\033[0;33mx\033[0m")
            and (t[j] == "\033[0;34mo\033[0m" or t[j + 1] == "\033[0;34mo\033[0m" or t[j + 2] == "\033[0;34mo\033[0m")
            and (t[i] == "\033[0;34mo\033[0m" or t[i + 3] == "\033[0;34mo\033[0m" or t[i + 6] == "\033[0;34mo\033[0m")
        ):
            if (
                (t[j] != "\033[0;33mx\033[0m" and t[j + 1] != "\033[0;33mx\033[0m" and t[j + 2] != "\033[0;33mx\033[0m")
                and (t[i] != "\033[0;33mx\033[0m" and t[i + 3] != "\033[0;33mx\033[0m" and t[i + 6] != "\033[0;33mx\033[0m")
                and (t[j] == "\033[0;34mo\033[0m" or t[j + 1] == "\033[0;34mo\033[0m" or t[j + 2] == "\033[0;34mo\033[0m")
                and (t[i] == "\033[0;34mo\033[0m" or t[i + 3] == "\033[0;34mo\033[0m" or t[i + 6] == "\033[0;34mo\033[0m")
            ):

                if (
                    (t[i] == t[j] or t[i] == t[j + 1] or t[i] == t[j + 2])
                    and t[i] != "\033[0;33mx\033[0m"
                    and t[i] != "\033[0;34mo\033[0m"
                ):
                    return i
                elif (
                    (t[i + 3] == t[j] or t[i + 3] == t[j + 1] or t[i + 3] == t[j + 2])
                    and t[i + 3] != "\033[0;33mx\033[0m"
                    and t[i + 3] != "\033[0;34mo\033[0m"
                ):
                    return i + 3
                elif (
                    (t[i + 6] == t[j] or t[i + 6] == t[j + 1] or t[i + 6] == t[j + 2])
                    and t[i + 6] != "\033[0;33mx\033[0m"
                    and t[i + 6] != "\033[0;34mo\033[0m"
                ):
                    return i + 6

        j += 1
        i += 1

    # 4.szukaj przeciecia przeciwnika
    j = 1
    i = 1
    while j < 4 and i < 4:
        if (
            (t[j] != "\033[0;34mo\033[0m" and t[j + 1] != "\033[0;34mo\033[0m" and t[j + 2] != "\033[0;34mo\033[0m")
            and (t[i] != "\033[0;34mo\033[0m" and t[i + 3] != "\033[0;34mo\033[0m" and t[i + 6] != "\033[0;34mo\033[0m")
            and (t[j] == "\033[0;33mx\033[0m" or t[j + 1] == "\033[0;33mx\033[0m" or t[j + 2] == "\033[0;33mx\033[0m")
            and (t[i] == "\033[0;33mx\033[0m" or t[i + 3] == "\033[0;33mx\033[0m" or t[i + 6] == "\033[0;33mx\033[0m")
        ):

            if (
                (t[i] == t[j] or t[i] == t[j + 1] or t[i] == t[j + 2])
                and t[i] != "\033[0;33mx\033[0m"
                and t[i] != "\033[0;34mo\033[0m"
            ):
                return i
            elif (
                (t[i + 3] == t[j] or t[i + 3] == t[j + 1] or t[i + 3] == t[j + 2])
                and t[i + 3] != "\033[0;33mx\033[0m"
                and t[i + 3] != "\033[0;34mo\033[0m"
            ):
                return i + 3
            elif (
                (t[i + 6] == t[j] or t[i + 6] == t[j + 1] or t[i + 6] == t[j + 2])
                and t[i + 6] != "\033[0;33mx\033[0m"
                and t[i + 6] != "\033[0;34mo\033[0m"
            ):
                return i + 6

        j += 1
        i += 1
    # 5.zagraj środek
    if t[5] == "5":
        return 5
    # 6.zagraj naroznik na przeciw przeciwnika
    elif t[1] == "\033[0;33mx\033[0m":
        return 9
    elif t[3] == "\033[0;33mx\033[0m":
        return 7
    elif t[7] == "\033[0;33mx\033[0m":
        return 3
    elif t[9] == "\033[0;33mx\033[0m":
        return 1
    # 7.zagraj pusty naroznik
    elif t[1] == "1" or t[3] == "3" or t[7] == "7" or t[9] == "9":
        while True:
            wybor = [1, 3, 7, 9]
            k = random.choice(wybor)
            if t[k] != "\033[0;34mo\033[0m" and t[k] != "\033[0;33mx\033[0m":
                return k

    # 8.zagraj pusty bok
    elif t[2] == "2" or t[4] == "4" or t[8] == "8" or t[6] == "6":
        while True:
            k = random.choice([2, 4, 6, 8])
            if t[k] != "\033[0;34mo\033[0m" and t[k] != "\033[0;33mx\033[0m":
                return k


def czy_wygrana(t):
    # sprawdzenie rzedu
    i = 1
    while i < 8:
        if (t[i] == t[i + 1]) and (t[i + 1] == t[i + 2]):
            if t[i] == "\033[0;33mx\033[0m":
                return "\n\033[0;31mWygrana!\033[0m"
            else:
                return "\n\033[0;31mPrzegrana :(\033[0m"
        i += 3
    # sprawdzenie kolumny
    i = 1
    while i < 4:
        if (t[i] == t[i + 3]) and (t[i + 3] == t[i + 6]):
            if t[i] == "\033[0;33mx\033[0m":
                return "\n\033[0;31mWygrana!\033[0m"
            else:
                return "\n\033[0;31mPrzegrana :(\033[0m"
        i += 1
    # sprawdzenie przekątnych
    if t[3] == t[5] and t[5] == t[7]:
        if t[3] == "\033[0;33mx\033[0m":
            return "\n\033[0;31mWygrana!\033[0m"
        else:
            return "\n\033[0;31mPrzegrana :(\033[0m"
    elif t[9] == t[5] and t[5] == t[1]:
        if t[1] == "\033[0;33mx\033[0m":
            return "\n\033[0;31mWygrana!\033[0m"
        else:
            return "\n\033[0;31mPrzegrana :(\033[0m"

    return False


if __name__ == "__main__":
    main()
