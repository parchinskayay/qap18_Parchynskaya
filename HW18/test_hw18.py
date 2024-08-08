import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

URL = 'https://elfsight.com/'
url = 'https://dash.elfsight.com/login'


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.close()
    driver.quit()


def test_forgot_password(driver):
    driver.get(url)
    cont_with_email = driver.find_element(By.XPATH, '(//*[text()="Continue with Email"])')
    cont_with_email.click()
    email_addr = driver.find_element(By.XPATH, '//input[@name="email"]')
    email_addr.click()
    email_addr.send_keys('parchinskayay@mail.ru')
    passw = driver.find_element(By.XPATH, '//input[@autocomplete="current-password"]')
    passw.click()
    passw.send_keys('1234Qwerty')
    log_in = driver.find_element(By.XPATH, '//button[@type="submit"]')
    log_in.click()
    driver.implicitly_wait(15)
    forgot_password = driver.find_element(By.CSS_SELECTOR, '[class="sc-b67f0229-0 eTiRRB"]')
    assert forgot_password.is_displayed()


def test_page_contain_text(driver):
    driver.get(URL)
    text = driver.find_element(By.CSS_SELECTOR, '[class="page-home-hero-start-caption"]')
    assert text.is_displayed()


def test_find_text(driver):
    driver.get(URL)
    el = driver.find_element(By.CLASS_NAME, 'page-home-platforms-text')
    assert el.text == 'Integrated with any website platform, no matter which is yours.'


def test_widgets(driver):
    driver.get(URL)
    widgets = driver.find_element(By.XPATH, '/html/body/div[3]/div/header/div/nav/ul/li[3]/a')
    widgets.click()
    time.sleep(2)
    assert widgets.is_enabled()


def test_banner(driver):
    driver.get(URL)
    banner = driver.find_element(By.CSS_SELECTOR, 'body > div.outer > div > a > img')
    driver.implicitly_wait(15)
    assert banner.is_displayed()
