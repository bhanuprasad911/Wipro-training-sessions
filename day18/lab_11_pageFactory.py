from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def _find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @property
    def desktop_menu(self): return self._find((By.LINK_TEXT, 'Desktops'))

    @property
    def mac_link(self): return self._find((By.XPATH, "//a[contains(text(),'Mac')]"))

    @property
    def mac_heading(self): return self._find((By.TAG_NAME, "h2"))

    @property
    def sort_dropdown(self): return self._find((By.ID, 'input-sort'))

    @property
    def add_to_cart_btn(self): return self._find((By.XPATH, '//button[contains(@onclick, "cart.add")]'))

    @property
    def search_box(self): return self._find((By.NAME, 'search'))

    @property
    def search_icon(self): return self._find((By.CSS_SELECTOR, '.btn-default.btn-lg'))

    @property
    def description_checkbox(self): return self._find((By.NAME, 'description'))

    @property
    def sub_search_btn(self): return self._find((By.ID, 'button-search'))

    def navigate_to_mac(self):
        self.desktop_menu.click()
        self.mac_link.click()

    def verify_mac_heading(self):
        assert self.mac_heading.text == "Mac", "Heading does not match!"

    def sort_by_name(self):
        select = Select(self.sort_dropdown)
        select.select_by_visible_text('Name (A - Z)')

    def search_for(self, item_name):
        self.search_box.clear()
        self.search_box.send_keys(item_name)
        self.search_icon.click()

    def perform_description_search(self):
        # Clear main search criteria field on the results page
        criteria_box = self._find((By.ID, 'input-search'))
        criteria_box.clear()
        self.description_checkbox.click()
        self.sub_search_btn.click()