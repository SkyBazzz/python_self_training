import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


class EveryDownloadsChrome:
    def __call__(self, browser):
        if not browser.current_url.startswith("chrome://downloads"):
            browser.get("chrome://downloads/")
        return browser.execute_script(
            """
               var items = document.querySelector('downloads-manager')
                   .shadowRoot.getElementById('downloadsList').items;
               if (items.every(e => e.state === "COMPLETE"))
                   return True;
               return false;
               """
        )


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://wiki.python.org/moin/FrontPage")
driver.maximize_window()
search_field = driver.find_element(By.XPATH, "//input[@id='searchinput']")
search_field.send_keys("Beginner")
search_field.send_keys(Keys.RETURN)
more_actions = Select(driver.find_element(By.XPATH, "//select[@name='action']"))

more_actions.select_by_visible_text("Raw Text")
# time.sleep(5)
path = WebDriverWait(driver, 5).until(EveryDownloadsChrome())
time.sleep(25)
driver.quit()
