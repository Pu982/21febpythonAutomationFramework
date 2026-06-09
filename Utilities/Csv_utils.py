# =========================================================
# CSV Utility - Read/Write CSV Test Data
# =========================================================
import os
import csv
import logging

logger = logging.getLogger(__name__)


class CsvUtils:

    @staticmethod
    def read_csv(file_path):

        logger.info(f"Reading CSV: {file_path}")

        try:
            data = []

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:

                reader = csv.DictReader(file)

                for row in reader:
                    data.append(dict(row))

            logger.info(f"CSV rows read: {len(data)}")

            return data

        except FileNotFoundError:
            logger.error(f"CSV file not found: {file_path}")

            raise

        except Exception as e:
            logger.error(f"Failed to read CSV: {e}")

            raise

    @staticmethod
    def read_csv_as_list(file_path):

        logger.info(f"Reading CSV as list: {file_path}")

        data = []

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            reader = csv.reader(file)

            for row in reader:
                data.append(row)

        logger.info(f"CSV rows read: {len(data)}")

        return data

    @staticmethod
    def write_csv(file_path, headers, data_rows):

        logger.info(f"Writing CSV: {file_path}")

        os.makedirs(
            os.path.dirname(file_path),
            exist_ok=True
        )

        with open(
            file_path,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow(headers)

            writer.writerows(data_rows)

        logger.info(
            f"CSV written successfully: {len(data_rows)} rows"
        )

    @staticmethod
    def get_row_count(file_path):

        data = CsvUtils.read_csv(file_path)

        return len(data)