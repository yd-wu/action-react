import json
import time

from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

REACTIONS_FILE = "reactions.json"
WAIT_TIMEOUT = 80
SLEEP = 0.15

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


def process_with_city_and_date(reaction, object, city, date):
    """
    Process string object with city and/or date

    Parameters
    ----------
    reaction: json object, reaction
    object: str, string to be updated
    city: str, target city
    date: date, target date

    Returns
    -------
    object: updated object
    """
    if "replace_city" in reaction and reaction["replace_city"] is True:
        object.replace("city", city)
    if "replace_date" in reaction and reaction["replace_date"] is True:
        object.replace("date", datetime.strptime(date, reaction["date_format"]))
    return object


def react(date, city):
    """
    React

    Parameters
    ----------
    city: str, target city
    date: date, target date
    """
    c_service = Service("/usr/bin/chromedriver")
    c_service.command_line_args()
    c_service.start()
    driver = webdriver.Chrome(chrome_options=chrome_options)
    with open(REACTIONS_FILE) as f:
        reactions = json.load(f)
        for reaction in reactions:
            if reaction["type"] == "go_to_url":
                url = process_with_city_and_date(reaction, reaction["url"], city, date)
                driver.get(url)
            elif reaction["type"] == "click_button":
                button_path = process_with_city_and_date(reaction, reaction["button_name"], city, date)
                try:
                    element_present = EC.presence_of_element_located((By.XPATH, button_path))
                    WebDriverWait(driver, WAIT_TIMEOUT).until(element_present)
                except TimeoutException:
                    print("Timed out waiting for page to load")
                time.sleep(SLEEP)
                button = driver.find_element(By.XPATH, button_path)
                button.click()
            else:
                select_name = process_with_city_and_date(reaction, reaction["select_name"], city, date)
                select = Select(driver.find_element(By.ID, select_name))
                if reaction["select_type"] == "visible_text":
                    select.select_by_visible_text(reaction["select_value"])
                else:
                    select.select_by_index(reaction["select_value"])
                time.sleep(SLEEP)
