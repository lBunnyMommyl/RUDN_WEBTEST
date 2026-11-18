from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):

    PAGE_TITLE = (
        By.CLASS_NAME,
        "title"
    )

    CART_BADGE = (
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    def get_title(self):
        return self.get_text(
            self.PAGE_TITLE
        )

    def get_cart_count(self):
        try:
            return int(
                self.get_text(
                    self.CART_BADGE
                )
            )
        except:
            return 0

    def add_item_to_cart(self, item_name):

        locator = (
            By.XPATH,
            f"//div[text()='{item_name}']"
            f"/ancestor::div[@class='inventory_item']"
            f"//button"
        )

        self.click(locator)