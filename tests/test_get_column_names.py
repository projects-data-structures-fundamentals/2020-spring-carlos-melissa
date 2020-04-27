"""
test_get_column_names.py
Carlos and Mellisa
Created April 27, 2020
"""

import unittest
from .practice_transformations import StudentModel


class TestGetColumnNames(unittest.TestCase):
    """
    Tests for test_get_column_names() method in DeveloperStats class
    """

    def setUp(self):
        """
        Define attribute dev_stats to hold object of type DeveloperStats
        """
        self.dev_stats = DeveloperStats()

    def test_for_empty_header(self):
        """
        Test case for testing empty header
        """
        input = 'stats.csv'

        actual_result = self.dev_stats.DeveloperStats(input)
        expected_result = ''
        self.assertDictEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
