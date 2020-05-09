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
        file_input = 'getColumnNames1.csv'

        actual_result = self.dev_stats.top_five(
            self.dev_stats.count_data(self.dev_stats.categorize_data(file_input)))
        expected_result = {
            'low_salary':
            {
                'count': 0, 'min': 0, 'max': 50000, 'data': {}
            },
            'medium_salary':
            {
                'count': 0, 'min': 50001, 'max': 80000, 'data': {}
            },
            'high_salary':
            {
                'count': 0, 'min': 80001, 'max': 200000, 'data': {}
            }
        }
        self.assertDictEqual(actual_result, expected_result)

    def test_for_nine_entries(self):
        """
        Test case for a csv file with 9 entries
        """
        file_input = 'categorizeData2.csv'

        actual_result = self.dev_stats.top_five(self.dev_stats.count_data(
            self.dev_stats.categorize_data(file_input)))
        expected_result = {
            'low_salary':
            {
                'count': 2, 'min': 0, 'max': 50000, 'data':
                {
                    'TypeScript': 1, '1 - 2 hours': 2,
                    'JavaScript': 2, 'HTML': 2, 'CSS': 2
                }
            },
            'medium_salary':
            {
                'count': 2, 'min': 50001, 'max': 80000, 'data': {
                    'SQL': 1, 'HTML': 1, 'CSS': 1,
                    'Bash/Shell': 1, 'JavaScript': 2
                }
            },
            'high_salary':
            {
                'count': 5, 'min': 80001, 'max': 200000, 'data': {
                    'Masterâ€™s degree (MA, MS, M.Eng., MBA, etc.)': 3, 'C#': 3,
                    'HTML': 3, 'Python': 3, 'JavaScript': 4
                }
            }
        }

        self.assertEqual(actual_result, expected_result)

    def test_for_all_entries(self):
        """
        Test case for csv with all the stats
        """
        file_input = 'stats.csv'

        actual_result = self.dev_stats.top_five(self.dev_stats.count_data(
            self.dev_stats.categorize_data(file_input)))
        expected_result = {
            'low_salary':
            {
                'count': 826, 'min': 0, 'max': 50000, 'data':
                {
                    'SQL': 463, 'Computer science, computer'+
                    ' engineering, or software engineering': 539,
                    'CSS': 558, 'HTML': 584, 'JavaScript': 600
                }
            },
            'medium_salary':
            {
                'count': 507, 'min': 50001, 'max': 80000, 'data': {
                    'SQL': 297, 'Computer science, computer engineering,'+
                    ' or software engineering': 312,
                    'CSS': 331, 'HTML': 347, 'JavaScript': 364
                }
            },
            'high_salary': {
                'count': 667, 'min': 80001, 'max': 200000, 'data': {
                    'United States': 406, 'Computer science, computer'+
                    ' engineering, or software engineering': 409,
                    'CSS': 413, 'HTML': 448, 'JavaScript': 504
                }
            }
        }
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
