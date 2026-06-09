# =========================================================
# Logger Utility - Structured Logging for Framework
# =========================================================
import os
import logging
from datetime import datetime


def setup_logger():

    logs_dir = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "logs"
    )

    os.makedirs(logs_dir, exist_ok=True)

    log_file = os.path.join(
        logs_dir,
        f"test_log_{datetime.now().strftime('%Y%m%d')}.log"
    )

    logging.basicConfig(
        level=logging.INFO,
        format=(
            "%(asctime)s "
            "[%(levelname)s] "
            "%(name)s - %(message)s"
        ),
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(
                log_file,
                encoding="utf-8"
            ),
            logging.StreamHandler()
        ],
        force=True
    )

    logger = logging.getLogger()

    logger.info("Logger initialized successfully")

    return logger


log = setup_logger()