import sys

from migratron.core.logger import logger

if not sys.argv[0].endswith("migratron"):
    logger.error('this package is intended to be used from CLI only.')
    sys.exit(1)

current_version = "0.1.0"
