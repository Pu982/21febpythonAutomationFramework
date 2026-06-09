# =========================================================
import os
import sys
import json
import pytest
import logging


logger = logging.getLogger(__name__)

DATA_PATH = os.path.join(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(__file__)
        )
    ),
    "testdata",
    "login_data.json"
)