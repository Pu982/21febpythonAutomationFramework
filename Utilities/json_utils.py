# =========================================================
# JSON Utility - Read/Write JSON Test Data
# =========================================================
import os
import json
import logging

logger = logging.getLogger(__name__)


class JsonUtils:

    @staticmethod
    def read_json(file_path):

        logger.info(f"Reading JSON: {file_path}")

        try:
            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as f:

                data = json.load(f)

            logger.info("JSON data loaded successfully")

            return data

        except FileNotFoundError:
            logger.error(f"JSON file not found: {file_path}")

            raise

        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON format: {e}")

            raise

    @staticmethod
    def write_json(file_path, data):

        logger.info(f"Writing JSON: {file_path}")

        try:
            os.makedirs(
                os.path.dirname(file_path),
                exist_ok=True
            )

            with open(
                file_path,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    data,
                    f,
                    indent=4,
                    ensure_ascii=False
                )

            logger.info("JSON written successfully")

        except Exception as e:
            logger.error(f"Failed to write JSON: {e}")

            raise

    @staticmethod
    def get_value(file_path, key):

        data = JsonUtils.read_json(file_path)

        value = data.get(key)

        logger.info(f"JSON key '{key}' = {value}")

        return value

    @staticmethod
    def get_nested_value(file_path, *keys):

        data = JsonUtils.read_json(file_path)

        for key in keys:
            data = data[key]

        logger.info(f"Nested value: {data}")

        return data