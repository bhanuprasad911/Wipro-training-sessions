from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://google.com")
driver.maximize_window()
search_bar = driver.find_element(By.NAME, "q")
search_bar.send_keys("selenium")
search_bar.submit()
time.sleep(10)
driver.minimize_window()
driver.quit()
  
