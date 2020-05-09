"""
test_count_data.py
Carlos and Mellisa
Created April 27, 2020
"""

import unittest
from project.dev_stats_analysis import DeveloperStats


class TestCountData(unittest.TestCase):
    """
    Tests for count_data() method in DeveloperStats class
    """

    def setUp(self):
        """
        Define attribute dev_stats to hold object of type DeveloperStats
        """
        self.dev_stats = DeveloperStats()

    def test_for_empty_file(self):
        """
        Test case for testing empty csv
        """
        file_input = self.dev_stats.categorize_data('getColumnNames1.csv')
        actual_result = self.dev_stats.count_data(file_input)
        expected_result = {
            'low_salary': {'count': 0, 'min': 0, 'max': 50000, 'data': {}},
            'medium_salary': {'count': 0, 'min': 50001, 'max': 80000, 'data': {}},
            'high_salary': {'count': 0, 'min': 80001, 'max': 200000, 'data': {}}
        }
        self.assertDictEqual(actual_result, expected_result)

    def test_for_three_entries(self):
        """
        Test case for three entries in csv file
        """
        file_input = self.dev_stats.categorize_data('categorizeData1.csv')

        actual_result = self.dev_stats.count_data(file_input)

        expected_result = {
            'low_salary':
            {
                'count': 1, 'min': 0, 'max': 50000, 'data': {
                    'C#': 1, 'CoffeeScript': 1, 'JavaScript': 1, 'Ruby': 1,
                    'HTML': 1, 'CSS': 1, 'Bash/Shell': 1, 'Argentina': 1,
                    'Slightly satisfied': 1,
                    'A business discipline (ex. accounting, finance, marketing)': 1,
                    '1 - 2 times per week': 1,
                    'Secondary school (e.g. American high school,'+
                    ' German Realschule or Gymnasium, etc.)': 1,
                    '1 - 2 hours': 1, 'More than 4 years ago': 1
                }
            },
            'medium_salary':
            {
                'count': 0, 'min': 50001, 'max': 80000, 'data': {}
            },
            'high_salary':
            {
                'count': 2, 'min': 80001, 'max': 200000, 'data': {
                    'C': 1, 'C#': 2, 'Java': 1, 'JavaScript': 2, 'Objective-C': 1,
                    'PHP': 1, 'Swift': 1, 'HTML': 2, 'CSS': 1, 'United Kingdom': 1,
                    'Moderately satisfied': 1,
                    'Computer science, computer engineering, or software engineering': 1,
                    '3 - 4 times per week': 2, 'Masterâ€™s degree (MA, MS, M.Eng., MBA, etc.)': 1,
                    '3 - 4 hours': 1, 'Between 1 and 2 years ago': 1, 'Python': 1, 'TypeScript': 1,
                    'Bash/Shell': 1, 'Germany': 1, 'Slightly dissatisfied': 1,
                    'A social science (ex. anthropology, psychology, political science)': 1,
                    'Secondary school (e.g. American high school, German '+
                    'Realschule or Gymnasium, etc.)': 1,
                    '1 - 2 hours': 1, 'Between 2 and 4 years ago': 1
                }
            }
        }

        self.assertDictEqual(actual_result, expected_result)

    def test_for_ten_entries(self):
        """
        Test case for three entries in csv file
        """
        file_input = self.dev_stats.categorize_data('categorizeData2.csv')

        actual_result = self.dev_stats.count_data(file_input)

        expected_result = {
            'low_salary':
            {
                'count': 2, 'min': 0, 'max': 50000, 'data':
                {
                    'C#': 1, 'CoffeeScript': 1, 'JavaScript': 2, 'Ruby': 1,
                    'HTML': 2, 'CSS': 2, 'Bash/Shell': 1, 'Argentina': 1,
                    'Slightly satisfied': 1,
                    'A business discipline (ex. accounting, finance, marketing)': 1,
                    '1 - 2 times per week': 1,
                    'Secondary school (e.g. American high school,'+
                    ' German Realschule or Gymnasium, etc.)': 1,
                    '1 - 2 hours': 2, 'More than 4 years ago': 1, 'PHP': 1,
                    'Python': 1, 'SQL': 1, 'TypeScript': 1,
                    'Brazil': 1, 'Moderately dissatisfied': 1,
                    'Computer science, computer engineering, or software engineering': 1,
                    '3 - 4 times per week': 1, 'Primary/elementary school': 1,
                    'Less than a year ago': 1
                }
            },
            'medium_salary':
            {
                'count': 2, 'min': 50001, 'max': 80000, 'data':
                {
                    'JavaScript': 2, 'PHP': 1, 'Japan': 1, 'Slightly dissatisfied': 1,
                    'Information systems, information technology, or system administration': 1,
                    '3 - 4 times per week': 1, 'They never completed any formal education': 1,
                    '30 - 59 minutes': 1, 'Between 2 and 4 years ago': 1, 'Groovy': 1,
                    'Java': 1, 'SQL': 1, 'HTML': 1, 'CSS': 1, 'Bash/Shell': 1, 'Germany': 1,
                    'Moderately dissatisfied': 1,
                    'Computer science, computer engineering, or software engineering': 1,
                    "I don't typically exercise": 1,
                    'Secondary school (e.g. American high school,'+
                    ' German Realschule or Gymnasium, etc.)': 1,
                    '1 - 2 hours': 1, 'Less than a year ago': 1
                }
            },
            'high_salary':
            {
                'count': 5, 'min': 80001, 'max': 200000, 'data':
                {
                    'C': 1, 'C#': 3, 'Java': 2, 'JavaScript': 4, 'Objective-C': 1, 'PHP': 1,
                    'Swift': 1, 'HTML': 3, 'CSS': 2, 'United Kingdom': 2, 'Moderately satisfied': 2,
                    'Computer science, computer engineering, or software engineering': 2,
                    '3 - 4 times per week': 2, 'Masterâ€™s degree (MA, MS, M.Eng., MBA, etc.)': 3,
                    '3 - 4 hours': 1, 'Between 1 and 2 years ago': 2, 'Python': 3,
                    'TypeScript': 1, 'Bash/Shell': 1, 'Germany': 1, 'Slightly dissatisfied': 1,
                    'A social science (ex. anthropology, psychology, political science)': 2,
                    'Secondary school (e.g. American high school,'+
                    ' German Realschule or Gymnasium, etc.)': 1,
                    '1 - 2 hours': 1, 'Between 2 and 4 years ago': 1, 'United States': 1,
                    'Moderately dissatisfied': 1, '1 - 2 times per week': 2,
                    'Bachelorâ€™s degree (BA, BS, B.Eng., etc.)': 1, 'Less than 30 minutes': 1,
                    'Go': 1, 'Ruby': 1, 'Extremely satisfied': 1,
                    'A humanities discipline (ex. literature, history, philosophy)': 1,
                    "I don't typically exercise": 1, '30 - 59 minutes': 2,
                    'Less than a year ago': 2, 'SQL': 1, 'Netherlands': 1
                }
            }
        }
        self.assertDictEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
