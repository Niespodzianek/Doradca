from modul_obserowanych_spolek import (lista_obserwowanych_spolek, notowania_obserwowanych_spolki)
import time
import os


def notowania_live():
    petla_notowan_live_pracuje = 1000
    while petla_notowan_live_pracuje > 0:
        petla_notowan_live_pracuje -= 1
        os.system("clear")
        notowania_obserwowanych_spolki(lista_akcji_z=lista_obserwowanych_spolek)
        time.sleep(15)
