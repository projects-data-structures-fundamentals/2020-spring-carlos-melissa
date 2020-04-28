"""
test_categorize_data.py
Carlos and Mellisa
Created April 27, 2020
"""

import unittest
from project.dev_stats_analysis import DeveloperStats


class TestCategorizeData(unittest.TestCase):
    """
    Tests for categorize_data() method in DeveloperStats class
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
        input = 'getColumnNames1.csv'

        actual_result = self.dev_stats.categorize_data(input)
        expected_result = {
            'high_salary': {'count': 0, 'data': [], 'max': 200000, 'min': 80001},
            'low_salary': {'count': 0, 'data': [], 'max': 50000, 'min': 0},
            'medium_salary': {'count': 0, 'data': [], 'max': 80000, 'min': 50001}
        }
        self.assertDictEqual(actual_result, expected_result)

    def test_for_three_entries(self):
        """
        Test case for three entries in csv file
        """
        input = 'categorizeData1.csv'

        actual_result = self.dev_stats.categorize_data(input)
        expected_result = {'low_salary':
                           {'count': 1, 'min': 0, 'max': 50000, 'data': [
                               ['Argentina', 'Slightly satisfied', 'A business discipline (ex. accounting, finance, marketing)',
                                '1 - 2 times per week', 'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)', '1 - 2 hours',
                                'More than 4 years ago', 'C#;CoffeeScript;JavaScript;Ruby;HTML;CSS;Bash/Shell']
                           ]
                           },
                           'medium_salary': {'count': 0, 'min': 50001, 'max': 80000, 'data': []},
                           'high_salary': {'count': 2, 'min': 80001, 'max': 200000, 'data': [
                               ['United Kingdom', 'Moderately satisfied', 'Computer science, computer engineering, or software engineering',
                                '3 - 4 times per week', 'Masterâ€™s degree (MA, MS, M.Eng., MBA, etc.)', '3 - 4 hours', 'Between 1 and 2 years ago',
                                'C;C#;Java;JavaScript;Objective-C;PHP;Swift;HTML;CSS'],
                               ['Germany', 'Slightly dissatisfied', 'A social science (ex. anthropology, psychology, political science)',
                                '3 - 4 times per week', 'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)',
                                '1 - 2 hours', 'Between 2 and 4 years ago', 'C#;JavaScript;Python;TypeScript;HTML;Bash/Shell']
                           ]
                           }
                           }
        self.assertDictEqual(actual_result, expected_result)

    def test_for_ten_entries(self):
        """
        Test case for three entries in csv file
        """
        input = 'categorizeData2.csv'

        actual_result = self.dev_stats.categorize_data(input)
        expected_result = {'low_salary': {'count': 2, 'min': 0, 'max': 50000, 'data': [['Argentina', 'Slightly satisfied', 'A business discipline (ex. accounting, finance, marketing)', '1 - 2 times per week', 'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)', '1 - 2 hours', 'More than 4 years ago', 'C#;CoffeeScript;JavaScript;Ruby;HTML;CSS;Bash/Shell'], ['Brazil', 'Moderately dissatisfied', 'Computer science, computer engineering, or software engineering', '3 - 4 times per week', 'Primary/elementary school', '1 - 2 hours', 'Less than a year ago', 'JavaScript;PHP;Python;SQL;TypeScript;HTML;CSS']]}, 'medium_salary': {'count': 2, 'min': 50001, 'max': 80000, 'data': [['Japan', 'Slightly dissatisfied', 'Information systems, information technology, or system administration', '3 - 4 times per week', 'They never completed any formal education', '30 - 59 minutes', 'Between 2 and 4 years ago', 'JavaScript;PHP'], ['Germany', 'Moderately dissatisfied', 'Computer science, computer engineering, or software engineering', "I don't typically exercise", 'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)', '1 - 2 hours', 'Less than a year ago', 'Groovy;Java;JavaScript;SQL;HTML;CSS;Bash/Shell']]}, 'high_salary': {'count': 5, 'min': 80001, 'max': 200000, 'data': [
            ['United Kingdom', 'Moderately satisfied', 'Computer science, computer engineering, or software engineering', '3 - 4 times per week', 'Masterâ€™s degree (MA, MS, M.Eng., MBA, etc.)', '3 - 4 hours', 'Between 1 and 2 years ago', 'C;C#;Java;JavaScript;Objective-C;PHP;Swift;HTML;CSS'], ['Germany', 'Slightly dissatisfied', 'A social science (ex. anthropology, psychology, political science)', '3 - 4 times per week', 'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)', '1 - 2 hours', 'Between 2 and 4 years ago', 'C#;JavaScript;Python;TypeScript;HTML;Bash/Shell'], ['United States', 'Moderately dissatisfied', 'A social science (ex. anthropology, psychology, political science)', '1 - 2 times per week', 'Bachelorâ€™s degree (BA, BS, B.Eng., etc.)', 'Less than 30 minutes', 'Between 1 and 2 years ago', 'JavaScript;Python'], ['United Kingdom', 'Extremely satisfied', 'A humanities discipline (ex. literature, history, philosophy)', "I don't typically exercise", 'Masterâ€™s degree (MA, MS, M.Eng., MBA, etc.)', '30 - 59 minutes', 'Less than a year ago', 'C#;Go;JavaScript;Ruby;HTML;CSS'], ['Netherlands', 'Moderately satisfied', 'Computer science, computer engineering, or software engineering', '1 - 2 times per week', 'Masterâ€™s degree (MA, MS, M.Eng., MBA, etc.)', '30 - 59 minutes', 'Less than a year ago', 'Java;Python;SQL']]}}
        self.assertDictEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
