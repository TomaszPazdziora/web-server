import requests
from bs4 import BeautifulSoup

def get_angle():
    url = "https://meteogram.pl/slonce/polska/linia/"

    # pobranie zawartości strony
    response = requests.get(url)
    html = response.content

    # utworzenie obiektu BeautifulSoup z zawartością strony
    soup = BeautifulSoup(html, "html.parser")

    # znalezienie elementu zawierającego wartość azymutu
    azimuth_span = soup.find("span", {"id": "azimuth"})
    altitude_span = soup.find("span", {"id": "altitude"})

    # pobranie wartości azymutu ze znacznika span
    azimuth_value = azimuth_span.text.split("°")[0]
    altitude_value = altitude_span.text.split("°")[0]

    return (azimuth_value + ' ' + altitude_value)
