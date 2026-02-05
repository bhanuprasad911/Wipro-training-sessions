from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
    alert = wait.until(EC.alert_is_present()) 
    
    print(f"Alert 1 Message: {alert.text}") 
    alert.accept() 
    
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
    confirm = wait.until(EC.alert_is_present())
    confirm.dismiss() 
    
    confirm_result = driver.find_element(By.ID, "result").text
    print(f"Confirmation Result: {confirm_result}")

    driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
    prompt = wait.until(EC.alert_is_present())
    
    my_text = "Selenium is fun!"
    prompt.send_keys(my_text) 
    prompt.accept() 
    result_text = driver.find_element(By.ID, "result").text
    if my_text in result_text:
        print(f"Success! Page displays: {result_text}")
    else:
        print("Verification failed.")

finally:
    time.sleep(2)
    driver.quit()