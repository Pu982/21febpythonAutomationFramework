# =========================================================
# Login Tests - TC001 to TC005
# =========================================================
import os
import sys
import json
import pytest
import logging
import allure

logger = logging.getLogger(__name__)

DATA_PATH = os.path.join(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(__file__)
        )
    ),
    "testdata",
    "login_data.json"
)

with open(DATA_PATH, "r") as f:
    LOGIN_DATA = json.load(f)


@allure.feature("Login")
@allure.story("Authentication")
class TestLogin:

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.login
    @allure.title(
        "TC001 - Valid login with correct credentials"
    )
    @allure.severity(
        allure.severity_level.CRITICAL
    )

    def test_valid_login(
        self,
        driver,
        login_page
    ):

        logger.info(
            "TC001: Valid Login Test"
        )

        user = LOGIN_DATA["validUser"]

        login_page.login(
            user["username"],
            user["password"]
        )

        assert login_page.is_user_logged_in(), \
            "User should be logged in"

        welcome = login_page.get_welcome_message()

        assert user["username"] in welcome, \
            f"Welcome message should contain username, got: {welcome}"

        logger.info(
            "TC001: PASSED - Valid login successful"
        )

    # =========================================================
    # TC002: Invalid Login
    # =========================================================

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.login

    @allure.title(
        "TC002 - Invalid login with wrong credentials"
    )

    @allure.severity(
        allure.severity_level.CRITICAL
    )

    def test_invalid_login(
        self,
        driver,
        login_page
    ):

        logger.info(
            "TC002: Invalid Login Test"
        )

        user = LOGIN_DATA["invalidUser"]

        login_page.login(
            user["username"],
            user["password"]
        )

        alert_text = login_page.get_alert_message()

        assert (
            "Wrong password" in alert_text
            or "User does not exist" in alert_text
        ), f"Expected error alert, got: {alert_text}"

        logger.info(
            "TC002: PASSED - Invalid login shows error"
        )

    # =========================================================
    # TC003: Blank Username Login
    # =========================================================

    @pytest.mark.regression
    @pytest.mark.login

    @allure.title(
        "TC003 - Login with blank username"
    )

    @allure.severity(
        allure.severity_level.NORMAL
    )

    def test_blank_username(
        self,
        driver,
        login_page
    ):

        logger.info(
            "TC003: Blank Username Test"
        )

        user = LOGIN_DATA["blankUsername"]

        login_page.login(
            user["username"],
            user["password"]
        )

        alert_text = login_page.get_alert_message()

        assert (
            "fill out" in alert_text.lower()
            or "username" in alert_text.lower()
            or len(alert_text) > 0
        ), "Expected error for blank username"

        logger.info(
            "TC003: PASSED - Blank username shows error"
        )

    # =========================================================
    # TC004: Blank Password Login
    # =========================================================

    @pytest.mark.regression
    @pytest.mark.login

    @allure.title(
        "TC004 - Login with blank password"
    )

    @allure.severity(
        allure.severity_level.NORMAL
    )

    def test_blank_password(
        self,
        driver,
        login_page
    ):

        logger.info(
            "TC004: Blank Password Test"
        )

        user = LOGIN_DATA["blankPassword"]

        login_page.login(
            user["username"],
            user["password"]
        )

        alert_text = login_page.get_alert_message()

        assert (
            "fill out" in alert_text.lower()
            or "password" in alert_text.lower()
            or len(alert_text) > 0
        ), "Expected error for blank password"

        logger.info(
            "TC004: PASSED - Blank password shows error"
        )

    # =========================================================
    # TC005: Logout Validation
    # =========================================================

    @pytest.mark.smoke
    @pytest.mark.login

    @allure.title(
        "TC005 - Logout after successful login"
    )

    @allure.severity(
        allure.severity_level.CRITICAL
    )

    def test_logout(
        self,
        driver,
        login_page
    ):

        logger.info(
            "TC005: Logout Test"
        )

        user = LOGIN_DATA["validUser"]

        login_page.login(
            user["username"],
            user["password"]
        )

        assert login_page.is_user_logged_in(), \
            "Login should succeed"

        login_page.logout()

        assert login_page.is_login_link_visible(), \
            "Login link should be visible after logout"

        logger.info(
            "TC005: PASSED - Logout successful"
        )