from selenium import webdriver
from selenium.webdriver.common.by import By
from Login_pageFactory import loginpage_PageFactory
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index')
time.sleep(5)
loginObj = loginpage_PageFactory(driver)
loginObj.enterusername("Admin")
loginObj.enterpassword("admin123")
loginObj.clicklogin()