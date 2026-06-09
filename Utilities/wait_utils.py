# =========================================================
# Wait Utilities
# =========================================================

import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

logger = logging.getLogger(__name__)


class WaitUtils:

    def __init__(self, driver, default_timeout=15):
        self.driver = driver
        self.timeout = default_timeout

    # =====================================================
    # WAIT FOR ELEMENT VISIBLE
    # =====================================================

    def wait_for_element_visible(self, locator, timeout=None):
        t = timeout or self.timeout
        logger.info(f"Waiting {t}s for element visible: {locator}")

        try:
            return WebDriverWait(self.driver, t).until(
                EC.visibility_of_element_located(locator)
            )

        except TimeoutException:
            logger.error(f"Element not visible after {t}s: {locator}")
            raise

    # =====================================================
    # WAIT FOR ELEMENT CLICKABLE
    # =====================================================

    def wait_for_element_clickable(self, locator, timeout=None):
        t = timeout or self.timeout
        logger.info(f"Waiting {t}s for element clickable: {locator}")

        try:
            return WebDriverWait(self.driver, t).until(
                EC.element_to_be_clickable(locator)
            )

        except TimeoutException:
            logger.error(f"Element not clickable after {t}s: {locator}")
            raise

    # =====================================================
    # WAIT FOR ELEMENT PRESENT
    # =====================================================

    def wait_for_element_present(self, locator, timeout=None):
        t = timeout or self.timeout
        logger.info(f"Waiting {t}s for element present: {locator}")

        try:
            return WebDriverWait(self.driver, t).until(
                EC.presence_of_element_located(locator)
            )

        except TimeoutException:
            logger.error(f"Element not present after {t}s: {locator}")
            raise

    # =====================================================
    # WAIT FOR ELEMENT INVISIBLE
    # =====================================================

    def wait_for_element_invisible(self, locator, timeout=None):
        t = timeout or self.timeout
        logger.info(f"Waiting {t}s for element invisible: {locator}")

        try:
            return WebDriverWait(self.driver, t).until(
                EC.invisibility_of_element_located(locator)
            )

        except TimeoutException:
            logger.error(f"Element still visible after {t}s: {locator}")
            raise

    # =====================================================
    # WAIT FOR TEXT IN ELEMENT
    # =====================================================

    def wait_for_text_in_element(self, locator, text, timeout=None):
        t = timeout or self.timeout
        logger.info(f"Waiting {t}s for text '{text}' in element: {locator}")

        try:
            return WebDriverWait(self.driver, t).until(
                EC.text_to_be_present_in_element(locator, text)
            )

        except TimeoutException:
            logger.error(f"Text '{text}' not found after {t}s")
            raise

    # =====================================================
    # WAIT FOR URL CONTAINS
    # =====================================================

    def wait_for_url_contains(self, url_part, timeout=None):
        t = timeout or self.timeout
        logger.info(f"Waiting {t}s for URL to contain: {url_part}")

        try:
            return WebDriverWait(self.driver, t).until(
                EC.url_contains(url_part)
            )

        except TimeoutException:
            logger.error(f"URL did not contain '{url_part}' after {t}s")
            raise

    # =====================================================
    # WAIT FOR TITLE CONTAINS
    # =====================================================

    def wait_for_title_contains(self, title_part, timeout=None):
        t = timeout or self.timeout
        logger.info(f"Waiting {t}s for title to contain: {title_part}")

        try:
            return WebDriverWait(self.driver, t).until(
                EC.title_contains(title_part)
            )

        except TimeoutException:
            logger.error(f"Title did not contain '{title_part}' after {t}s")
            raise

    # =====================================================
    # WAIT FOR PAGE LOAD
    # =====================================================

    def wait_for_page_load(self, timeout=None):
        t = timeout or self.timeout
        logger.info(f"Waiting {t}s for page load")

        WebDriverWait(self.driver, t).until(
            lambda d: d.execute_script(
                "return document.readyState"
            ) == "complete"
        )

        logger.info("Page loaded")

    # =====================================================
    # WAIT FOR ALERT
    # =====================================================

    def wait_for_alert(self, timeout=None):
        t = timeout or self.timeout
        logger.info(f"Waiting {t}s for alert")

        try:
            return WebDriverWait(self.driver, t).until(
                EC.alert_is_present()
            )

        except TimeoutException:
            logger.error(f"Alert not present after {t}s")
            raise

    # =====================================================
    # WAIT FOR NEW WINDOW
    # =====================================================

    def wait_for_new_window(self, current_handles, timeout=None):
        t = timeout or self.timeout
        logger.info(f"Waiting {t}s for new window")

        try:
            return WebDriverWait(self.driver, t).until(
                EC.new_window_is_opened(current_handles)
            )

        except TimeoutException:
            logger.error(f"No new window after {t}s")
            raise