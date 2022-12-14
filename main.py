from modul_wyboru_indeksu import notowania_spolki_z_wybranych_indeksow
from modul_obserowanych_spolek import (lista_obserwowanych_spolek, notowania_obserwowanych_spolki)
from modul_notowan_live import notowania_live
import os

def program():
    program_pracuje = True
    while program_pracuje:
        os.system("clear")
        print(20 * "*" + "  ANALIZATOR GIEŁDOWY  " + 20 * "*" + "\n")
        wybor_menu = input(
            "(1) \tBieżące notowanie obserwowanych spółek\n"
            "(2) \tZbiorcze notowania obserwowanych spółek\n"
            "(3) \tNotowania akcji z wybranych indeksów\n"
            # "(4) \tAnaliza obserwowanych spółek - funkcja aktualnie nie działa\n"
            "(Q/q) \tKoniec pracy programu !!!\n")
        if wybor_menu == "Q" or wybor_menu == "q":
            program_pracuje = False
        else:
            if wybor_menu == "1":
                notowania_live()
            elif wybor_menu == "2":
                notowania_obserwowanych_spolki(lista_akcji_z=lista_obserwowanych_spolek)
            elif wybor_menu == "3":
                notowania_spolki_z_wybranych_indeksow()
            elif wybor_menu == "4":
                print(f"Opcja: {wybor_menu}")
            else:
                print("Zły wybór !!!!!!")
            input("\nNaciśnij ENTER aby przejść do głównego MENU !\n")
            os.system("clear")
    print("KONIEC PROGRAMU")


if __name__ == "__main__":
    program()

# TODO w notowaniach live trzeba umieścić:
# TODO oferty kupna i sprzedaży,
# TODO data notowania,
# TODO notowanie poprzednie.
# TODO analiza notowań, zmienić kod modułu analizy
# TODO stworzyć moduł kalkulatora oszczędności
# TODO wczytanie danych z pliku, najpierw sprawdzajęc czy jest już plik i czy notowania w pliku są aktualne
# TODO pobranie notowania
# TODO sprawdzenie godziny i jeżeli będzie po zamknięciu sesji, wtedy program będzie pobierał notowania i zapisywał je do pliku
