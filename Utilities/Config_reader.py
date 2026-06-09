# =========================================================
# Config Reader - Environment Configuration Reader
# =========================================================
import os
import logging
import configparser

logger = logging.getLogger(__name__)


class ConfigReader:

    def __init__(self, env="qa"):

        self.env = env

        config_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "config"
        )

        config_file = os.path.join(
            config_dir,
            f"{env}.ini"
        )

        if not os.path.exists(config_file):
            raise FileNotFoundError(
                f"Config file not found: {config_file}"
            )

        self.config = configparser.ConfigParser()

        self.config.read(config_file)

        logger.info(
            f"Config loaded for environment: {env}"
        )

    def get_base_url(self):

        return self.config.get(
            "environment",
            "base_url"
        )

    def get_username(self):

        return self.config.get(
            "environment",
            "username"
        )

    def get_password(self):

        return self.config.get(
            "environment",
            "password"
        )

    def get_env_name(self):

        return self.config.get(
            "environment",
            "env"
        )

    def get_browser(self):

        return self.config.get(
            "browser",
            "browser_name"
        )

    def is_headless(self):

        return self.config.getboolean(
            "browser",
            "headless"
        )

    def get_implicit_wait(self):

        return self.config.getint(
            "browser",
            "implicit_wait"
        )

    def get_explicit_wait(self):

        return self.config.getint(
            "browser",
            "explicit_wait"
        )

    def get_page_load_timeout(self):

        return self.config.getint(
            "browser",
            "page_load_timeout"
        )

    def get_timeout(self):

        return self.config.getint(
            "execution",
            "timeout"
        )

    def get_retries(self):

        return self.config.getint(
            "execution",
            "retries"
        )

    def get_workers(self):

        return self.config.getint(
            "execution",
            "workers"
        )

    def is_parallel(self):

        return self.config.getboolean(
            "execution",
            "parallel"
        )

    def get_screenshot_mode(self):

        return self.config.get(
            "reporting",
            "screenshot"
        )

    def get_log_level(self):

        return self.config.get(
            "reporting",
            "log_level"
        )

    def get(self, section, key, fallback=None):

        return self.config.get(
            section,
            key,
            fallback=fallback
        )