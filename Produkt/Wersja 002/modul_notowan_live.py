from modul_obserowanych_spolek import lista_obserwowanych_spolek, notowania_obserwowanych_spolki
import time
import os

def notowania_live():
    program_pracuje = 100
    while program_pracuje > 0:
        program_pracuje -= 1
        os.system('clear')
        notowania_obserwowanych_spolki(lista_akcji_z=lista_obserwowanych_spolek)
        time.sleep(5)
