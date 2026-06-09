import logging
from selenium.webdriver.common.by import By
from Pages.Base_Page import BasePage

logger = logging.getLogger(__name__)


class HomePage(BasePage):
    """
    HomePage - Handles navigation, categories, and product listing on demoblaze.com.
    """

    # =========================================================
    # LOCATORS
    # =========================================================

    # Navigation Menu
    HOME_LINK = (By.XPATH, "//a[contains(@class,'nav-link') and text()='Home ']")
    CONTACT_LINK = (By.XPATH, "//a[text()='Contact']")
    ABOUT_US_LINK = (By.XPATH, "//a[text()='About us']")
    CART_LINK = (By.ID, "cartur")
    LOGIN_LINK = (By.ID, "login2")
    SIGNUP_LINK = (By.ID, "signin2")

    # Categories
    CATEGORIES_HEADER = (By.ID, "cat")
    PHONES_CATEGORY = (By.XPATH, "//a[text()='Phones']")
    LAPTOPS_CATEGORY = (By.XPATH, "//a[text()='Laptops']")
    MONITORS_CATEGORY = (By.XPATH, "//a[text()='Monitors']")

    # Product List
    PRODUCT_CARDS = (By.CSS_SELECTOR, "#tbodyid .card")
    PRODUCT_LINKS = (By.CSS_SELECTOR, "#tbodyid .card-title a")
    PRODUCT_PRICES = (By.CSS_SELECTOR, "#tbodyid .card-block h5")
    PRODUCT_IMAGES = (By.CSS_SELECTOR, "#tbodyid .card-img-top")

    # Pagination
    NEXT_BUTTON = (By.ID, "next2")
    PREVIOUS_BUTTON = (By.ID, "prev2")

    # Carousel
    CAROUSEL = (By.ID, "carouselExampleIndicators")

    # =========================================================
    # NAVIGATION METHODS
    # =========================================================

    def click_home(self):
        """Navigate to Home page"""
        logger.info("Clicking Home link")

        self.click_element(self.HOME_LINK)
        self.hard_wait(1)

    def click_contact(self):
        """Navigate to Contact page"""
        logger.info("Clicking Contact link")

        self.click_element(self.CONTACT_LINK)
        self.hard_wait(1)

    def click_about_us(self):
        """Click About Us link"""
        logger.info("Clicking About Us link")

        self.click_element(self.ABOUT_US_LINK)
        self.hard_wait(1)

    def click_cart(self):
        """Navigate to Cart page"""
        logger.info("Clicking Cart link")

        self.click_element(self.CART_LINK)
        self.hard_wait(1)

    # =========================================================
    # CATEGORY METHODS
    # =========================================================

    def select_phones_category(self):
        """Click Phones category"""
        logger.info("Selecting Phones category")

        self.click_element(self.PHONES_CATEGORY)
        self.hard_wait(1)

    def select_laptops_category(self):
        """Click Laptops category"""
        logger.info("Selecting Laptops category")

        self.click_element(self.LAPTOPS_CATEGORY)
        self.hard_wait(1)

    def select_monitors_category(self):
        """Click Monitors category"""
        logger.info("Selecting Monitors category")

        self.click_element(self.MONITORS_CATEGORY)
        self.hard_wait(1)

    def select_category(self, category_name):
        """Select category by name - Phones, Laptops, Monitors"""

        logger.info(f"Selecting category: {category_name}")

        category_map = {
            "phones": self.PHONES_CATEGORY,
            "laptops": self.LAPTOPS_CATEGORY,
            "monitors": self.MONITORS_CATEGORY
        }

        locator = category_map.get(category_name.lower())

        if locator:
            self.click_element(locator)
            self.hard_wait(1)

        else:
            raise ValueError(f"Unknown category: {category_name}")

    # =========================================================
    # PRODUCT METHODS
    # =========================================================

    def get_product_count(self):
        """Get number of products displayed on page"""

        self.hard_wait(1)

        count = self.get_element_count(self.PRODUCT_CARDS)

        logger.info(f"Products displayed: {count}")

        return count

    def select_product_by_name(self, product_name):
        """Click on a product by its name"""

        logger.info(f"Selecting product: {product_name}")

        product_locator = (
            By.XPATH,
            f"//a[text()='{product_name}']"
        )

        self.click_element(product_locator)
        self.hard_wait(1)

    def get_all_product_names(self):
        """Get list of all product names on current page"""

        self.hard_wait(1)

        elements = self.driver.find_elements(*self.PRODUCT_LINKS)

        names = [el.text for el in elements if el.text]

        logger.info(f"Product names: {names}")

        return names

    def get_all_product_prices(self):
        """Get all product prices displayed on page"""

        self.hard_wait(1)

        elements = self.driver.find_elements(*self.PRODUCT_PRICES)

        prices = [el.text for el in elements if el.text]

        logger.info(f"Product prices: {prices}")

        return prices

    def is_product_displayed(self, product_name):
        """Check if a specific product is displayed"""

        product_locator = (
            By.XPATH,
            f"//a[text()='{product_name}']"
        )

        return self.is_element_visible(product_locator, timeout=5)

    # =========================================================
    # PAGINATION METHODS
    # =========================================================

    def click_next(self):
        """Click Next button for product pagination"""

        logger.info("Clicking Next button")

        self.click_element(self.NEXT_BUTTON)
        self.hard_wait(1)

    def click_previous(self):
        """Click Previous button for product pagination"""

        logger.info("Clicking Previous button")

        self.click_element(self.PREVIOUS_BUTTON)
        self.hard_wait(1)

    # =========================================================
    # VALIDATION METHODS
    # =========================================================

    def is_home_page_loaded(self):
        """Verify home page is loaded by checking carousel"""

        return self.is_element_visible(
            self.CAROUSEL,
            timeout=10
        )

    def verify_categories_displayed(self):
        """Verify all 3 categories are visible"""

        phones = self.is_element_visible(self.PHONES_CATEGORY)
        laptops = self.is_element_visible(self.LAPTOPS_CATEGORY)
        monitors = self.is_element_visible(self.MONITORS_CATEGORY)

        logger.info(
            f"Categories visible - Phones: {phones}, "
            f"Laptops: {laptops}, Monitors: {monitors}"
        )

        return phones and laptops and monitors

    def verify_navigation_menu(self):
        """Verify all navigation links are visible"""

        home = self.is_element_visible(self.HOME_LINK)
        contact = self.is_element_visible(self.CONTACT_LINK)
        cart = self.is_element_visible(self.CART_LINK)

        logger.info(
            f"Navigation - Home: {home}, "
            f"Contact: {contact}, Cart: {cart}"
        )

        return home and contact and cart