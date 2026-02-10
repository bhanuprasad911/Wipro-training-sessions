import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


GRID_URL = "http://localhost:4444"

@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_remote_execution(browser):
    if browser == "chrome":
        options = ChromeOptions()
    elif browser == "firefox":
        options = FirefoxOptions()
        options.binary_location = "/usr/bin/firefox"
    
    driver = webdriver.Remote(
        command_executor=GRID_URL,
        options=options
    )
    
    try:
        driver.get("https://www.selenium.dev/")
        expected_title = "Selenium"
        assert expected_title in driver.title
        
        capabilities = driver.capabilities
        browser_name = capabilities.get("browserName")
        browser_version = capabilities.get("browserVersion")
        platform = capabilities.get("platformName")
        
        print(f"\n--- Execution Details ---")
        print(f"Browser:  {browser_name} (v{browser_version})")
        print(f"Platform: {platform}")
        print(f"Result:   Title verified successfully!")
        print(f"--------------------------")

    finally:
        driver.quit()