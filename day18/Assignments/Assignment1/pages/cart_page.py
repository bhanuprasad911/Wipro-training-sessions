from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    # Locators
    DESKTOP_MENU = (By.LINK_TEXT, 'Desktops')
    MAC_LINK = (By.XPATH, "//a[contains(text(),'Mac')]")
    MAC_HEADING = (By.TAG_NAME, "h2")
    SORT_DROPDOWN = (By.ID, 'input-sort')
    SEARCH_BOX = (By.NAME, 'search')

    def navigate_to_mac(self):
        self.click(self.DESKTOP_MENU)
        self.click(self.MAC_LINK)

    def get_header_text(self):
        return self.get_text(self.MAC_HEADING)

    def sort_products(self, sort_text):
        self.select_by_text(self.SORT_DROPDOWN, sort_text)