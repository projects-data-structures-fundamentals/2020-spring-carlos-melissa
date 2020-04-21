"""
project.py
Final project for COMP 525
Carlos Sandoval & Melissa Mullen
Updated April 21, 2020
"""
# import plotly


class DeveloperStats():
    """
    Reads information from a CSV file, categorizes the data by salary, counts
    the occurrance of features, and plots the results
    """
    @classmethod
    def read_csv(cls, filename):
        """
        This method sorts through the CSV file provided from filename,
        parses the results into a dictionary, and counts the results
        filename: name of a CSV file (string)
        Returns: dictionary
            keys: categories from CSV file (strings)
            values: dictionary
                keys: answers from respondents (strings)
                value: count of occurrence of answers (integers)
        """
        # Do not forget to parse the LanguageWorkedWith category

    @classmethod
    def categorize_data(cls, count_dict):
        """
        This method sorts through the dictionary returned from read_csv() and
        categorizes the data into three categories: low_salary, medium_salary,
        and high_salary
        count_dict: the dictionary returned from read_csv()
        Returns: dictionary
            keys: salary category (strings)
            values: dictionary
                keys: categories from CSV file (strings)
                values: dictionary
                    keys: answers from respondents (strings)
                    values: count of occurrence of answers (integers)
        """

    @classmethod
    def top_five(cls, category_dict):
        """
        This method sorts through the dictionary returned from
        categorize_data() and determines the top five results for each salary
        category
        category_dict: the dictionary returned from categorize_data()
        Returns: dictionary
            keys: salary category (strings)
            values: dictionary
                keys: categories from CSV file (strings)
                values: dictionary
                    keys: top answers (strings)
                    values: count of occurrence of answers (integers)
        """

    @classmethod
    def plot_data(cls, top_five_dict):
        """
        This method requires the plotly library
        This method sorts through the dictionary returned from top_five() and
        plots the occurrance of answers for each salary category
        top_five_dict: the dictionary returned from top_five()
        Returns: three plots that display the results of top_five_dict
        """


def main():
    """
    Contains test cases for the DeveloperStats class methods
    """


if __name__ == '__main__':
    main()
