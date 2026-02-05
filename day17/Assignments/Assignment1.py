from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/dropdown")
    
    dropdown_element = driver.find_element(By.ID, "dropdown")
    select = Select(dropdown_element)
    
    select.select_by_visible_text("Option 2")
    print("Selected Option 2 from dropdown")
    time.sleep(1) 

    driver.get("https://the-internet.herokuapp.com/checkboxes")
    
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "#checkboxes input")
    
    for i, checkbox in enumerate(checkboxes):
        if not checkbox.is_selected():
            checkbox.click()
            print(f"Checkbox {i+1} was unchecked, now checked.")
        else:
            print(f"Checkbox {i+1} was already checked.")

    driver.get("https://the-internet.herokuapp.com/login")
    
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    driver.find_element(By.CSS_SELECTOR, "button.radius").click()
    
    flash_msg = driver.find_element(By.ID, "flash").text
    if "You logged into a secure area!" in flash_msg:
        print("Success: Confirmation message verified!")
    else:
        print("Failure: Login message not found.")

finally:
    time.sleep(2)
    driver.quit()