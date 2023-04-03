import os
import sys
import unittest

sys.path.append("lib")

if __name__ == "__main__":
    os.environ["__TESTING__"] = "1"
    runner = unittest.TextTestRunner().run(unittest.defaultTestLoader.discover("."))
