# =========================================================
# Date Utilities - Date Formatting and Manipulation
# =========================================================

import logging
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


class DateUtils:
    """
    Utility class for date and time operations
    """

    # =========================================================
    # CURRENT DATE/TIME METHODS
    # =========================================================

    @staticmethod
    def get_current_date(format="%Y-%m-%d"):
        """
        Get current date

        Example:
        2026-05-20
        """
        date = datetime.now().strftime(format)

        logger.info(f"Current date: {date}")

        return date

    @staticmethod
    def get_current_datetime(
        format="%Y-%m-%d %H:%M:%S"
    ):
        """
        Get current date and time
        """
        dt = datetime.now().strftime(format)

        logger.info(f"Current datetime: {dt}")

        return dt

    @staticmethod
    def get_current_timestamp():
        """
        Get timestamp

        Example:
        20260520224530
        """
        timestamp = datetime.now().strftime(
            "%Y%m%d%H%M%S"
        )

        logger.info(f"Current timestamp: {timestamp}")

        return timestamp

    # =========================================================
    # DATE ADDITION METHODS
    # =========================================================

    @staticmethod
    def add_days(days, format="%Y-%m-%d"):
        """
        Add days to current date
        """
        new_date = (
            datetime.now() + timedelta(days=days)
        ).strftime(format)

        logger.info(f"Date after adding days: {new_date}")

        return new_date

    @staticmethod
    def subtract_days(days, format="%Y-%m-%d"):
        """
        Subtract days from current date
        """
        new_date = (
            datetime.now() - timedelta(days=days)
        ).strftime(format)

        logger.info(f"Date after subtracting days: {new_date}")

        return new_date

    @staticmethod
    def add_hours(hours,
                  format="%Y-%m-%d %H:%M:%S"):
        """
        Add hours to current datetime
        """
        new_time = (
            datetime.now() + timedelta(hours=hours)
        ).strftime(format)

        logger.info(f"Datetime after adding hours: {new_time}")

        return new_time

    @staticmethod
    def subtract_hours(hours,
                       format="%Y-%m-%d %H:%M:%S"):
        """
        Subtract hours from current datetime
        """
        new_time = (
            datetime.now() - timedelta(hours=hours)
        ).strftime(format)

        logger.info(f"Datetime after subtracting hours: {new_time}")

        return new_time

    # =========================================================
    # DATE CONVERSION METHODS
    # =========================================================

    @staticmethod
    def string_to_date(date_string,
                       format="%Y-%m-%d"):
        """
        Convert string to datetime object
        """
        date_obj = datetime.strptime(
            date_string,
            format
        )

        logger.info(f"Converted string to date: {date_obj}")

        return date_obj

    @staticmethod
    def date_to_string(date_obj,
                       format="%Y-%m-%d"):
        """
        Convert datetime object to string
        """
        date_string = date_obj.strftime(format)

        logger.info(f"Converted date to string: {date_string}")

        return date_string

    # =========================================================
    # DATE COMPARISON METHODS
    # =========================================================

    @staticmethod
    def compare_dates(date1,
                      date2,
                      format="%Y-%m-%d"):
        """
        Compare two dates

        Returns:
        1  -> date1 > date2
        0  -> equal
        -1 -> date1 < date2
        """

        d1 = datetime.strptime(date1, format)
        d2 = datetime.strptime(date2, format)

        if d1 > d2:
            return 1
        elif d1 < d2:
            return -1
        else:
            return 0

    @staticmethod
    def get_date_difference(date1,
                            date2,
                            format="%Y-%m-%d"):
        """
        Get difference between two dates
        """
        d1 = datetime.strptime(date1, format)
        d2 = datetime.strptime(date2, format)

        difference = abs((d2 - d1).days)

        logger.info(f"Date difference: {difference} days")

        return difference

    # =========================================================
    # VALIDATION METHODS
    # =========================================================

    @staticmethod
    def is_valid_date(date_string,
                      format="%Y-%m-%d"):
        """
        Validate date format
        """
        try:
            datetime.strptime(date_string, format)

            logger.info("Valid date format")

            return True

        except ValueError:

            logger.error("Invalid date format")

            return False

    # =========================================================
    # DAY / MONTH / YEAR METHODS
    # =========================================================

    @staticmethod
    def get_day():
        """
        Get current day
        """
        return datetime.now().day

    @staticmethod
    def get_month():
        """
        Get current month
        """
        return datetime.now().month

    @staticmethod
    def get_year():
        """
        Get current year
        """
        return datetime.now().year

    @staticmethod
    def get_weekday():
        """
        Get current weekday name
        """
        return datetime.now().strftime("%A")