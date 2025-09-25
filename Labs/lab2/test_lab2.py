# === CS 115 Lab 2 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name:Shrikar Swami
#
# Pledge:I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Lab 2 ===

import lab2
import unittest
# You can access vali_date as lab2.vali_date in this file.

class TestCases(unittest.TestCase):
    def test_vali_date_case_1(self):
        """
        Tests that the date May 15th registers as valid.
        """
        self.assertTrue(lab2.vali_date(5, 15))

    def test_vali_date_case_2(self):
        # Valid date (October 29th exists)
        self.assertTrue(lab2.vali_date(10, 29))

        # Valid date (November 8th exists)
        self.assertTrue(lab2.vali_date(11, 8))

        # Invalid date (April has only 30 days, so April 31st should fail)
        self.assertFalse(lab2.vali_date(4, 31))

        # Invalid date (February only has 29 days)
        self.assertFalse(lab2.vali_date(2,30))

        # Invalid date (There is only 12 months)
        self.assertFalse(lab2.vali_date(13,2))

        #Invalid date (There isn't a 0 date)
        self.assertFalse(lab2.vali_date(12,0))

        # Valid date (February 29th exists)
        self.assertTrue(lab2.vali_date(2,29))


if __name__ == "__main__":
    unittest.main()
