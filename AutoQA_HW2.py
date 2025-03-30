from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

BROWSER_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
CHROMEDRIVER_PATH = r"C:\Program Files\chromedriver-win64\chromedriver.exe"

options = Options()
options.binary_location = BROWSER_PATH
options.add_argument("--start-maximized")

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://itcareerhub.de/ru")
    wait = WebDriverWait(driver, 10)
    payment_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Способы оплаты")))
    payment_link.click()
    time.sleep(3)
    screenshot_path = os.path.join(os.getcwd(), "payment_section.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")
finally:
    driver.quit()
