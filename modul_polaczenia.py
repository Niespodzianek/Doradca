import requests


def polaczenienie_ze_strona_www_o_adresie(url):
    try:
        strona_www = requests.get(url)
        # print(strona_www.status_code)
        # print(strona_www.ok)
        # print(tekst_strony_www)
    except requests.exceptions as error:
        print(f"Błąd przy połączeniu: {error}")
        return

    try:
        strona_www.raise_for_status()
    except requests.HTTPError as error:
        print(f"Żądanie zakończone niepowodzeniem: {error}")
        return

    return strona_www.text
