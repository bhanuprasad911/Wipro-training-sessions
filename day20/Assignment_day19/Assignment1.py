from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time


driver = webdriver.Chrome()

driver.implicitly_wait(10)

try:
    driver.get("https://www.google.com")

    wait = WebDriverWait(driver, 10)
    search_box = wait.until(EC.element_to_be_clickable((By.NAME, "q")))
    
    print("Message: Search box is now available for interaction (Explicit Wait).")
    search_box.send_keys("Selenium Python")

    fluent_wait = WebDriverWait(
        driver, 
        timeout=15, 
        poll_frequency=2, 
        ignored_exceptions=[NoSuchElementException, ElementNotInteractableException]
    )

    search_button = fluent_wait.until(EC.visibility_of_element_located((By.NAME, "btnK")))

    print(f"Message: Element '{search_button.get_attribute('name')}' is ready (Fluent Wait).")
    
    search_button.click()

finally:
    time.sleep(2)
    driver.quit()