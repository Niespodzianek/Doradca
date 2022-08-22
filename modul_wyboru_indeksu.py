from modul_polaczenia import polaczenienie_ze_strona_www_o_adresie
import os


def wybrany_indeks():
    tekst_strony_www = polaczenienie_ze_strona_www_o_adresie(
        url="https://www.biznesradar.pl/gielda/indeksy"
    )
    marker_start = 0
    pozycja = 0
    lista_indeksow = []
    os.system("clear")
    print(f"Notowania indeksów:\n")
    while True:
        try:
            marker_poczatku_szukania = tekst_strony_www.index(
                '<a class="s_tt ', marker_start
            )
            marker_poczatku_wycinania = tekst_strony_www.index(
                '">', marker_poczatku_szukania
            ) + len('">')
            marker_konca_wycinania = tekst_strony_www.index(
                "</a>", marker_poczatku_wycinania
            )
            indeks = tekst_strony_www[
                marker_poczatku_wycinania:marker_konca_wycinania
            ]
            marker_start = marker_konca_wycinania

            marker_poczatku_szukania = tekst_strony_www.index(
                '<span class="', marker_start
            )
            marker_poczatku_wycinania = tekst_strony_www.index(
                'ch_act">', marker_poczatku_szukania
            ) + len('ch_act">')
            marker_konca_wycinania = tekst_strony_www.index(
                "</span>", marker_poczatku_wycinania
            )
            kurs = tekst_strony_www[
                marker_poczatku_wycinania:marker_konca_wycinania
            ]
            marker_start = marker_konca_wycinania

            marker_poczatku_szukania = tekst_strony_www.index(
                'span class="', marker_start
            )
            marker_poczatku_wycinania = tekst_strony_www.index(
                'ch_prev">', marker_poczatku_szukania
            ) + len('ch_prev">')
            marker_konca_wycinania = tekst_strony_www.index(
                "</span>", marker_poczatku_wycinania
            )
            poprzedni = tekst_strony_www[
                marker_poczatku_wycinania:marker_konca_wycinania
            ]
            marker_start = marker_konca_wycinania

            marker_poczatku_szukania = tekst_strony_www.index(
                '<span class="', marker_start
            )
            marker_poczatku_wycinania = tekst_strony_www.index(
                'ch_open">', marker_poczatku_szukania
            ) + len('ch_open">')
            marker_konca_wycinania = tekst_strony_www.index(
                "</span>", marker_poczatku_wycinania
            )
            otwarcie = tekst_strony_www[
                marker_poczatku_wycinania:marker_konca_wycinania
            ]
            marker_start = marker_konca_wycinania

            marker_poczatku_szukania = tekst_strony_www.index(
                '<span class="', marker_start
            )
            marker_poczatku_wycinania = tekst_strony_www.index(
                'ch_min">', marker_poczatku_szukania
            ) + len('ch_min">')
            marker_konca_wycinania = tekst_strony_www.index(
                "</span>", marker_poczatku_wycinania
            )
            minimum = tekst_strony_www[
                marker_poczatku_wycinania:marker_konca_wycinania
            ]
            marker_start = marker_konca_wycinania

            marker_poczatku_szukania = tekst_strony_www.index(
                '<span class="', marker_start
            )
            marker_poczatku_wycinania = tekst_strony_www.index(
                'ch_max">', marker_poczatku_szukania
            ) + len('ch_max">')
            marker_konca_wycinania = tekst_strony_www.index(
                "</span>", marker_poczatku_wycinania
            )
            maksimum = tekst_strony_www[
                marker_poczatku_wycinania:marker_konca_wycinania
            ]
            marker_start = marker_konca_wycinania

            marker_poczatku_szukania = tekst_strony_www.index(
                '<span class="', marker_start
            )
            marker_poczatku_wycinania = tekst_strony_www.index(
                'ch_mc">', marker_poczatku_szukania
            ) + len('ch_mc">')
            marker_konca_wycinania = tekst_strony_www.index(
                "</span>", marker_poczatku_wycinania
            )
            obrot = tekst_strony_www[
                marker_poczatku_wycinania:marker_konca_wycinania
            ]
            marker_start = marker_konca_wycinania

            lista_indeksow.append(indeks)
            print(
                f"{pozycja + 1} - Indeks: {indeks}, kurs: {kurs}, poprzedni: {poprzedni}, otwarcie: {otwarcie},"
                f" maksymalny: {maksimum}, minimalny: {minimum}, obrót; {obrot} zł."
            )
            pozycja += 1
        except ValueError:
            return lista_indeksow


