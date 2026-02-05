from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://letcode.in/window")
time.sleep(5)
driver.find_element(By.ID, "multi").click()
window = driver.window_handles
for child in window:
    driver.switch_to.window(child)
    time.sleep(5)
    print("url", driver.current_url)
time.sleep(10)