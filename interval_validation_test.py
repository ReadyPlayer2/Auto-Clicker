import unittest
import re

class IntervalValidation(unittest.TestCase):
    def setUp(self):
        self.click_reg = r"(?P<time>[\d]+)"  # only capture numbers

    def test_basic(self):
        text_input = "123"
        time = re.search(self.click_reg, text_input)
        self.assertIsNotNone(time)
        actual_time = int(time.group())
        self.assertEqual(123, actual_time)

    def test_non_int(self):
        text_input = "foo"
        time = re.search(self.click_reg, text_input)
        self.assertIsNone(time)

    def test_append_int(self):
        text_input = "foo123"
        time = re.search(self.click_reg, text_input)
        self.assertIsNotNone(time)
        actual_time = int(time.group())
        self.assertEqual(123, actual_time)

    def test_append_str(self):
        text_input = "123foo"
        time = re.search(self.click_reg, text_input)
        self.assertIsNotNone(time)
        actual_time = int(time.group())
        self.assertEqual(123, actual_time)

    def test_negative(self): # currently passing, update to expect -1 returned from validation function
        text_input = "-123"
        time = re.search(self.click_reg, text_input)
        self.assertIsNotNone(time)
        actual_time = int(time.group())
        self.assertEqual(123, actual_time)

if __name__ == '__main__':
    unittest.main()