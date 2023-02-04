import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_rates(city="lvov", currency="usd", rate_date=datetime.now()):
    today = rate_date.date()
    response = requests.get(f"https://minfin.com.ua/ua/currency/{city}/{currency}/{today}/")
    text = response.text
    soup = BeautifulSoup(text, "html.parser")
    table = soup.find_all("td")
    banks_low_rate = table[1].find("span").get_text()[:7].replace("\n", "0").replace("-", "0")
    banks_high_rate = table[2].find("span").get_text()[:7].replace("\n", "0").replace("-", "0")
    market_low_rate = table[5].find("span").get_text()[:7].replace("\n", "0").replace("-", "0")
    market_high_rate = table[6].find("span").get_text()[:7].replace("\n", "0").replace("-", "0")
    pretty_today = rate_date.strftime("%Y-%m-%d: %a %H:%m:%S")
    with open(
        "/Users/obalkash/PycharmProjects/python_self_training/fun/exchange_rate/lviv_exchange_rate.txt", mode="a"
    ) as rates:
        information = f"{pretty_today}: Banks: {banks_low_rate}--{banks_high_rate}; Market {market_low_rate}--{market_high_rate}\n"
        rates.write(information)

    return {
        "banks": (banks_low_rate, banks_high_rate),
        "market": (market_low_rate, market_high_rate),
    }


print(get_rates())
