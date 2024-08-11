import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.bbc.com/news')
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.close()
    driver.quit()


class TestLocators:

    def test_logo_bbc_1(self, driver):
        logo_bbc = driver.find_element(By.CSS_SELECTOR, '[class="sc-49542412-10 jTsKD"] [class="sc-1097f7fe-0 jbvZzi"]')
        assert logo_bbc.is_displayed()

    def test_sign_in_2(self, driver):
        sign_in_button = driver.find_element(By.XPATH, '(//*[@aria-hidden="false"])[2]')
        assert sign_in_button.is_displayed()

    def test_home_3(self, driver):
        home = driver.find_element(By.CSS_SELECTOR, '[class="sc-f116bf72-4 yKcKi"]')
        assert home.is_displayed()

    def test_sport_4(self, driver):
        sport = driver.find_element(By.CSS_SELECTOR, 'a[href*="/sport"]')
        assert sport.is_displayed()

    # пятый элемент на странице отсутствует, поэтому я сделала вместо необходимого Reel, поиск элемента Culture

    def test_culture_5(self, driver):
        culture = driver.find_element(By.CSS_SELECTOR, 'a[href*="/culture"]')
        assert culture.is_displayed()

    def test_travel_6(self, driver):
        travel = driver.find_element(By.XPATH, '(//*[@class="sc-f116bf72-4 eqTiTw"])[6]')
        assert travel.is_displayed()

    def test_three_dots_7(self, driver):
        three_dots = driver.find_element(By.CSS_SELECTOR, '[aria-label="Open menu"]')
        assert three_dots.is_displayed()

    def test_text_of_news_8(self, driver):
        text_of_news = driver.find_element(By.XPATH, '(//h2[@class="sc-4fedabc7-3 zTZri"][1])')
        assert text_of_news.is_displayed()

    def test_picture_of_news_9(self, driver):
        picture_of_news = driver.find_element(By.XPATH, '(//img[@alt="Donald Trump speaking at a campaign rally"])')
        assert picture_of_news.is_displayed()

    def test_release_time_10(self, driver):
        release_time = driver.find_element(By.XPATH, '(//*[@class="sc-4e537b1-1 dsUUMv"])[1]')
        driver.execute_script("arguments[0].scrollIntoView(true);", release_time)
        assert release_time.is_displayed()

    def test_feature_and_analysis_11(self, driver):
        feature_and_analysis = driver.find_element(By.XPATH, "//*[@data-testid='virginia-title' and text()="
                                                             "'Features & analysis']")
        driver.execute_script("arguments[0].scrollIntoView(true);", feature_and_analysis)
        assert feature_and_analysis.is_displayed()

    def test_news(self, driver):
        news = driver.find_element(By.CSS_SELECTOR, '[class="sc-66cb3400-0 kSKEBf"] [class="sc-1097f7fe-0 jbvZzi"]')
        assert news
