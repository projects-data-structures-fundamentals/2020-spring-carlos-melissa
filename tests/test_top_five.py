"""
test_top_five.py
Carlos and Mellisa
Created April 27, 2020
"""

import unittest
from project.dev_stats_analysis import DeveloperStats


class TestTopFive(unittest.TestCase):
    """
    Tests for top_five() method in DeveloperStats class
    """

    def setUp(self):
        """
        Define attribute dev_stats to hold object of type DeveloperStats
        """
        self.dev_stats = DeveloperStats()

    def test_for_empty_file(self):
        """
        Test case for testing empty csv file header or empty csv file
        """
        input = 'getColumnNames1.csv'

        actual_result = self.dev_stats.top_five(
            self.dev_stats.count_data(self.dev_stats.categorize_data(input)))
        expected_result = {}
        print(actual_result)
        self.assertDictEqual(actual_result, expected_result)

    def test_for_ten_entries(self):
        """
        Test case for a csv file header with 3 columns
        """
        input = 'categorizeData2.csv'

        actual_result = self.dev_stats.top_five(self.dev_stats.count_data(
            self.dev_stats.categorize_data(input)))
        expected_result = {}
        self.assertEqual(actual_result, expected_result)

    def test_for_all_entries(self):
        """
        Test case for a csv file header columns
        """
        input = 'stats.csv'

        actual_result = self.dev_stats.top_five(self.dev_stats.count_data(
            self.dev_stats.categorize_data(input)))
        expected_result = ['Respondent', 'Country', 'JobSatisfaction', 'UndergradMajor', 'ConvertedSalary', 'Exercise',
                           'Gender', 'RaceEthnicity', 'EducationParents', 'HoursOutside', 'Age', 'LastNewJob', 'LanguageWorkedWith']
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
