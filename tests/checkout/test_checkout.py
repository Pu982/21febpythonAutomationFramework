# =========================================================
# Checkout Tests - TC010, TC011
# =========================================================
import os
import json
import pytest
import logging
import allure

logger = logging.getLogger(__name__)

PRODUCT_DATA_PATH = os.path.join(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(__file__)
        )
    ),
    "testdata",
    "product_data.json"
)

CHECKOUT_DATA_PATH = os.path.join(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(__file__)
        )
    ),
    "testdata",
    "checkout_data.json"
)

with open(PRODUCT_DATA_PATH, "r") as f:
    PRODUCT_DATA = json.load(f)

with open(CHECKOUT_DATA_PATH, "r") as f:
    CHECKOUT_DATA = json.load(f)


@allure.feature("Checkout")
@allure.story("Order Placement")
class TestCheckout:

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.checkout
    @allure.title("TC010 - Place order successfully")
    @allure.severity(allure.severity_level.BLOCKER)

    def test_place_order(
        self,
        driver,
        home_page,
        product_page,
        cart_page,
        checkout_page
    ):

        logger.info("TC010: Place Order Test")

        product_name = PRODUCT_DATA["singleProduct"]

        checkout = CHECKOUT_DATA["validCheckout"]

        home_page.select_product_by_name(product_name)

        product_page.add_to_cart()

        driver.get("https://demoblaze.com/cart.html")

        cart_page.hard_wait(2)

        cart_page.click_place_order()

        checkout_page.complete_purchase(
            checkout["name"],
            checkout["country"],
            checkout["city"],
            checkout["card"],
            checkout["month"],
            checkout["year"]
        )

        assert checkout_page.is_order_confirmed(), (
            "Order confirmation should be displayed"
        )

        title = checkout_page.get_confirmation_title()

        assert "Thank you" in title, (
            f"Expected 'Thank you' in confirmation, got: {title}"
        )

        checkout_page.click_confirmation_ok()

        logger.info(
            "TC010: PASSED - Order placed successfully"
        )

    @pytest.mark.regression
    @pytest.mark.checkout
    @allure.title("TC011 - Verify order confirmation details")
    @allure.severity(allure.severity_level.CRITICAL)

    def test_verify_order_confirmation(
        self,
        driver,
        home_page,
        product_page,
        cart_page,
        checkout_page
    ):

        logger.info(
            "TC011: Verify Order Confirmation Test"
        )

        product_name = PRODUCT_DATA["singleProduct"]

        checkout = CHECKOUT_DATA["validCheckout"]

        home_page.select_product_by_name(product_name)

        product_page.add_to_cart()

        driver.get("https://demoblaze.com/cart.html")

        cart_page.hard_wait(2)

        cart_page.click_place_order()

        checkout_page.complete_purchase(
            checkout["name"],
            checkout["country"],
            checkout["city"],
            checkout["card"],
            checkout["month"],
            checkout["year"]
        )

        assert checkout_page.is_order_confirmed(), (
            "Order should be confirmed"
        )

        details = checkout_page.get_confirmation_details()

        logger.info(
            f"Confirmation details: {details}"
        )

        assert checkout["card"][-4:] in details or \
               "Amount" in details, (
            "Confirmation should contain order details"
        )

        checkout_page.click_confirmation_ok()

        logger.info(
            "TC011: PASSED - "
            "Order confirmation details verified"
        )