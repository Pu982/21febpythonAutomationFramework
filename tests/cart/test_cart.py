# =========================================================
# Cart Tests - TC008, TC009
# =========================================================
import os
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
    "product_data.json"
)

with open(DATA_PATH, "r") as f:
    PRODUCT_DATA = json.load(f)


@allure.feature("Cart")
@allure.story("Cart Management")
class TestCart:

    @pytest.mark.regression
    @pytest.mark.cart
    @allure.title("TC008 - Remove product from cart")
    @allure.severity(allure.severity_level.CRITICAL)

    def test_remove_product_from_cart(
        self,
        driver,
        home_page,
        product_page,
        cart_page
    ):

        logger.info("TC008: Remove Product from Cart Test")

        product_name = PRODUCT_DATA["singleProduct"]

        home_page.select_product_by_name(product_name)

        product_page.add_to_cart()

        driver.get("https://demoblaze.com/cart.html")

        cart_page.hard_wait(2)

        items_before = cart_page.get_cart_item_count()

        logger.info(
            f"Cart items before delete: {items_before}"
        )

        cart_page.delete_first_item()

        cart_page.hard_wait(2)

        items_after = cart_page.get_cart_item_count()

        assert items_after < items_before, (
            "Cart should have fewer items after delete"
        )

        logger.info(
            f"TC008 PASSED - "
            f"Item removed successfully. "
            f"Before: {items_before}, "
            f"After: {items_after}"
        )

    @pytest.mark.regression
    @pytest.mark.cart
    @allure.title("TC009 - Verify cart total price")
    @allure.severity(allure.severity_level.CRITICAL)

    def test_verify_cart_total(
        self,
        driver,
        home_page,
        product_page,
        cart_page
    ):

        logger.info("TC009: Verify Cart Total Test")

        products = PRODUCT_DATA["multipleProducts"][:2]

        for product_name in products:

            home_page.select_product_by_name(product_name)

            product_page.add_to_cart()

            product_page.navigate_to_home()

            home_page.hard_wait(1)

        driver.get("https://demoblaze.com/cart.html")

        cart_page.hard_wait(2)

        total = cart_page.get_total_price()

        logger.info(f"Cart total: {total}")

        assert total > 0, (
            "Cart total should be greater than 0"
        )

        prices = cart_page.get_cart_prices()

        price_sum = sum(
            int(price)
            for price in prices
            if price.isdigit()
        )

        logger.info(
            f"Sum of prices: {price_sum}, "
            f"Displayed total: {total}"
        )

        assert total == price_sum, (
            f"Total ({total}) should match "
            f"sum of prices ({price_sum})"
        )

        logger.info(
            "TC009 PASSED - Cart total verified successfully"
        )