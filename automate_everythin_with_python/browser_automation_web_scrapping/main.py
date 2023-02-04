import re
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import smtplib
import ssl


def clean_text(text: str):
    return re.findall(r"\d+", text)


def get_driver(url: str = "https://automated.pythonanywhere.com/") -> WebDriver:
    options = Options()
    options.add_argument("disable-infobars")
    options.add_argument("--start-fullscreen")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    chrome_driver.get(url)

    return chrome_driver


def find_text():
    with get_driver() as driver:
        # simple text
        title = driver.find_element(By.XPATH, "//h1[@class='animated fadeIn mb-4']")
        print(title.text)
        # dynamic text
        time.sleep(2)
        dynamic_text = driver.find_element(By.ID, "displaytimer")
        print(clean_text(dynamic_text.text))


def sep_text(text):
    """Extract only the temperature from text"""
    return float(text.split(" ")[0])


def send_email(price):
    sender = "skyaleksandr@gmail.com"  # os.getenv('EMAIL_SENDER')
    receiver = "skyaleksandr@gmail.com"  # os.getenv('EMAIL_RECEIVER')
    password = "puxhfsuekxfuxupz"  # os.getenv('PASSWORD')
    message = f"""
    The stock price is now {price}%
    """

    port = 465
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)


def main():
    web_site = "https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6"
    web_dr = get_driver(web_site)
    time.sleep(2)
    element = web_dr.find_element(by="xpath", value="//span[@class = 'stock-trend trend-grow']")
    text = str(sep_text(element.text))

    if float(text) > -0.10:
        send_email(text)


if __name__ == "__main__":
    main()
