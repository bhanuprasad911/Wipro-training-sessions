from pages.cart_page import CartPage
from config import Config

def test_mac_selection_flow(driver):
    # 1. Open URL
    driver.get(Config.BASE_URL)
    cart_page = CartPage(driver)

    # 2. Navigate and Verify
    cart_page.navigate_to_mac()
    assert cart_page.get_header_text() == "Mac"
    
    # 3. Perform Actions
    cart_page.sort_products("Name (A - Z)")
    cart_page.input_text(CartPage.SEARCH_BOX, "Monitors")
    
    print("\nTest Case Result: PASSED")