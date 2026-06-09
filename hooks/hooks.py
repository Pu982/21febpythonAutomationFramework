# =========================================================
# Hooks - Additional Pytest Hooks
# =========================================================
#
# Main hooks are in conftest.py (pytest_runtest_makereport).
# This file has supplementary hook functions.
#
# =========================================================

import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class Hooks:
    """
    Supplementary hook utilities.

    Main pytest hooks are in conftest.py.
    These are helper functions that can be called
    from conftest hooks.
    """

    @staticmethod
    def before_test(test_name):
        """Log before test starts"""

        logger.info("=" * 60)

        logger.info(f"STARTING TEST: {test_name}")

        logger.info(
            f"Start Time: "
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )

        logger.info("=" * 60)

    @staticmethod
    def after_test(test_name, status):
        """Log after test ends"""

        logger.info("=" * 60)

        logger.info(
            f"FINISHED TEST: {test_name} - Status: {status}"
        )

        logger.info(
            f"End Time: "
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )

        logger.info("=" * 60)

    @staticmethod
    def before_suite():
        """Log before test suite starts"""

        logger.info("=" * 60)

        logger.info("TEST SUITE EXECUTION STARTED")

        logger.info(
            f"Start Time: "
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )

        logger.info("=" * 60)

    @staticmethod
    def after_suite():
        """Log after test suite ends"""

        logger.info("=" * 60)

        logger.info("TEST SUITE EXECUTION COMPLETED")

        logger.info(
            f"End Time: "
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )

        logger.info("=" * 60)