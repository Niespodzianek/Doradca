from modul_polaczenia import polaczenienie_ze_strona_www_o_adresie
import os


def notowania_obserwowanych_spolki(lista_akcji_z):
    os.system("clear")
    print("\nNotowania wybranych spółek:")
    lista_innych_spolek = lista_akcji_z
    for spolka in lista_innych_spolek:
        tekst_ze_strony = polaczenienie_ze_strona_www_o_adresie(url=spolka)
        przeszukanie_pojedynczej_spolki_ze_strony_www(
            analizowany_tekst=tekst_ze_strony
        )


def przeszukanie_pojedynczej_spolki_ze_strony_www(analizowany_tekst):
    tekst_strony_www = analizowany_tekst
    lista_akcji = []
    marker_start = 0
    marker_poczatku_szukania = tekst_strony_www.index(
        "profile-h1-c", marker_start
    )
    marker_poczatku_wycinania = tekst_strony_www.index(
        "<h1>", marker_poczatku_szukania
    ) + len("<h1>")
    marker_konca_wycinania = tekst_strony_www.index(
        "</h1>", marker_poczatku_wycinania
    )
    spolka = tekst_strony_www[marker_poczatku_wycinania:marker_konca_wycinania]
    marker_poczatku_szukania = tekst_strony_www.index("Kurs", marker_start)
    marker_poczatku_wycinania = tekst_strony_www.index(
        'ch_act">', marker_poczatku_szukania
    ) + len('ch_act">')
    marker_konca_wycinania = tekst_strony_www.index(
        "</span>", marker_poczatku_wycinania
    )
    kurs = tekst_strony_www[marker_poczatku_wycinania:marker_konca_wycinania]
    marker_poczatku_szukania = tekst_strony_www.index("Otwarcie:", marker_start)
    marker_poczatku_wycinania = tekst_strony_www.index(
        'ch_open">', marker_poczatku_szukania
    ) + len('ch_open">')
    marker_konca_wycinania = tekst_strony_www.index(
        "</span>", marker_poczatku_wycinania
    )
    otwarcie = tekst_strony_www[
        marker_poczatku_wycinania:marker_konca_wycinania
    ]
    marker_poczatku_szukania = tekst_strony_www.index("Min:", marker_start)
    marker_poczatku_wycinania = tekst_strony_www.index(
        'ch_min">', marker_poczatku_szukania
    ) + len('ch_min">')
    marker_konca_wycinania = tekst_strony_www.index(
        "</span>", marker_poczatku_wycinania
    )
    minimum = tekst_strony_www[marker_poczatku_wycinania:marker_konca_wycinania]
    marker_poczatku_szukania = tekst_strony_www.index("Max:", marker_start)
    marker_poczatku_wycinania = tekst_strony_www.index(
        'ch_max">', marker_poczatku_szukania
    ) + len('ch_max">')
    marker_konca_wycinania = tekst_strony_www.index(
        "</span>", marker_poczatku_wycinania
    )
    maksimum = tekst_strony_www[
        marker_poczatku_wycinania:marker_konca_wycinania
    ]
    marker_poczatku_szukania = tekst_strony_www.index("Wolumen:", marker_start)
    marker_poczatku_wycinania = tekst_strony_www.index(
        'ch_vol">', marker_poczatku_szukania
    ) + len('ch_vol">')
    marker_konca_wycinania = tekst_strony_www.index(
        "</span>", marker_poczatku_wycinania
    )
    wolumen = tekst_strony_www[marker_poczatku_wycinania:marker_konca_wycinania]
    marker_poczatku_szukania = tekst_strony_www.index("Obrót:", marker_start)
    marker_poczatku_wycinania = tekst_strony_www.index(
        'ch_mc">', marker_poczatku_szukania
    ) + len('ch_mc">')
    marker_konca_wycinania = tekst_strony_www.index(
        "</span>", marker_poczatku_wycinania
    )
    obrot = tekst_strony_www[marker_poczatku_wycinania:marker_konca_wycinania]

    notowanie = (spolka, kurs, otwarcie, minimum, maksimum, wolumen, obrot)
    lista_akcji.append(notowanie)
    for _ in lista_akcji:
        print(f"{spolka} - aktualny kurs: {kurs}, otwarcie: {otwarcie}, maksymalny: {maksimum}, minimalny: {minimum}, wolumen: {wolumen}, akcji, obrót; {obrot} zł.")

lista_obserwowanych_spolek = ["https://www.biznesradar.pl/notowania/CRI#1d_lin_lin", "https://www.biznesradar.pl/notowania/EASYCALL-PL#1d_lin_lin"]
