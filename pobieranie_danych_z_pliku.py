def wczytanie_danych_z_pliku():
    lista_notowan = []
    sciezka_do_pliku = "creotech.csv"
    with open(sciezka_do_pliku, newline="") as plik_csv:
        notowania_historyczne = csv.reader(plik_csv)
        print(notowania_historyczne)
        for index, notowanie in enumerate(lista_notowan):
            lista_notowan.append(notowanie[4])
        print(lista_notowan)
