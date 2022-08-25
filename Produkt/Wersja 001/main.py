from modul_wyboru_indeksu import notowania_spolki_z_wybranych_indeksow
from modul_obserowanych_spolek import lista_obserwowanych_spolek, notowania_obserwowanych_spolki
from modul_notowan_live import notowania_live
import os

def program(opcja_wyboru_menu):
    opcja = opcja_wyboru_menu
    if opcja == "1":
        notowania_live()
    elif opcja == "2":
        notowania_obserwowanych_spolki(lista_akcji_z=lista_obserwowanych_spolek)
    elif opcja == "3":
        notowania_spolki_z_wybranych_indeksow()
    elif opcja == '4':
        print(f'Opcja: {opcja}')
    else:
        print("Zły wybór !!!!!!")
    input("\nNaciśnij ENTER aby przejść do głównego MENU !\n")

if __name__ == '__main__':
    program_pracuje = True
    while program_pracuje:
        os.system('clear')
        print(20 * "*" + "  ANALIZATOR GIEŁDOWY  " + 20 * "*" + "\n")
        wybor_menu = input("(1) - Bieżące notowanie obserwowanych spółek\n"
                           "(2) - Zbiorcze notowania obserwowanych spółek\n"
                           "(3) - Notowania akcji z wybranych indeksów\n"
                           '(4) - Analiza obserwowanych spółek\n'
                           "(Q/q) - Koniec pracy programu !!!" + "\n")
        if wybor_menu == "Q" or wybor_menu == "q":
            program_pracuje = False
        else:
            program(opcja_wyboru_menu=wybor_menu)
            os.system("clear")
    print("KONIEC PROGRAMU")
