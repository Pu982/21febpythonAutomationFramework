# =========================================================
# Test Fixtures - Additional Custom Fixtures
# =========================================================
#
# Contains specialized fixtures for data loading, etc.
# Main fixtures are in conftest.py; this has extras.
#
# =========================================================

import os
import json
import pytest
import logging

logger = logging.getLogger(__name__)

# =========================================================
# TEST DATA FIXTURES
# =========================================================

@pytest.fixture(scope="session")
def login_data():
    """
    Load login test data from JSON file
    (session scope - loaded once)
    """

    data_path = os.path.join(
        os.path.dirname(
            os.path.dirname(__file__)
        ),
        "testdata",
        "login_data.json"
    )

    logger.info(f"Loading login data from: {data_path}")

    with open(data_path, "r") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def product_data():
    """
    Load product test data from JSON file
    """

    data_path = os.path.join(
        os.path.dirname(
            os.path.dirname(__file__)
        ),
        "testdata",
        "product_data.json"
    )

    logger.info(f"Loading product data from: {data_path}")

    with open(data_path, "r") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def checkout_data():
    """
    Load checkout test data from JSON file
    """

    data_path = os.path.join(
        os.path.dirname(
            os.path.dirname(__file__)
        ),
        "testdata",
        "checkout_data.json"
    )

    logger.info(f"Loading checkout data from: {data_path}")

    with open(data_path, "r") as f:
        return json.load(f)