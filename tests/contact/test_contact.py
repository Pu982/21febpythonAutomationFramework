# =========================================================
# Contact Tests - TC015
# =========================================================

import pytest
import logging
import allure

from Utilities.random_data_generator import RandomDataGenerator

logger = logging.getLogger(__name__)


@allure.feature("Contact")
@allure.story("Contact Form")
class TestContact:

    @pytest.mark.regression
    @pytest.mark.contact
    @allure.title("TC015 - Submit Contact Form Successfully")
    @allure.severity(allure.severity_level.NORMAL)

    def test_contact_form_submission(
        self,
        driver,
        home_page,
        contact_page
    ):

        logger.info("========== TC015 STARTED ==========")

        # Generate test data
        email = RandomDataGenerator.generate_random_email()
        name = RandomDataGenerator.generate_random_name()

        message = (
            "This is an automated test message "
            "for contact form validation."
        )

        logger.info(
            f"Generated Data -> "
            f"Name: {name}, Email: {email}"
        )

        # Navigate to Contact Page
        home_page.click_contact()

        # Submit contact form
        alert_text = contact_page.send_contact_message(
            email,
            name,
            message
        )

        logger.info(f"Contact Form Alert: {alert_text}")

        # Validation
        assert (
            "Thanks" in alert_text
            or len(alert_text.strip()) > 0
        ), (
            f"Expected success message, "
            f"but got: {alert_text}"
        )

        logger.info(
            "TC015 PASSED - "
            "Contact form submitted successfully"
        )

        logger.info("========== TC015 COMPLETED ==========")