import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BROWSER_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
CHROMEDRIVER_PATH = r"C:\Program Files\chromedriver-win64\chromedriver.exe"

@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.binary_location = BROWSER_PATH
    service = Service(executable_path=CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://itcareerhub.de/ru")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_logo_displayed(driver):
    logo = driver.find_element(By.CSS_SELECTOR, "img[src*='Group_3793.svg']")
    assert logo.is_displayed(), "❌ Логотип ITCareerHub не отображается"
    print("✅ Логотип ITCareerHub отображается")

def test_programs_link_displayed(driver):
    link = driver.find_element(By.LINK_TEXT, "Программы")
    assert link.is_displayed(), "❌ Ссылка 'Программы' не отображается"
    print("✅ Ссылка 'Программы' отображается")

def test_payment_methods_link_displayed(driver):
    link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    assert link.is_displayed(), "❌ Ссылка 'Способы оплаты' не отображается"
    print("✅ Ссылка 'Способы оплаты' отображается")

def test_news_link_displayed(driver):
    link = driver.find_element(By.LINK_TEXT, "Новости")
    assert link.is_displayed(), "❌ Ссылка 'Новости' не отображается"
    print("✅ Ссылка 'Новости' отображается")

def test_about_us_link_displayed(driver):
    link = driver.find_element(By.LINK_TEXT, "О нас")
    assert link.is_displayed(), "❌ Ссылка 'О нас' не отображается"
    print("✅ Ссылка 'О нас' отображается")

def test_reviews_link_displayed(driver):
    link = driver.find_element(By.LINK_TEXT, "Отзывы")
    assert link.is_displayed(), "❌ Ссылка 'Отзывы' не отображается"
    print("✅ Ссылка 'Отзывы' отображается")

def test_language_switch_ru_displayed(driver):
    ru = driver.find_element(By.LINK_TEXT, "ru")
    assert ru.is_displayed(), "Переключатель языка 'ru' не отображается"
    print("✅ Переключатель языка 'ru' отображается")

def test_language_switch_de_displayed(driver):
    de = driver.find_element(By.LINK_TEXT, "de")
    assert de.is_displayed(), "❌ Переключатель языка 'de' не отображается"
    print("✅ Переключатель языка 'de' отображается")

def test_phone_icon_click_opens_popup(driver):
    phone_icon_img = driver.find_element(By.CSS_SELECTOR, 'a[href="#popup:form-tr3"] img')
    driver.execute_script("arguments[0].click();", phone_icon_img)

    wait = WebDriverWait(driver, 10)
    popup_text = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(), 'Если вы не дозвонились')]")
        )
    )

    assert popup_text.is_displayed(), "❌ Текст 'Если вы не дозвонились...' не отображается"
    print("✅ Текст 'Если вы не дозвонились...' отображается")
