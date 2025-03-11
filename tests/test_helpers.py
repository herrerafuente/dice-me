# region Import Libraries
import unittest
import os
import shutil
import tempfile
from unittest.mock import patch
import cv2
# endregion

# region Import the functions to be tested
from helpers import get_current_directory, find_photos, remove_background
# endregion

# Test case
class TestPhotoFunctions(unittest.TestCase):
    def setUp(self):
        #Set up a temporary directory
        self.test_dir = tempfile.TemporaryDirectory()

        self.real_image_path = r'C:\Users\pablo\PycharmProjects\dice-me\tests\resources\test_image_1.jpg'
        self.image1 = os.path.join(self.test_dir.name, 'test1.jpg')
        self.image2 = os.path.join(self.test_dir.name, 'test2.png')

        shutil.copy(self.real_image_path, self.image1)
        shutil.copy(self.real_image_path, self.image2)

    def tearDown(self):
        self.test_dir.cleanup()

    def test_get_current_directory(self):
        self.assertEqual(get_current_directory(), os.getcwd())

    def test_find_no_photos(self):
        empty_dir = tempfile.TemporaryDirectory()
        photos = find_photos(empty_dir.name)
        self.assertEqual(photos, [])
        empty_dir.cleanup()

    #TODO: Write test cases for find_photos
    #TODO Write test cases for remove_background


# endregion


if __name__ == '__main__':
    unittest.main()
