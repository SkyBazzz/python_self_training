from datetime import datetime

import requests
from bs4 import BeautifulSoup

PATH_TO_RATES = "/Users/obalkash/PycharmProjects/python_self_training/fun/exchange_rate/lviv_exchange_rate.txt"


def get_rates(city="lvov", currency="usd", rate_date=datetime.now()):
    text = collecting_web_data(city, currency, rate_date)
    banks_low, banks_high, market_low, market_high = extracting_rates(text)
    save_rates(rate_date, (banks_low, banks_high, market_low, market_high))

    return {
        "banks": (banks_low, banks_high),
        "market": (market_low, market_high),
    }


def collecting_web_data(city, currency, rate_date):
    today = rate_date.date()
    response = requests.get(f"https://minfin.com.ua/ua/currency/{city}/{currency}/{today}/", timeout=5)
    return response.text


def extracting_rates(text):
    soup = BeautifulSoup(text, "html.parser")
    table = soup.find_all("td")
    banks_low = table[1].get_text()[:7].replace("\n", "0").replace("-", "0").replace(".", "0")
    banks_high = table[2].get_text()[:7].replace("\n", "0").replace("-", "0").replace(".", "0")
    market_low = table[5].get_text()[:7].replace("\n", "0").replace("-", "0").replace(".", "0")
    market_high = table[6].get_text()[:7].replace("\n", "0").replace("-", "0").replace(".", "0")
    return banks_low, banks_high, market_low, market_high


def save_rates(rate_date, bank_rates):
    pretty_date = rate_date.strftime("%Y-%m-%d: %a %H:%M:%S")
    with open(PATH_TO_RATES, mode="a", encoding="utf-8") as rates:
        information = (
            f"{pretty_date}: Banks: {bank_rates[0]}--{bank_rates[1]}; Market {bank_rates[2]}--{bank_rates[3]}\n"
        )
        rates.write(information)


print(get_rates())
