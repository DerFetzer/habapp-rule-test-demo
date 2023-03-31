import sys
import unittest

sys.path.append("lib")

if __name__ == "__main__":
    runner = unittest.TextTestRunner().run(unittest.defaultTestLoader.discover("."))
