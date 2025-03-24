import sys

from migropy.core.logger import logger

if not sys.argv[0].endswith("migropy"):
    logger.error('this package is intended to be used from CLI only.')
    sys.exit(1)

current_version = "0.2.0"
