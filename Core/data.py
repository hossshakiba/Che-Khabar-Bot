import requests
from bs4 import BeautifulSoup

url = "https://www.tgju.org/"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")


def date():
    date = soup.find("div", class_="date").text
    return date[:date.find('-')]

def sekke_price():
    sekke_emami = soup.find("th", text="سکه امامی").find_next_siblings("td")
    sekke_bahar = soup.find("th", text="سکه بهار آزادی").find_next_siblings("td")
    nim = soup.find("th", text="نیم سکه").find_next_siblings("td")
    rob = soup.find("th", text="ربع سکه").find_next_siblings("td")
    price = {
        'emami':sekke_emami,
        'bahar':sekke_bahar,
        'nim':nim,
        'rob':rob,
    }

    return price


def gold_price():
    tala_18 = soup.find("tr", attrs={"data-market-row":"geram18"}).find_all("td")
    tala_24 = soup.find("tr", attrs={"data-market-row":"geram24"}).find_all("td")
    price = {
        'tala_18':tala_18,
        'tala_24':tala_24
    }

    return price

def arz_price():
    dollar_usa = soup.find("tr", attrs={"data-market-row":"price_dollar_rl"}).find_all("td")
    euro = soup.find("tr", attrs={"data-market-row":"price_eur"}).find_all("td")
    pond = soup.find("tr", attrs={"data-market-row":"price_gbp"}).find_all("td")
    frank = soup.find("tr", attrs={"data-market-row":"price_chf"}).find_all("td")
    derham = soup.find("tr", attrs={"data-market-row":"price_aed"}).find_all("td")
    lir = soup.find("tr", attrs={"data-market-row":"price_try"}).find_all("td")
    youan = soup.find("tr", attrs={"data-market-row":"price_cny"}).find_all("td")
    yen = soup.find("tr", attrs={"data-market-row":"price_jpy"}).find_all("td")
    dollar_canada = soup.find("tr", attrs={"data-market-row":"price_cny"}).find_all("td")
    price = {
        'dollar_usa':dollar_usa,
        'euro':euro,
        'pond':pond,
        'frank':frank,
        'derham':derham,
        'lir':lir,
        'youan':youan,
        'yen':yen,
        'dollar_canada':dollar_canada,
    }

    return price

def stock():
    stock = soup.find("table", class_="data-table market-table bourse-table mobile-half small-th-text").find_all('td')
    shakhes_kol = stock[0].text
    shakhes_kol_hamvazn = stock[2].text
    shakhes_kol_faraburs = stock[4].text
    stock_dict = {
        'shakhes_kol' : shakhes_kol,
        'shakhes_kol_hamvazn' : shakhes_kol_hamvazn,
        'shakhes_kol_faraburs' : shakhes_kol_faraburs,
    }

    return stock_dict

def crypto():
    crypto = soup.find("table", class_="data-table market-table market-section-right crypto-table flag-none").find_all('td')
    return crypto
