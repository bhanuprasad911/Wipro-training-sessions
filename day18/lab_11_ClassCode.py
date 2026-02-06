from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Cartpage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Locators
    desktopButton = (By.LINK_TEXT, 'Desktops')
    macButton = (By.XPATH, "//a[contains(text(),'Mac')]")
    macHeading = (By.TAG_NAME, "h2")
    sort_dropdown = (By.ID, 'input-sort')
    cart_button = (By.XPATH, '//button[contains(@onclick, "cart.add")]')
    search_input = (By.NAME, 'search')
    search_button = (By.CSS_SELECTOR, '.btn-default.btn-lg')
    search_criteria_box = (By.ID, 'input-search')
    description_checkbox = (By.NAME, 'description')
    sub_search_button = (By.ID, 'button-search')

    def click_on_desktop(self):
        self.driver.find_element(*self.desktopButton).click()
        
    def mac_option_click(self):
        self.driver.find_element(*self.macButton).click()

    def verify_mac_heading(self):
        heading = self.driver.find_element(*self.macHeading).text
        assert heading == "Mac", f"Expected Mac, but got {heading}"

    def sort_by_name_az(self):
        from selenium.webdriver.support.ui import Select
        select = Select(self.driver.find_element(*self.sort_dropdown))
        select.select_by_visible_text('Name (A - Z)')

    def add_to_cart(self):
        self.driver.find_element(*self.cart_button).click()

    def search_for_item(self, text):
        search_field = self.driver.find_element(*self.search_input)
        search_field.clear()
        search_field.send_keys(text)
        self.driver.find_element(*self.search_button).click()

    def advanced_search(self):
        # Clear search criteria
        criteria = self.driver.find_element(*self.search_criteria_box)
        criteria.clear()
        # Click checkbox and search again
        self.driver.find_element(*self.description_checkbox).click()
        self.driver.find_element(*self.sub_search_button).click()