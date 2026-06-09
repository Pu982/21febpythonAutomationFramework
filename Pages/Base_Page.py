# BasePage - Reusable Generic Methods for All Page Objects
# =========================================================
# This is the MOST IMPORTANT file in POM framework.
# Every page object class extends BasePage to inherit common methods.
# Contains 25+ reusable methods - click, type, wait, scroll, etc.
# =========================================================
from selenium import webdriver
import time 
import os 
import logging
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    TimeoutException,NoSuchElementException,ElementNotInteractableException,StaleElementReferenceException
)
logger = logging.getLogger(__name__)
import pytest

class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,15)
#navigation method
    def navigation_to(self,url):
        self.driver.get(url)
    def get_current_url(self,url):
        url=self.driver.current_url  
        return url
    def get_page_title(self):
        title=self.driver.title
        return title
# go back
# go forward
# refresh 
# click_element
# enterText
# clear 
# get_text
# pass_text
# pass_key
# waitforElement 
# is_element_displayed


    # Browser navigation
    def go_back(self):
        self.driver.back()

    def go_forward(self):
        self.driver.forward()

    def refresh(self):
        self.driver.refresh()

    # Element interactions
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator, text):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.send_keys(text)

    def clear(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()

    def get_text(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.text

    def pass_text(self, locator, text):
        # Similar to enter_text but ensures clearing first
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def pass_key(self, locator, key):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.send_keys(key)

    def wait_for_element(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return None

    def is_element_displayed(self, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element.is_displayed()
        except TimeoutException:
            return False
    
    # =========================================================
    # ELEMENT INTERACTION METHODS
    # =========================================================

    def click_element(self, locator, timeout=15):
        """Click on an element after waiting for it to be clickable"""
        logger.info(f"Clicking element: {locator}")
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
            logger.info(f"Clicked element: {locator}")
        except TimeoutException:
            logger.error(f"Element not clickable: {locator}")
            raise

    def enter_text(self, locator, text, timeout=15):
        """Enter text into an input field after clearing it"""
        logger.info(f"Entering text '{text}' into: {locator}")
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            element.clear()
            element.send_keys(text)
            logger.info(f"Text entered successfully: {locator}")
        except TimeoutException:
            logger.error(f"Element not visible for text entry: {locator}")
            raise

    def clear_and_type(self, locator, text, timeout=15):
        """Clear field completely using keyboard shortcuts, then type"""
        logger.info(f"Clear and type '{text}' into: {locator}")
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(text)

    def get_text(self, locator, timeout=15):
        """Get visible text content of an element"""
        logger.info(f"Getting text from: {locator}")
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            text = element.text
            logger.info(f"Text found: '{text}'")
            return text
        except TimeoutException:
            logger.error(f"Element not visible: {locator}")
            raise

    def get_attribute(self, locator, attribute, timeout=15):
        """Get attribute value of an element"""
        logger.info(f"Getting attribute '{attribute}' from: {locator}")
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        value = element.get_attribute(attribute)
        logger.info(f"Attribute value: '{value}'")
        return value

    def press_key(self, key):
        """Press a keyboard key using ActionChains"""
        logger.info(f"Pressing key: {key}")
        self.actions.send_keys(key).perform()

    # =========================================================
    # WAIT METHODS
    # =========================================================

    def wait_for_element(self, locator, timeout=15):
        """Wait for element to be visible on page"""
        logger.info(f"Waiting for element: {locator}")
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            logger.info(f"Element visible: {locator}")
            return element
        except TimeoutException:
            logger.error(f"Element not found within {timeout}s: {locator}")
            raise

    def wait_for_element_hidden(self, locator, timeout=15):
        """Wait for element to disappear from page"""
        logger.info(f"Waiting for element to hide: {locator}")
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            logger.info(f"Element hidden: {locator}")
        except TimeoutException:
            logger.error(f"Element still visible after {timeout}s: {locator}")
            raise

    def wait_for_element_clickable(self, locator, timeout=15):
        """Wait for element to be clickable"""
        logger.info(f"Waiting for element clickable: {locator}")
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_page_load(self, timeout=30):
        """Wait for page to fully load (document.readyState == complete)"""
        logger.info("Waiting for page load complete")
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        logger.info("Page loaded successfully")

    def wait_for_url_contains(self, text, timeout=15):
        """Wait until URL contains specific text"""
        logger.info(f"Waiting for URL to contain: {text}")
        WebDriverWait(self.driver, timeout).until(EC.url_contains(text))

    def wait_for_alert(self, timeout=10):
        """Wait for browser alert to appear"""
        logger.info("Waiting for alert")
        return WebDriverWait(self.driver, timeout).until(EC.alert_is_present())

    def hard_wait(self, seconds):
        """Hard wait - use sparingly, prefer explicit waits"""
        logger.warning(f"Hard wait: {seconds} seconds (avoid in production code)")
        time.sleep(seconds)

    # =========================================================
    # ELEMENT STATE CHECK METHODS
    # =========================================================

    def is_element_visible(self, locator, timeout=5):
        """Check if element is visible on page"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            logger.info(f"Element is visible: {locator}")
            return True
        except TimeoutException:
            logger.info(f"Element is NOT visible: {locator}")
            return False

    def is_element_enabled(self, locator, timeout=5):
        """Check if element is enabled (interactable)"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            enabled = element.is_enabled()
            logger.info(f"Element enabled({enabled}): {locator}")
            return enabled
        except TimeoutException:
            logger.info(f"Element not found: {locator}")
            return False

    def is_element_selected(self, locator, timeout=5):
        """Check if element (checkbox/radio) is selected"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element.is_selected()
        except TimeoutException:
            return False

    def get_element_count(self, locator):
        """Get count of elements matching a locator"""
        elements = self.driver.find_elements(*locator)
        count = len(elements)
        logger.info(f"Element count for {locator}: {count}")
        return count

    # =========================================================
    # DROPDOWN METHODS
    # =========================================================

    def select_dropdown_by_value(self, locator, value, timeout=15):
        """Select dropdown option by value attribute"""
        logger.info(f"Selecting dropdown value '{value}' from: {locator}")
        element = self.wait_for_element(locator, timeout)
        select = Select(element)
        select.select_by_value(value)

    def select_dropdown_by_text(self, locator, text, timeout=15):
        """Select dropdown option by visible text"""
        logger.info(f"Selecting dropdown text '{text}' from: {locator}")
        element = self.wait_for_element(locator, timeout)
        select = Select(element)
        select.select_by_visible_text(text)

    def select_dropdown_by_index(self, locator, index, timeout=15):
        """Select dropdown option by index"""
        logger.info(f"Selecting dropdown index {index} from: {locator}")
        element = self.wait_for_element(locator, timeout)
        select = Select(element)
        select.select_by_index(index)

    # =========================================================
    # ADVANCED INTERACTION METHODS
    # =========================================================

    def scroll_to_element(self, locator, timeout=15):
        """Scroll page until element is in view"""
        logger.info(f"Scrolling to element: {locator}")
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            element
        )

    def hover_element(self, locator, timeout=15):
        """Mouse hover over an element"""
        logger.info(f"Hovering over element: {locator}")
        element = self.wait_for_element(locator, timeout)
        ActionChains(self.driver).move_to_element(element).perform()

    def double_click(self, locator, timeout=15):
        """Double click on an element"""
        logger.info(f"Double clicking: {locator}")
        element = self.wait_for_element(locator, timeout)
        ActionChains(self.driver).double_click(element).perform()

    def right_click(self, locator, timeout=15):
        """Right click (context click) on an element"""
        logger.info(f"Right clicking: {locator}")
        element = self.wait_for_element(locator, timeout)
        ActionChains(self.driver).context_click(element).perform()

    def drag_and_drop(self, source_locator, target_locator, timeout=15):
        """Drag element from source and drop on target"""
        logger.info(f"Drag from {source_locator} to {target_locator}")
        source = self.wait_for_element(source_locator, timeout)
        target = self.wait_for_element(target_locator, timeout)
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    def upload_file(self, locator, file_path, timeout=15):
        """Upload file using file input element"""
        logger.info(f"Uploading file: {file_path}")
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        element.send_keys(os.path.abspath(file_path))
        logger.info("File uploaded successfully")

    # =========================================================
    # ALERT HANDLING METHODS
    # =========================================================

    def accept_alert(self, timeout=10):
        """Accept (OK) browser alert"""
        logger.info("Accepting alert")
        alert = self.wait_for_alert(timeout)
        text = alert.text
        alert.accept()
        logger.info(f"Alert accepted. Text was: '{text}'")
        return text

    def dismiss_alert(self, timeout=10):
        """Dismiss (Cancel) browser alert"""
        logger.info("Dismissing alert")
        alert = self.wait_for_alert(timeout)
        text = alert.text
        alert.dismiss()
        logger.info(f"Alert dismissed. Text was: '{text}'")
        return text

    def get_alert_text(self, timeout=10):
        """Get text from browser alert"""
        alert = self.wait_for_alert(timeout)
        return alert.text

    # =========================================================
    # SCREENSHOT METHOD
    # =========================================================

    def take_screenshot(self, name="screenshot"):
        """Capture full page screenshot with timestamp"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshots_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "screenshots"
        )
        os.makedirs(screenshots_dir, exist_ok=True)

        filepath = os.path.join(
            screenshots_dir,
            f"{name}_{timestamp}.png"
        )

        self.driver.save_screenshot(filepath)
        logger.info(f"Screenshot saved: {filepath}")
        return filepath

    # =========================================================
    # JAVASCRIPT EXECUTION METHODS
    # =========================================================

    def execute_js(self, script, *args):
        """Execute JavaScript on current page"""
        logger.info(f"Executing JS: {script[:80]}")
        return self.driver.execute_script(script, *args)

    def js_click(self, locator, timeout=15):
        """Click element using JavaScript (for stubborn elements)"""
        logger.info(f"JS clicking: {locator}")
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_to_top(self):
        """Scroll page to top"""
        self.driver.execute_script("window.scrollTo(0, 0);")

    def scroll_to_bottom(self):
        """Scroll page to bottom"""
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

    # =========================================================
    # FRAME / WINDOW METHODS
    # =========================================================

    def switch_to_frame(self, locator, timeout=15):
        """Switch to iframe"""
        logger.info(f"Switching to frame: {locator}")
        WebDriverWait(self.driver, timeout).until(
            EC.frame_to_be_available_and_switch_to_it(locator)
        )

    def switch_to_default_content(self):
        """Switch back to main page from iframe"""
        logger.info("Switching to default content")
        self.driver.switch_to.default_content()

    def switch_to_window(self, index):
        """Switch to browser window by index"""
        windows = self.driver.window_handles
        logger.info(f"Switching to window index {index} (total: {len(windows)})")
        self.driver.switch_to.window(windows[index])

    def get_window_count(self):
        """Get number of open browser windows/tabs"""
        return len(self.driver.window_handles)

    # =========================================================
    # UTILITY METHODS
    # =========================================================

    def generate_random_number(self, min_val=1000, max_val=9999):
        """Generate a random number between min and max"""
        import random
        num = random.randint(min_val, max_val)
        logger.info(f"Generated random number: {num}")
        return num

    def generate_unique_name(self, prefix="test"):
        """Generate unique name with timestamp"""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        name = f"{prefix}_{timestamp}"
        logger.info(f"Generated unique name: {name}")
        return name