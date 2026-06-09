# =========================================================
# Product Tests - TC006, TC007, TC012, TC013
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


@allure.feature("Product")
@allure.story("Product Management")
class TestProduct:

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.product
    @allure.title(
        "TC006 - Add single product to cart"
    )
    @allure.severity(
        allure.severity_level.CRITICAL
    )

    def test_add_single_product(
        self,
        driver,
        home_page,
        product_page
    ):

        logger.info(
            "TC006: Add Single Product Test"
        )

        product_name = PRODUCT_DATA["singleProduct"]

        home_page.select_product_by_name(
            product_name
        )

        alert_text = product_page.add_to_cart()

        assert "Product added" in alert_text, \
            f"Expected 'Product added' alert, got: {alert_text}"

        logger.info(
            "TC006: PASSED - Single product added to cart"
        )

    @pytest.mark.regression
    @pytest.mark.product
    @allure.title(
        "TC007 - Add multiple products to cart"
    )
    @allure.severity(
        allure.severity_level.CRITICAL
    )

    def test_add_multiple_products(
        self,
        driver,
        home_page,
        product_page
    ):

        logger.info(
            "TC007: Add Multiple Products Test"
        )

        products = PRODUCT_DATA["multipleProducts"]

        for product_name in products:

            home_page.select_product_by_name(
                product_name
            )

            product_page.add_to_cart()

            product_page.navigate_to_home()

            home_page.hard_wait(1)

        logger.info(
            f"TC007: PASSED - {len(products)} products added to cart"
        )

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.product
    @allure.title(
        "TC012 - Verify product categories are displayed"
    )
    @allure.severity(
        allure.severity_level.NORMAL
    )

    def test_verify_categories(
        self,
        driver,
        home_page
    ):

        logger.info(
            "TC012: Verify Categories Test"
        )

        assert home_page.verify_categories_displayed(), \
            "All 3 categories should be visible"

        home_page.select_phones_category()

        phone_count = home_page.get_product_count()

        assert phone_count > 0, \
            "Phones category should have products"

        logger.info(
            f"Phones: {phone_count} products"
        )

        home_page.select_laptops_category()

        laptop_count = home_page.get_product_count()

        assert laptop_count > 0, \
            "Laptops category should have products"

        logger.info(
            f"Laptops: {laptop_count} products"
        )

        home_page.select_monitors_category()

        monitor_count = home_page.get_product_count()

        assert monitor_count > 0, \
            "Monitors category should have products"

        logger.info(
            f"Monitors: {monitor_count} products"
        )

        logger.info("TC012: PASSED - All categories verified")

    @pytest.mark.regression
    @pytest.mark.product
    @allure.title(
        "TC013 - Verify product details page"
    )
    @allure.severity(
        allure.severity_level.NORMAL
    )

    def test_verify_product_details(self,driver,
        home_page,
        product_page
    ):

        logger.info("TC013: Verify Product Details Test")

        product_name = PRODUCT_DATA["singleProduct"]

        home_page.select_product_by_name(product_name )

        assert product_page.is_product_page_loaded(), "Product page should be loaded"

        title = product_page.get_product_title()

        assert len(title) > 0, "Product title should not be empty"

        logger.info(f"Product title: {title}" )

        price = product_page.get_product_price()

        assert len(price) > 0, "Product price should not be empty"

        logger.info(
            f"Product price: {price}")

        logger.info(
            "TC013: PASSED - Product details verified")