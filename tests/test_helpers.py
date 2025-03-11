# region Import Libraries
import unittest
import os
import tempfile
from unittest.mock import patch
import cv2
import numpy as np
# endregion

# region Import the functions to be tested
from helpers import get_current_directory, find_photos, remove_background
# endregion

def add(a, b):
    return a + b

# Test case
class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # Check if 2+3 = 5
        self.assertEqual(add(-1, 1), 0)  # Check if -1+1 = 0




if __name__ == '__main__':
    unittest.main()
