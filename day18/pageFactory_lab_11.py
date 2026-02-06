from selenium import webdriver
from lab_11_pageFactory import CartPage
import time

# Initialization
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://tutorialsninja.com/demo')

try:
    page = CartPage(driver)

    # 1. Verify title
    assert "Your Store" in driver.title
    print("Step 1: Title Verified")

    # 2. Go to Desktops > Mac
    page.navigate_to_mac()
    print("Step 2: Navigated to Mac")

    # 3. Verify 'Mac' heading (Step added after Step 5 in your list)
    page.verify_mac_heading()
    print("Step 3: Mac Heading Verified")

    # 4. Sort By Name (A-Z)
    page.sort_by_name()
    print("Step 4: Sorted A-Z")

    # 5. Add to Cart
    page.add_to_cart_btn.click()
    print("Step 5: Added to Cart")

    # 6. Search for 'Monitors' (Value changed from Mobile)
    page.search_for("Monitors")
    print("Step 6: Searched for Monitors")

    # 7. Advanced Search (Clear and check description)
    page.perform_description_search()
    print("Step 7: Advanced Search Completed")

    print("\nFinal Status: PASS")

finally:
    time.sleep(3)
    driver.quit()