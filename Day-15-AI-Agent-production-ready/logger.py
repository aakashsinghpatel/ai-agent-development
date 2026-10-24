import logging
""" This is part of observability """
logging.basicConfig(level=logging.INFO,
    format=("%(asctime)s | ""%(levelname)s | ""%(message)s"))

logger = logging.getLogger("Agent Logger")