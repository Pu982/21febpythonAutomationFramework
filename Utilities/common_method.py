# =========================================================
# Common Methods - Shared Helper Functions
# =========================================================
import os
import re
import logging

logger = logging.getLogger(__name__)


class CommonMethods:

    @staticmethod
    def extract_number_from_text(text):

        logger.info(f"Extracting number from: {text}")

        numbers = re.findall(r'\d+', text)

        if numbers:
            result = int(numbers[0])

            logger.info(f"Extracted number: {result}")

            return result

        logger.warning(f"No number found in: {text}")

        return 0

    @staticmethod
    def extract_price(price_text):

        numbers = re.findall(
            r'\d+',
            price_text
        )

        return int(numbers[0]) if numbers else 0

    @staticmethod
    def create_directory(dir_path):

        os.makedirs(
            dir_path,
            exist_ok=True
        )

        logger.info(f"Directory ensured: {dir_path}")

    @staticmethod
    def file_exists(file_path):

        exists = os.path.exists(file_path)

        logger.info(
            f"File exists ({file_path}): {exists}"
        )

        return exists

    @staticmethod
    def get_project_root():

        return os.path.dirname(
            os.path.dirname(__file__)
        )

    @staticmethod
    def get_testdata_path(filename):

        root = os.path.dirname(
            os.path.dirname(__file__)
        )

        return os.path.join(
            root,
            "testdata",
            filename
        )

    @staticmethod
    def compare_lists(list1, list2):

        missing = [
            item for item in list1
            if item not in list2
        ]

        extra = [
            item for item in list2
            if item not in list1
        ]

        return {
            "missing": missing,
            "extra": extra,
            "match":
                len(missing) == 0 and
                len(extra) == 0
        }

    @staticmethod
    def clean_string(text):

        if text:
            return " ".join(
                text.split()
            ).strip()

        return ""

    @staticmethod
    def is_sorted(lst, reverse=False):

        if reverse:
            return lst == sorted(
                lst,
                reverse=True
            )

        return lst == sorted(lst)