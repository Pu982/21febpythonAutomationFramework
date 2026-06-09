from selenium.webdriver.common.by import By
from Pages.Base_Page import BasePage
import logging
logger = logging.getLogger(__name__)

class CartPage(BasePage):
    """
    CartPage - Handles cart operations on demoblaze.com (cart.html).
    """

    # =========================================================
    # LOCATORS
    # =========================================================

    CART_TABLE = (By.ID, "tbodyid")
    CART_ROWS = (By.CSS_SELECTOR, "#tbodyid tr")
    CART_PRODUCT_NAMES = (By.CSS_SELECTOR, "#tbodyid tr td:nth-child(2)")
    CART_PRODUCT_PRICES = (By.CSS_SELECTOR, "#tbodyid tr td:nth-child(3)")
    DELETE_BUTTONS = (By.XPATH, "//a[text()='Delete']")
    TOTAL_PRICE = (By.ID, "totalp")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Place Order']")
    CART_HEADER = (By.XPATH, "//h2[text()='Products']")

    # =========================================================
    # ACTION METHODS
    # =========================================================

    def get_cart_items(self):
        """Get list of product names in cart"""
        logger.info("Getting cart items")
        self.hard_wait(1)
        elements = self.driver.find_elements(*self.CART_PRODUCT_NAMES)
        items = [el.text for el in elements if el.text]
        logger.info(f"Cart items: {items}")
        return items

    def get_cart_item_count(self):
        """Get number of items in cart"""
        items = self.get_cart_items()
        count = len(items)
        logger.info(f"Cart item count: {count}")
        return count

    def get_cart_prices(self):
        """Get list of product prices in cart"""
        logger.info("Getting cart prices")
        self.hard_wait(1)
        elements = self.driver.find_elements(*self.CART_PRODUCT_PRICES)
        prices = [el.text for el in elements if el.text]
        logger.info(f"Cart prices: {prices}")
        return prices

    def get_total_price(self):
        """Get total price displayed in cart"""
        logger.info("Getting total price")
        self.hard_wait(1)

        try:
            total = self.get_text(self.TOTAL_PRICE)
            logger.info(f"Total price: {total}")
            return int(total) if total else 0
        except Exception:
            logger.warning("Total price not found")
            return 0

    def delete_item_by_name(self, product_name):
        """Delete a specific product from cart by name"""
        logger.info(f"Deleting item: {product_name}")

        delete_locator = (
            By.XPATH,
            f"//td[text()='{product_name}']/../td[4]/a"
        )

        self.click_element(delete_locator)
        self.hard_wait(1)

        logger.info(f"Deleted: {product_name}")

    def delete_first_item(self):
        """Delete the first item in cart"""
        logger.info("Deleting first cart item")

        self.click_element(self.DELETE_BUTTONS)
        self.hard_wait(1)

    def click_place_order(self):
        """Click 'Place Order' button to open checkout form"""
        logger.info("Clicking Place Order button")

        self.click_element(self.PLACE_ORDER_BUTTON)
        self.hard_wait(1)

    def is_product_in_cart(self, product_name):
        """Check if a specific product exists in cart"""
        items = self.get_cart_items()

        result = product_name in items

        logger.info(f"Product '{product_name}' in cart: {result}")

        return result

    def is_cart_empty(self):
        """Check if cart is empty"""
        self.hard_wait(1)

        count = self.get_element_count(self.CART_ROWS)

        return count == 0

    def is_cart_page_loaded(self):
        """Verify cart page is loaded"""
        return self.is_element_visible(
            self.PLACE_ORDER_BUTTON,
            timeout=10
        )