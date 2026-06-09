from selenium.webdriver.common.by import By
import logging
from Pages.Base_Page import BasePage

logger = logging.getLogger(__name__)

class ContactPage(BasePage):
    """
    ContactPage - Handles the 'Contact' modal form on demoblaze.com.
    """

    # =========================================================
    # LOCATORS
    # =========================================================

    CONTACT_MODAL = (By.ID, "exampleModal")
    CONTACT_EMAIL = (By.ID, "recipient-email")
    CONTACT_NAME = (By.ID, "recipient-name")
    CONTACT_MESSAGE = (By.ID, "message-text")
    SEND_MESSAGE_BUTTON = (By.XPATH, "//button[text()='Send message']")
    CLOSE_CONTACT_BUTTON = (By.XPATH, "//div[@id='exampleModal']//button[text()='Close']")
    CONTACT_TITLE = (By.CSS_SELECTOR, "#exampleModal .modal-title")

    # =========================================================
    # ACTION METHODS
    # =========================================================

    def enter_contact_email(self, email):
        """Enter email in contact form"""
        logger.info(f"Entering contact email: {email}")

        self.enter_text(self.CONTACT_EMAIL, email)

    def enter_contact_name(self, name):
        """Enter name in contact form"""
        logger.info(f"Entering contact name: {name}")

        self.enter_text(self.CONTACT_NAME, name)

    def enter_message(self, message):
        """Enter message in contact form"""
        logger.info(f"Entering message: {message[:50]}...")

        self.enter_text(self.CONTACT_MESSAGE, message)

    def click_send_message(self):
        """Click 'Send message' button"""
        logger.info("Clicking Send message button")

        self.click_element(self.SEND_MESSAGE_BUTTON)
        self.hard_wait(1)

    def send_contact_message(self, email, name, message):
        """
        Complete contact form submission:
        1. Enter email
        2. Enter name
        3. Enter message
        4. Click send
        """

        logger.info("Filling and sending contact form")

        self.enter_contact_email(email)
        self.enter_contact_name(name)
        self.enter_message(message)

        self.click_send_message()

        # Handle alert confirmation
        try:
            alert_text = self.accept_alert(timeout=5)

            logger.info(f"Contact alert: {alert_text}")

            return alert_text

        except Exception:
            logger.warning("No alert after contact form submission")

            return ""

    def close_contact_modal(self):
        """Close contact modal without sending"""
        logger.info("Closing contact modal")

        self.click_element(self.CLOSE_CONTACT_BUTTON)

    # =========================================================
    # VALIDATION METHODS
    # =========================================================

    def is_contact_modal_displayed(self):
        """Check if contact modal is visible"""
        return self.is_element_visible(
            self.CONTACT_MODAL,
            timeout=5
        )

    def get_contact_modal_title(self):
        """Get contact modal title text"""
        return self.get_text(self.CONTACT_TITLE)
