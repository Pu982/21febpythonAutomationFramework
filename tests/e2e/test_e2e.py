# =========================================================
# E2E Tests - TC014, TC016 to TC020
# =========================================================
import os
import json
import pytest
import logging
import allure
import requests

from selenium.webdriver.common.by import By
from Utilities.random_data_generator import RandomDataGenerator

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

LOGIN_DATA_PATH = os.path.join(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(__file__)
        )
    ),
    "testdata",
    "login_data.json"
)

with open(PRODUCT_DATA_PATH, "r") as f:
    PRODUCT_DATA = json.load(f)

with open(CHECKOUT_DATA_PATH, "r") as f:
    CHECKOUT_DATA = json.load(f)

with open(LOGIN_DATA_PATH, "r") as f:
    LOGIN_DATA = json.load(f)


@allure.feature("E2E")
@allure.story("End-to-End Workflows")
class TestE2E:

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.e2e
    @allure.title(
        "TC014 - Verify navigation menu links"
    )
    @allure.severity(
        allure.severity_level.NORMAL
    )

    def test_verify_navigation_menu(
        self,
        driver,
        home_page
    ):

        logger.info(
            "TC014: Verify Navigation Menu Test"
        )

        assert home_page.verify_navigation_menu(), \
            "Navigation menu should be visible"

        assert home_page.is_home_page_loaded(), \
            "Home page should be loaded"

        logger.info(
            "TC014: PASSED - Navigation menu verified"
        )

    @pytest.mark.regression
    @pytest.mark.e2e
    @allure.title(
        "TC016 - Validate no broken links on home page"
    )
    @allure.severity(
        allure.severity_level.NORMAL
    )

    def test_broken_links(
        self,
        driver
    ):

        logger.info(
            "TC016: Broken Link Validation Test"
        )

        links = driver.find_elements(
            By.TAG_NAME,
            "a"
        )

        hrefs = [
            link.get_attribute("href")
            for link in links
            if link.get_attribute("href")
        ]

        unique_urls = list(
            set(
                url for url in hrefs
                if url.startswith("http")
            )
        )

        broken_links = []

        for url in unique_urls[:20]:

            try:
                response = requests.head(
                    url,
                    timeout=10,
                    allow_redirects=True
                )

                if response.status_code >= 400:

                    broken_links.append({
                        "url": url,
                        "status": response.status_code
                    })

                    logger.warning(
                        f"Broken link: {url} "
                        f"- Status: {response.status_code}"
                    )

            except requests.exceptions.RequestException as e:

                broken_links.append({
                    "url": url,
                    "error": str(e)
                })

                logger.warning(
                    f"Link error: {url} - {e}"
                )

        logger.info(
            f"Total links checked: {len(unique_urls[:20])}, "
            f"broken: {len(broken_links)}"
        )

        assert len(broken_links) == 0, \
            f"Found broken links: {broken_links}"

        logger.info(
            "TC016: PASSED - No broken links found"
        )

    @pytest.mark.regression
    @pytest.mark.e2e
    @allure.title(
        "TC017 - Browse and find product by category"
    )
    @allure.severity(
        allure.severity_level.NORMAL
    )

    def test_search_product(
        self,
        driver,
        home_page
    ):

        logger.info(
            "TC017: Search/Browse Product Test"
        )

        home_page.select_phones_category()

        products = home_page.get_all_product_names()

        logger.info(
            f"Phone products: {products}"
        )

        assert len(products) > 0, \
            "Should find products in Phones category"

        target = PRODUCT_DATA["singleProduct"]

        assert home_page.is_product_displayed(target), \
            f"Product '{target}' should be displayed"

        logger.info(
            f"TC017: PASSED - "
            f"Product '{target}' found in category"
        )

    @pytest.mark.smoke
    @pytest.mark.e2e
    @allure.title(
        "TC018 - Cross browser - verify home page loads"
    )
    @allure.severity(
        allure.severity_level.CRITICAL
    )

    def test_cross_browser(
        self,
        driver,
        home_page
    ):

        logger.info(
            "TC018: Cross Browser Test"
        )

        assert home_page.is_home_page_loaded(), \
            "Home page should load"

        title = home_page.get_page_title()

        logger.info(
            f"Page title: {title}"
        )

        assert "STORE" in title.upper(), \
            f"Title should contain 'STORE', got: {title}"

        assert home_page.verify_categories_displayed(), \
            "Categories should be visible"

        logger.info(
            "TC018: PASSED - "
            "Cross browser verification complete"
        )

    @pytest.mark.e2e
    @allure.title(
        "TC019 - Parallel execution - independent test"
    )
    @allure.severity(
        allure.severity_level.NORMAL
    )

    def test_parallel_execution(
        self,
        driver,
        home_page
    ):

        logger.info(
            "TC019: Parallel Execution Test"
        )

        assert home_page.is_home_page_loaded(), \
            "Home page loaded"

        home_page.select_laptops_category()

        products = home_page.get_all_product_names()

        assert len(products) > 0, \
            "Laptops should have products"

        logger.info(
            f"TC019: PASSED - "
            f"{len(products)} laptop products found"
        )

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.e2e
    @allure.title(
        "TC020 - Full E2E purchase flow: "
        "Login + Browse + Cart + Checkout"
    )
    @allure.severity(
        allure.severity_level.BLOCKER
    )

    def test_full_e2e_purchase(
        self,
        driver,
        login_page,
        home_page,
        product_page,
        cart_page,
        checkout_page
    ):

        logger.info(
            "TC020: Full E2E Purchase Flow"
        )

        user = LOGIN_DATA["validUser"]

        login_page.login(
            user["username"],
            user["password"]
        )

        assert login_page.is_user_logged_in(), \
            "Login should succeed"

        logger.info(
            "Step 1: Login - DONE"
        )

        home_page.select_phones_category()

        home_page.hard_wait(1)

        logger.info(
            "Step 2: Browse products - DONE"
        )

        product_name = PRODUCT_DATA["singleProduct"]

        home_page.select_product_by_name(
            product_name
        )

        logger.info(
            f"Step 3: Selected product "
            f"'{product_name}' - DONE"
        )

        product_page.add_to_cart()

        logger.info(
            "Step 4: Added to cart - DONE"
        )

        driver.get(
            "https://demoblaze.com/cart.html"
        )

        cart_page.hard_wait(2)

        logger.info(
            "Step 5: Navigated to cart - DONE"
        )

        assert cart_page.is_product_in_cart(
            product_name
        ), f"'{product_name}' should be in cart"

        total = cart_page.get_total_price()

        assert total > 0, \
            "Cart total should be > 0"

        logger.info(
            f"Step 6: Cart verified - "
            f"Total: {total} - DONE"
        )

        cart_page.click_place_order()

        logger.info(
            "Step 7: Place order clicked - DONE"
        )

        checkout = CHECKOUT_DATA["validCheckout"]

        checkout_page.complete_purchase(
            checkout["name"],
            checkout["country"],
            checkout["city"],
            checkout["card"],
            checkout["month"],
            checkout["year"]
        )

        logger.info(
            "Step 8-9: Checkout completed - DONE"
        )

        assert checkout_page.is_order_confirmed(), \
            "Order should be confirmed"

        confirmation = \
            checkout_page.get_confirmation_title()

        assert "Thank you" in confirmation, \
            f"Expected 'Thank you', got: {confirmation}"

        checkout_page.click_confirmation_ok()

        logger.info(
            "Step 10: Order confirmed - DONE"
        )

        login_page.hard_wait(1)

        login_page.logout()

        assert login_page.is_login_link_visible(), \
            "Should be logged out"

        logger.info(
            "Step 11: Logout - DONE"
        )