import logging
from selenium.webdriver.common.by import By

from Pages.Base_Page import BasePage

logger = logging.getLogger(__name__)


class CheckoutPage(BasePage):
    """
    CheckoutPage - Handles the Place Order modal
    and purchase confirmation on demoblaze.com.
    """

    # =========================================================
    # LOCATORS
    # =========================================================
    

    # Order Form Modal
    ORDER_MODAL = (By.ID, "orderModal")
    NAME_INPUT = (By.ID, "name")
    COUNTRY_INPUT = (By.ID, "country")
    CITY_INPUT = (By.ID, "city")
    CREDIT_CARD_INPUT = (By.ID, "card")
    MONTH_INPUT = (By.ID, "month")
    YEAR_INPUT = (By.ID, "year")

    # Buttons
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Place Order']")
    PURCHASE_BUTTON = (By.XPATH, "//button[text()='Purchase']")
    CLOSE_BUTTON = (
        By.XPATH,
        "//div[@id='orderModal']//button[text()='Close']"
    )

    # Success Message
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".sweet-alert h2")
    CONFIRMATION_TEXT = (By.CSS_SELECTOR, ".sweet-alert p")
    OK_BUTTON = (By.XPATH, "//button[text()='OK']")
    # Backwards-compatible aliases used elsewhere in tests
    CONFIRMATION_TITLE = SUCCESS_MESSAGE
    CONFIRMATION_OK_BUTTON = OK_BUTTON

    # =========================================================
    # ACTION METHODS
    # =========================================================

    def open_checkout_modal(self):
        """
        Wait for the checkout modal to be visible (button click happens in Cart page)
        """
        logger.info("Opening checkout modal")
        # Use existing wait helper defined in BasePage
        self.wait_for_element(self.ORDER_MODAL)

    def enter_name(self, name):
        """
        Enter customer name
        """
        logger.info(f"Entering name: {name}")
        self.enter_text(self.NAME_INPUT, name)

    def enter_country(self, country):
        """
        Enter country
        """
        logger.info(f"Entering country: {country}")
        self.enter_text(self.COUNTRY_INPUT, country)

    def enter_city(self, city):
        """
        Enter city
        """
        logger.info(f"Entering city: {city}")
        self.enter_text(self.CITY_INPUT, city)

    def enter_credit_card(self, card_number):
        """
        Enter credit card number
        """
        logger.info("Entering credit card details")
        self.enter_text(self.CREDIT_CARD_INPUT, card_number)

    def enter_month(self, month):
        """
        Enter expiry month
        """
        logger.info(f"Entering month: {month}")
        self.enter_text(self.MONTH_INPUT, month)

    def enter_year(self, year):
        """
        Enter expiry year
        """
        logger.info(f"Entering year: {year}")
        self.enter_text(self.YEAR_INPUT, year)

    def fill_checkout_form(
        self,
        name,
        country,
        city,
        card_number,
        month,
        year
    ):
        """
        Fill complete checkout form
        """
        logger.info("Filling checkout form")

        self.enter_name(name)
        self.enter_country(country)
        self.enter_city(city)
        self.enter_credit_card(card_number)
        self.enter_month(month)
        self.enter_year(year)

    def click_purchase(self):
        """
        Click Purchase button
        """
        logger.info("Clicking Purchase button")
        self.click_element(self.PURCHASE_BUTTON)

    def close_checkout_modal(self):
        """
        Close order modal
        """
        logger.info("Closing checkout modal")
        self.click_element(self.CLOSE_BUTTON)

    # =========================================================
    # VALIDATION METHODS
    # =========================================================

    def is_order_modal_displayed(self):
        """
        Check if order modal is visible
        """
        return self.is_element_displayed(self.ORDER_MODAL)

    def get_success_message(self):
        """
        Get purchase success message
        """
        return self.get_text(self.SUCCESS_MESSAGE)

    def get_confirmation_text(self):
        """
        Get full confirmation text
        """
        return self.get_text(self.CONFIRMATION_TEXT)

    def click_ok(self):
        """
        Click OK button after successful purchase
        """
        logger.info("Clicking OK button")
        self.click_element(self.OK_BUTTON)

    def complete_purchase(
        self,
        name,
        country,
        city,
        card_number,
        month,
        year
    ):
        """
        Complete full purchase flow
        """
        logger.info("Starting complete purchase flow")

        self.open_checkout_modal()

        self.fill_checkout_form(
            name,
            country,
            city,
            card_number,
            month,
            year
        )

        self.click_purchase()

        logger.info("Purchase completed successfully")
        # =========================================================
    # CONFIRMATION METHODS
    # =========================================================

    def get_confirmation_title(self):
        """Get order confirmation title (e.g., 'Thank you for your purchase!')"""
        logger.info("Getting confirmation title")

        return self.get_text(self.CONFIRMATION_TITLE)

    def get_confirmation_details(self):
        """Get order confirmation details text"""
        logger.info("Getting confirmation details")

        return self.get_text(self.CONFIRMATION_TEXT)

    def click_confirmation_ok(self):
        """Click OK on confirmation dialog"""
        logger.info("Clicking confirmation OK")

        self.click_element(self.CONFIRMATION_OK_BUTTON)
        self.hard_wait(1)

    def is_order_confirmed(self):
        """Check if order confirmation is displayed"""
        return self.is_element_visible(
            self.CONFIRMATION_TITLE,
            timeout=10
        )

    def is_checkout_form_displayed(self):
        """Check if checkout form modal is visible"""
        return self.is_element_visible(
            self.ORDER_MODAL,
            timeout=5
        )
