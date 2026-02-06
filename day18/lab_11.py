from selenium import webdriver
from lab_11_ClassCode import Cartpage
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://tutorialsninja.com/demo')

try:
    cart = Cartpage(driver)
    assert "Your Store" in driver.title
    
    cart.click_on_desktop()
    cart.mac_option_click()
    
    cart.verify_mac_heading()
    
    cart.sort_by_name_az()
    cart.add_to_cart()
    
    cart.search_for_item("Monitors")
    
    time.sleep(2) 
    cart.advanced_search()
    
    print("Test Status: PASS")

finally:
    time.sleep(3)
    driver.quit()