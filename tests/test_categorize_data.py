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
        file_file_input = 'getColumnNames1.csv'

        actual_result = self.dev_stats.categorize_data(file_file_input)
        expected_result = {
            'low_salary': {'min': 0, 'max': 50000, 'data': []},
            'medium_salary': {'min': 50001, 'max': 80000, 'data': []},
            'high_salary':  {'min': 80001, 'max': 200000, 'data': []}
        }
        self.assertDictEqual(actual_result, expected_result)

    def test_for_three_entries(self):
        """
        Test case for three entries in csv file
        """
        file_input = 'categorizeData1.csv'

        actual_result = self.dev_stats.categorize_data(file_input)
        expected_result = {
            'low_salary':
            {
                'min': 0, 'max': 50000, 'data': [
                    [
                        '95836', 'Argentina', 'Slightly satisfied',
                        'A business discipline (ex. accounting, finance, marketing)',
                        '45600.0', '1 - 2 times per week', 'Male',
                        'Hispanic or Latino/Latina',
                        'Secondary school (e.g. American high school,'+
                        ' German Realschule or Gymnasium, etc.)',
                        '1 - 2 hours', '35 - 44 years old', 'More than 4 years ago',
                        'C#;CoffeeScript;JavaScript;Ruby;HTML;CSS;Bash/Shell'
                    ]
                ]
            },
            'medium_salary':
            {
                'min': 50001, 'max': 80000, 'data': []
            },
            'high_salary':
            {
                'min': 80001, 'max': 200000, 'data':
                [
                    [
                        '51900', 'United Kingdom', 'Moderately satisfied',
                        'Computer science, computer engineering, or software engineering',
                        '94455.0', '3 - 4 times per week', 'Male',
                        'White or of European descent',
                        'Masterâ€™s degree (MA, MS, M.Eng., MBA, etc.)',
                        '3 - 4 hours', '35 - 44 years old', 'Between 1 and 2 years ago',
                        'C;C#;Java;JavaScript;Objective-C;PHP;Swift;HTML;CSS'
                    ],
                    [
                        '51710', 'Germany', 'Slightly dissatisfied',
                        'A social science (ex. anthropology, psychology, political science)',
                        '807756.0', '3 - 4 times per week', 'Male',
                        'White or of European descent',
                        'Secondary school (e.g. American high school,'+
                        ' German Realschule or Gymnasium, etc.)',
                        '1 - 2 hours', '25 - 34 years old', 'Between 2 and 4 years ago',
                        'C#;JavaScript;Python;TypeScript;HTML;Bash/Shell'
                    ]
                ]
            }
        }
        self.assertDictEqual(actual_result, expected_result)

    def test_for_ten_entries(self):
        """
        Test case for three entries in csv file
        """
        file_input = 'categorizeData2.csv'

        actual_result = self.dev_stats.categorize_data(file_input)
        expected_result = {
            'low_salary':
            {
                'min': 0, 'max': 50000, 'data': [
                    [
                        '95836', 'Argentina', 'Slightly satisfied',
                        'A business discipline (ex. accounting, finance, marketing)',
                        '45600.0', '1 - 2 times per week', 'Male', 'Hispanic or Latino/Latina',
                        'Secondary school (e.g. American high school,'+
                        ' German Realschule or Gymnasium, etc.)',
                        '1 - 2 hours', '35 - 44 years old', 'More than 4 years ago',
                        'C#;CoffeeScript;JavaScript;Ruby;HTML;CSS;Bash/Shell'
                    ],
                    [
                        '36729', 'Brazil', 'Moderately dissatisfied',
                        'Computer science, computer engineering, or software engineering',
                        '16848.0', '3 - 4 times per week', 'Male', 'Hispanic or Latino/Latina',
                        'Primary/elementary school', '1 - 2 hours', '25 - 34 years old',
                        'Less than a year ago', 'JavaScript;PHP;Python;SQL;TypeScript;HTML;CSS'
                    ]
                ]
            },
            'medium_salary':
            {
                'min': 50001, 'max': 80000, 'data': [
                    [
                        '31721', 'Japan', 'Slightly dissatisfied',
                        'Information systems, information technology, or system administration',
                        '77433.0', '3 - 4 times per week', 'Male', 'East Asian',
                        'They never completed any formal education', '30 - 59 minutes',
                        '35 - 44 years old', 'Between 2 and 4 years ago', 'JavaScript;PHP'
                    ],
                    [
                        '38620', 'Germany', 'Moderately dissatisfied',
                        'Computer science, computer engineering, or software engineering',
                        '73433.0', "I don't typically exercise", 'Female',
                        'White or of European descent',
                        'Secondary school (e.g. American high school,'+
                        ' German Realschule or Gymnasium, etc.)',
                        '1 - 2 hours', '35 - 44 years old', 'Less than a year ago',
                        'Groovy;Java;JavaScript;SQL;HTML;CSS;Bash/Shell'
                    ]
                ]
            },
            'high_salary':
            {
                'min': 80001, 'max': 200000, 'data': [
                    [
                        '51900', 'United Kingdom', 'Moderately satisfied',
                        'Computer science, computer engineering, or software engineering',
                        '94455.0', '3 - 4 times per week', 'Male', 'White or of European descent',
                        'Masterâ€™s degree (MA, MS, M.Eng., MBA, etc.)', '3 - 4 hours',
                        '35 - 44 years old', 'Between 1 and 2 years ago',
                        'C;C#;Java;JavaScript;Objective-C;PHP;Swift;HTML;CSS'
                    ],
                    [
                        '51710', 'Germany', 'Slightly dissatisfied',
                        'A social science (ex. anthropology, psychology, political science)',
                        '807756.0', '3 - 4 times per week', 'Male', 'White or of European descent',
                        'Secondary school (e.g. American high school,'+
                        ' German Realschule or Gymnasium, etc.)',
                        '1 - 2 hours', '25 - 34 years old', 'Between 2 and 4 years ago',
                        'C#;JavaScript;Python;TypeScript;HTML;Bash/Shell'
                    ],
                    [
                        '44125', 'United States', 'Moderately dissatisfied',
                        'A social science (ex. anthropology, psychology, political science)',
                        '175000.0', '1 - 2 times per week', 'Male',
                        'White or of European descent',
                        'Bachelorâ€™s degree (BA, BS, B.Eng., etc.)',
                        'Less than 30 minutes', '45 - 54 years old',
                        'Between 1 and 2 years ago', 'JavaScript;Python'
                    ],
                    [
                        '35167', 'United Kingdom', 'Extremely satisfied',
                        'A humanities discipline (ex. literature, history, philosophy)',
                        '90288.0', "I don't typically exercise", 'Male',
                        'White or of European descent',
                        'Masterâ€™s degree (MA, MS, M.Eng., MBA, etc.)',
                        '30 - 59 minutes', '25 - 34 years old',
                        'Less than a year ago', 'C#;Go;JavaScript;Ruby;HTML;CSS'
                    ],
                    [
                        '54695', 'Netherlands', 'Moderately satisfied',
                        'Computer science, computer engineering, or software engineering',
                        '82000.0', '1 - 2 times per week', 'Male',
                        'White or of European descent',
                        'Masterâ€™s degree (MA, MS, M.Eng., MBA, etc.)',
                        '30 - 59 minutes', '25 - 34 years old',
                        'Less than a year ago', 'Java;Python;SQL'
                    ]
                ]
            }
        }
        self.assertDictEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()
