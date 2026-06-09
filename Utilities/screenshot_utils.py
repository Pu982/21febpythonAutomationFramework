# =========================================================
# Screenshot Utility
# =========================================================
import os
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class ScreenshotUtil:
    SCREENSHOTS_DIR = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "screenshots"
    )

    @staticmethod
    def capture_screenshot(driver, name="screenshot"):
        os.makedirs(ScreenshotUtil.SCREENSHOTS_DIR, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        clean_name = "".join(
            c if c.isalnum() or c in "_-"
            else "_"
            for c in name
        )

        filename = f"{clean_name}_{timestamp}.png"

        filepath = os.path.join(
            ScreenshotUtil.SCREENSHOTS_DIR,
            filename
        )

        try:
            driver.save_screenshot(filepath)

            logger.info(f"Screenshot saved: {filepath}")

            return filepath

        except Exception as e:
            logger.error(f"Failed to capture screenshot: {e}")

            return None

    @staticmethod
    def capture_element_screenshot(driver, locator, name="element"):
        os.makedirs(ScreenshotUtil.SCREENSHOTS_DIR, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png"

        filepath = os.path.join(
            ScreenshotUtil.SCREENSHOTS_DIR,
            filename
        )

        try:
            element = driver.find_element(*locator)

            element.screenshot(filepath)

            logger.info(f"Element screenshot saved: {filepath}")

            return filepath

        except Exception as e:
            logger.error(f"Failed to capture element screenshot: {e}")

            return None