"""
test_get_column_names.py
Carlos and Mellisa
Created April 27, 2020
"""

import unittest
from project.dev_stats_analysis import DeveloperStats


class TestGetColumnNames(unittest.TestCase):
    """
    Tests for get_column_names() method in DeveloperStats class
    """

    def setUp(self):
        """
        Define attribute dev_stats to hold object of type DeveloperStats
        """
        self.dev_stats = DeveloperStats()

    def test_for_empty_header(self):
        """
        Test case for testing empty csv file header or empty csv file
        """
        file_input = 'getColumnNames1.csv'

        actual_result = self.dev_stats.get_column_names(file_input)
        expected_result = ['']
        self.assertEqual(actual_result, expected_result)

    def test_for_three_columns(self):
        """
        Test case for a csv file header with 3 columns
        """
        file_input = 'getColumnNames2.csv'

        actual_result = self.dev_stats.get_column_names(file_input)
        expected_result = ['Respondent', 'Country', 'JobSatisfaction']
        self.assertEqual(actual_result, expected_result)

    def test_for_all_columns(self):
        """
        Test case for a csv file header columns
        """
        file_input = 'stats.csv'

        actual_result = self.dev_stats.get_column_names(file_input)
        expected_result = [
            'Respondent', 'Country', 'JobSatisfaction', 'UndergradMajor',
            'ConvertedSalary', 'Exercise', 'Gender', 'RaceEthnicity',
            'EducationParents', 'HoursOutside', 'Age', 'LastNewJob',
            'LanguageWorkedWith'
        ]
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
