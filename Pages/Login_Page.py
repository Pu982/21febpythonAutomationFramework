# =========================================================
# LoginPage - Page Object for Login & Logout functionality
# =========================================================
#
# Application: https://demoblaze.com/
# Handles: Login, Logout, Error message validation
# Extends: BasePage (inherits all reusable methods)
#
# =========================================================

import time
import logging
from selenium.webdriver.common.by import By
from Pages.Base_Page import BasePage

logger = logging.getLogger(__name__)


class LoginPage(BasePage):
    """
    LoginPage - Handles all login/logout related actions on demoblaze.com.
    Uses Bootstrap modal for login form.
    """

    # =========================================================
    # LOCATORS - All element locators for Login page
    # =========================================================

    # Navigation
    LOGIN_NAV_LINK = (By.ID, "login2")
    SIGNUP_NAV_LINK = (By.ID, "signin2")
    LOGOUT_NAV_LINK = (By.ID, "logout2")
    WELCOME_USER = (By.ID, "nameofuser")

    # Login Modal
    LOGIN_USERNAME = (By.ID, "loginusername")
    LOGIN_PASSWORD = (By.ID, "loginpassword")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Log in']")
    LOGIN_CLOSE_BUTTON = (
        By.XPATH,
        "//div[@id='logInModal']//button[text()='Close']"
    )
    LOGIN_MODAL = (By.ID, "logInModal")

    # Signup Modal
    SIGNUP_USERNAME = (By.ID, "sign-username")
    SIGNUP_PASSWORD = (By.ID, "sign-password")
    SIGNUP_BUTTON = (By.XPATH, "//button[text()='Sign up']")

    # =========================================================
    # ACTION METHODS
    # =========================================================

    def open_login_modal(self):
        """Click 'Log in' link in navigation to open login modal"""

        logger.info("Opening login modal")

        self.click_element(self.LOGIN_NAV_LINK)

        self.hard_wait(1)  # Wait for modal animation

    def enter_username(self, username):
        """Enter username in login form"""

        logger.info(f"Entering username: {username}")

        self.enter_text(self.LOGIN_USERNAME, username)

    def enter_password(self, password):
        """Enter password in login form"""

        logger.info("Entering password")

        self.enter_text(self.LOGIN_PASSWORD, password)

    def click_login_button(self):
        """Click 'Log in' button in modal"""

        logger.info("Clicking login button")

        self.click_element(self.LOGIN_BUTTON)

    def login(self, username, password):
        """
        Complete login flow:
        1. Open login modal
        2. Enter username
        3. Enter password
        4. Click login button
        5. Wait for login to complete
        """

        logger.info(f"Performing login with user: {username}")

        self.open_login_modal()

        self.enter_username(username)

        self.enter_password(password)

        self.click_login_button()

        self.hard_wait(2)  # Wait for login process

    def logout(self):
        """Click logout link in navigation"""

        logger.info("Performing logout")

        self.click_element(self.LOGOUT_NAV_LINK)

        # Wait for logout link to disappear (indicates logout is complete)
        self.wait_for_element_hidden(self.LOGOUT_NAV_LINK, timeout=10)

        logger.info("Logout successful")

    def close_login_modal(self):
        """Close login modal using Close button"""

        logger.info("Closing login modal")

        self.click_element(self.LOGIN_CLOSE_BUTTON)

    # =========================================================
    # VALIDATION METHODS
    # =========================================================

    def get_welcome_message(self):
        """Get welcome message text after login (e.g., 'Welcome pavanol')"""

        logger.info("Getting welcome message")

        self.hard_wait(2)

        return self.get_text(self.WELCOME_USER)

    def is_user_logged_in(self):
        """Check if user is logged in by checking welcome message visibility"""

        logger.info("Checking if user is logged in")

        return self.is_element_visible(
            self.WELCOME_USER,
            timeout=5
        )

    def is_logout_visible(self):
        """Check if logout link is visible (user is logged in)"""

        return self.is_element_visible(
            self.LOGOUT_NAV_LINK,
            timeout=5
        )

    def is_login_link_visible(self):
        """Check if login link is visible (user is logged out)"""

        return self.is_element_visible(
            self.LOGIN_NAV_LINK,
            timeout=5
        )

    def get_alert_message(self):
        """Get alert message text (for invalid login attempts)"""

        logger.info("Getting alert message")

        try:
            alert_text = self.accept_alert(timeout=5)

            return alert_text

        except Exception:

            logger.warning("No alert present")

            return ""

    # =========================================================
    # SIGNUP METHODS
    # =========================================================

    def open_signup_modal(self):
        """Open signup modal"""

        logger.info("Opening signup modal")

        self.click_element(self.SIGNUP_NAV_LINK)

        self.hard_wait(1)

    def signup(self, username, password):
        """Complete signup flow"""

        logger.info(f"Performing signup with user: {username}")

        self.open_signup_modal()

        self.enter_text(self.SIGNUP_USERNAME, username)

        self.enter_text(self.SIGNUP_PASSWORD, password)

        self.click_element(self.SIGNUP_BUTTON)

        self.hard_wait(2)