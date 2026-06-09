import random
import string
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class RandomDataGenerator:

    @staticmethod
    def generate_unique_username(prefix="user"):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        username = f"{prefix}_{timestamp}"

        logger.info(f"Generated username: {username}")

        return username

    @staticmethod
    def generate_random_email(domain="test.com"):
        timestamp = datetime.now().strftime("%H%M%S")

        random_str = "".join(
            random.choices(
                string.ascii_lowercase,
                k=5
            )
        )

        email = f"test_{random_str}_{timestamp}@{domain}"

        logger.info(f"Generated email: {email}")

        return email

    @staticmethod
    def generate_random_phone():
        phone = "".join(
            random.choices(
                string.digits,
                k=10
            )
        )

        logger.info(f"Generated phone: {phone}")

        return phone

    @staticmethod
    def generate_random_name():
        names = [
            "John",
            "Jane",
            "Mike",
            "Sarah",
            "David",
            "Emily",
            "Alex",
            "Lisa",
            "Robert",
            "Anna",
            "James",
            "Maria",
            "Thomas",
            "Laura",
            "William"
        ]

        name = random.choice(names)

        logger.info(f"Generated name: {name}")

        return name

    @staticmethod
    def generate_random_number(min_val=1000, max_val=9999):
        num = random.randint(min_val, max_val)

        logger.info(f"Generated number: {num}")

        return num

    @staticmethod
    def generate_random_string(length=8):
        result = "".join(
            random.choices(
                string.ascii_letters + string.digits,
                k=length
            )
        )

        logger.info(f"Generated string: {result}")

        return result

    @staticmethod
    def generate_random_card_number():
        card = "".join(
            random.choices(
                string.digits,
                k=16
            )
        )

        logger.info(
            f"Generated card: {card[:4]}********{card[-4:]}"
        )

        return card

    @staticmethod
    def generate_random_city():
        cities = [
            "New York",
            "London",
            "Tokyo",
            "Paris",
            "Mumbai",
            "Sydney",
            "Berlin",
            "Toronto",
            "Dubai",
            "Singapore",
            "Chicago",
            "Boston"
        ]

        city = random.choice(cities)

        logger.info(f"Generated city: {city}")

        return city

    @staticmethod
    def generate_random_country():
        countries = [
            "USA",
            "UK",
            "India",
            "Japan",
            "Germany",
            "Canada",
            "Australia",
            "France",
            "UAE",
            "Singapore",
            "Brazil"
        ]

        country = random.choice(countries)

        logger.info(f"Generated country: {country}")

        return country

    @staticmethod
    def generate_order_name():
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        order = (
            f"ORD_{timestamp}_"
            f"{random.randint(100, 999)}"
        )

        logger.info(f"Generated order name: {order}")

        return order