def prezentacja_skladu_wybranego_indeksu(
    sposrod_listy_z_indeksami_do_wyboru=None,
):
    if sposrod_listy_z_indeksami_do_wyboru is None:
        sposrod_listy_z_indeksami_do_wyboru = wybrany_indeks()
    lista_indeksow = sposrod_listy_z_indeksami_do_wyboru
    wybor = input(
        "\nWpisz numer obok indeksu, którego akcji notowania chcesz zobaczyć\n"
    )
    opcja = int(wybor)
    os.system("clear")
    print(f"Notowania akcji z wybranego indeksu {lista_indeksow[opcja - 1]}:\n")
    adres_url = (
        "https://www.biznesradar.pl/gielda/indeks:" + lista_indeksow[opcja - 1]
    )
    tekst_strony_www = polaczenienie_ze_strona_www_o_adresie(url=adres_url)
    marker_start = 0
    lista_akcji = []
    while True:
        try:
            marker_poczatku_szukania = tekst_strony_www.index(
                '<a class="s_tt s_tt_sname_', marker_start
            )
            marker_poczatku_wycinania = tekst_strony_www.index(
                '">', marker_poczatku_szukania
            ) + len('">')
            marker_konca_wycinania = tekst_strony_www.index(
                "</a>", marker_poczatku_wycinania
            )
            spolka = tekst_strony_www[
                marker_poczatku_wycinania:marker_konca_wycinania
            ]
            marker_start = marker_konca_wycinania

            marker_poczatku_szukania = tekst_strony_www.index(
                '<span class="', marker_start
            )
            marker_poczatku_wycinania = tekst_strony_www.index(
                'ch_act">', marker_poczatku_szukania
            ) + len('ch_act">')
            marker_konca_wycinania = tekst_strony_www.index(
                "</span>", marker_poczatku_wycinania
            )
            kurs = tekst_strony_www[
                marker_poczatku_wycinania:marker_konca_wycinania
            ]
            marker_start = marker_konca_wycinania

            marker_poczatku_szukania = tekst_strony_www.index(
                'span class="', marker_start
            )
            marker_poczatku_wycinania = tekst_strony_www.index(
                'ch_prev">', marker_poczatku_szukania
            ) + len('ch_prev">')
            marker_konca_wycinania = tekst_strony_www.index(
                "</span>", marker_poczatku_wycinania
            )
            poprzedni = tekst_strony_www[
                marker_poczatku_wycinania:marker_konca_wycinania
            ]
            marker_start = marker_konca_wycinania

            marker_poczatku_szukania = tekst_strony_www.index(
                '<span class="', marker_start
            )
            marker_poczatku_wycinania = tekst_strony_www.index(
                'ch_open">', marker_poczatku_szukania
            ) + len('ch_open">')
            marker_konca_wycinania = tekst_strony_www.index(
                "</span>", marker_poczatku_wycinania
            )
            otwarcie = tekst_strony_www[
                marker_poczatku_wycinania:marker_konca_wycinania
            ]
            marker_start = marker_konca_wycinania

            marker_poczatku_szukania = tekst_strony_www.index(
                '<span class="', marker_start
            )
            marker_poczatku_wycinania = tekst_strony_www.index(
                'ch_min">', marker_poczatku_szukania
            ) + len('ch_min">')
            marker_konca_wycinania = tekst_strony_www.index(
                "</span>", marker_poczatku_wycinania
            )
            minimum = tekst_strony_www[
                marker_poczatku_wycinania:marker_konca_wycinania
            ]
            marker_start = marker_konca_wycinania

            marker_poczatku_szukania = tekst_strony_www.index(
                '<span class="', marker_start
            )
            marker_poczatku_wycinania = tekst_strony_www.index(
                'ch_max">', marker_poczatku_szukania
            ) + len('ch_max">')
            marker_konca_wycinania = tekst_strony_www.index(
                "</span>", marker_poczatku_wycinania
            )
            maksimum = tekst_strony_www[
                marker_poczatku_wycinania:marker_konca_wycinania
            ]
            marker_start = marker_konca_wycinania

            marker_poczatku_szukania = tekst_strony_www.index(
                '<span class="', marker_start
            )
            marker_poczatku_wycinania = tekst_strony_www.index(
                'ch_vol">', marker_poczatku_szukania
            ) + len('ch_vol">')
            marker_konca_wycinania = tekst_strony_www.index(
                "</span>", marker_poczatku_wycinania
            )
            wolumen = tekst_strony_www[
                marker_poczatku_wycinania:marker_konca_wycinania
            ]
            marker_start = marker_konca_wycinania

            marker_poczatku_szukania = tekst_strony_www.index(
                '<span class="', marker_start
            )
            marker_poczatku_wycinania = tekst_strony_www.index(
                'ch_mc">', marker_poczatku_szukania
            ) + len('ch_mc">')
            marker_konca_wycinania = tekst_strony_www.index(
                "</span>", marker_poczatku_wycinania
            )
            obrot = tekst_strony_www[
                marker_poczatku_wycinania:marker_konca_wycinania
            ]
            marker_start = marker_konca_wycinania

            notowanie = (
                spolka,
                kurs,
                poprzedni,
                otwarcie,
                minimum,
                maksimum,
                wolumen,
                obrot,
            )
            lista_akcji.append(notowanie)
        except ValueError:
            return lista_akcji


def notowania_spolki_z_wybranych_indeksow():
    notowania_spolek = prezentacja_skladu_wybranego_indeksu(
        sposrod_listy_z_indeksami_do_wyboru=wybrany_indeks()
    )
    for pozycja, notowania in enumerate(notowania_spolek):
        (
            spolka,
            kurs,
            poprzedni,
            otwarcie,
            minimum,
            maksimum,
            wolumen,
            obrot,
        ) = notowania
        print(
            f"{pozycja + 1} - {spolka} - aktualny kurs: {kurs}, poprzedni: {poprzedni}, otwarcie: {otwarcie},"
            f" maksymalny: {maksimum}, minimalny: {minimum}, wolumen: {wolumen}, akcji, obrót; {obrot} zł."
        )
