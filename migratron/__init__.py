import sys

if not sys.argv[0].endswith("migratron"):
    raise RuntimeError("This package is intended to be used from CLI only.")