# =========================================================
# ProductPage - Page Object for Product Detail Page
# =========================================================
#
# Handles: Product details, Add to cart, Price/Description
# Extends: BasePage
#
# =========================================================

import logging
from selenium.webdriver.common.by import By
from Pages.Base_Page  import BasePage

logger = logging.getLogger(__name__)


class ProductPage(BasePage):

    """
    ProductPage - Handles product detail view and add-to-cart
    on demoblaze.com.
    """

    # =========================================================
    # LOCATORS
    # =========================================================

    PRODUCT_TITLE = (By.CSS_SELECTOR, ".name")

    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price-container")

    PRODUCT_DESCRIPTION = (By.ID, "more-information")

    ADD_TO_CART_BUTTON = (
        By.XPATH,
        "//a[text()='Add to cart']"
    )

    PRODUCT_IMAGE = (
        By.CSS_SELECTOR,
        ".product-image img, #imgp img"
    )

    NAV_HOME = (
        By.XPATH,
        "//a[text()='Home ']"
    )

    # =========================================================
    # ACTION METHODS
    # =========================================================

    def get_product_title(self):
        """Get product title/name from detail page"""

        logger.info("Getting product title")

        return self.get_text(self.PRODUCT_TITLE)

    def get_product_price(self):
        """Get product price from detail page"""

        logger.info("Getting product price")

        price_text = self.get_text(self.PRODUCT_PRICE)

        logger.info(f"Raw price text: {price_text}")

        return price_text

    def get_product_description(self):
        """Get product description"""

        logger.info("Getting product description")

        return self.get_text(self.PRODUCT_DESCRIPTION)

    def add_to_cart(self):
        """
        Click 'Add to cart' button and handle alert confirmation
        """

        logger.info("Adding product to cart")

        # Ensure product page is loaded before interacting
        try:
            self.wait_for_element(self.PRODUCT_TITLE, timeout=10)
        except Exception:
            logger.warning("Product title not detected before clicking Add to cart")

        # Try clickable click first, then fall back to JS click
        try:
            btn = self.wait_for_element_clickable(self.ADD_TO_CART_BUTTON, timeout=8)
            btn.click()
        except Exception:
            logger.warning("Clickable wait failed; attempting visibility wait then JS click")
            try:
                el = self.wait_for_element(self.ADD_TO_CART_BUTTON, timeout=8)
                self.driver.execute_script("arguments[0].click();", el)
            except Exception:
                logger.error("Failed to click 'Add to cart' using all strategies")
                raise

        self.hard_wait(2)

        # demoblaze shows alert: "Product added"

        try:

            alert_text = self.accept_alert(timeout=5)

            logger.info(f"Cart alert: {alert_text}")

            return alert_text

        except Exception:

            logger.warning("No alert appeared after adding to cart")

            return ""

    # =========================================================
    # VALIDATION METHODS
    # =========================================================

    def is_product_page_loaded(self):
        """Verify product detail page is loaded"""

        return self.is_element_visible(
            self.PRODUCT_TITLE,
            timeout=10
        )

    def is_product_image_displayed(self):
        """Check if product image is visible"""

        return self.is_element_visible(
            self.PRODUCT_IMAGE,
            timeout=5
        )

    # =========================================================
    # NAVIGATION METHODS
    # =========================================================

    def navigate_to_home(self):
        """Go back to home page"""

        logger.info("Navigating back to home")

        self.click_element(self.NAV_HOME)

        self.hard_wait(1)