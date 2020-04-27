"""
project.py
Final project for COMP 525
Carlos Sandoval & Melissa Mullen
Updated April 26, 2020
"""
import plotly.graph_objects as go


class DeveloperStats():
    """
    Reads information from a CSV file, categorizes the data by salary, counts
    the occurrance of features, and plots the results
    """
    @classmethod
    def get_column_names(cls, filename):
        """
        This method sorts through the first line of the CSV file provided
        from filename and parses the column names into a list
        filename: name of a CSV file (string)
        returns: list of strings (the names of the columns)
        """
        with open(filename, 'r') as file_ref:
            return file_ref.readline().strip().split('|')

    @classmethod
    def categorize_data(cls, filename):
        """
        This method sorts through the CSV file provided from filename and sorts
        the responses into three categories (low_salary, medium_salary,
        high_salary) based on their salary
        filename: name of a CSV file (string)
        returns: dictionary
            keys: salary category (string)
            values: dictionary
                keys: summary data from the method calculation (including count
                of responses, min salary, max salary, and data) (strings)
                values: the count of respondants (integer), min salary
                (integer), max salary (integer), and a list of lists containing
                responses
        """
        data_columns = DeveloperStats.get_column_names(filename)
        target_column_index = 4
        low_salary_list = []
        medium_salary_list = []
        high_salary_list = []
        frequency_data = {
            'low_salary': {'count': 0, 'min': 0, 'max': 50000, 'data': {}},
            'medium_salary': {'count': 0, 'min': 50001, 'max': 80000, 'data': {}},
            'high_salary':  {'count': 0, 'min': 80001, 'max': 200000, 'data': {}}
        }
        with open('stats.csv', 'r') as file_ref:
            temp_frequency_holder_dic = {}
            for line in file_ref.readlines()[1:]:
                row = line.strip().split('|')
                field_salary = float(row[target_column_index])
                del row[0] # respondant id
                del row[3] # salary
                del row[4] # gender
                del row[4] # race
                del row[6] # age
                if field_salary <= 50000:
                    low_salary_list.append(row) # appends this response to low_salary_list
                    frequency_data['low_salary']['count'] += 1 # count increases
                elif field_salary <= 80000:
                    medium_salary_list.append(row)
                    frequency_data['medium_salary']['count'] += 1
                else:
                    high_salary_list.append(row)
                    frequency_data['high_salary']['count'] += 1
        frequency_data['low_salary']['data'] = low_salary_list
        frequency_data['medium_salary']['data'] = medium_salary_list
        frequency_data['high_salary']['data'] = high_salary_list

        return frequency_data

    @classmethod
    def count_data(cls, filename):
        """
        This method sorts through the CSV file provided from filename and
        counts the occurrance of respondant's answers in each salary category
        filename: name of a CSV file (string)
        Returns: dictionary
            keys: salary category (strings)
            values: dictionary
                keys: summary data from the method calculation (including count
                of responses, min salary, max salary, and data) (strings)
                values: the count of respondants (integer), min salary
                (integer), max salary (integer), and a dictionary containing
                CSV data
                    keys: categories from CSV file (strings)
                    values: dictionary
                        keys: answers from respondents (strings)
                        values: count of occurrence of answers (integers)
        """
        category_dict = DeveloperStats.categorize_data(filename)
        frequency_data = {
            'low_salary': {'count': 0, 'min': 0, 'max': 50000, 'data': {}},
            'medium_salary': {'count': 0, 'min': 50001, 'max': 80000, 'data': {}},
            'high_salary':  {'count': 0, 'min': 80001, 'max': 200000, 'data': {}}
        }
        for salary_category in category_dict:
            frequency_data[salary_category]['count'] = category_dict[salary_category]['count'] # makes the count values the same as the previous method
            temp_frequency_holder_dic = {}
            for responses in category_dict[salary_category]['data']: # for responses in each salary category
                languages = responses[-1] # picks out the LanguageWorkedWith column
                list_of_languages = languages.split(';') # parses it
                for language in list_of_languages:
                    if(language not in temp_frequency_holder_dic): # if it's not a key already...
                        temp_frequency_holder_dic[language] = 0 # make it a key value pair
                    temp_frequency_holder_dic[language] += 1 # increment by one with each occurrance
                for item in responses[:-1]: # for all other features except languages
                    if(item not in temp_frequency_holder_dic):
                        temp_frequency_holder_dic[item] = 0
                    temp_frequency_holder_dic[item] += 1
            frequency_data[salary_category]['data'] = temp_frequency_holder_dic

        return frequency_data
    @classmethod
    def top_five(cls, category_dict):
        """
        This method sorts through the dictionary returned from
        count_data() and determines the top five results for each salary
        category
        category_dict: the dictionary returned from count_data()
        Returns: dictionary
            keys: salary category (strings)
            values: dictionary
                keys: rankings (strings)
                values: dictionary
                    keys: name of feature (string)
                    values: count of occurrence of feature (integer)
        """
        top_five_dict = {}
        for key in category_dict.keys():
            top_five_dict[key] = {}
            temp_count = {'one': 0, 'two': 0, 'three': 0, 'four': 0, 'five': 0}
            for category in category_dict[key]['data']: # for responses in each salary category
                item_count = (category_dict[key]['data'][category]) # count of feature
                if item_count > temp_count['one']: # if count is greater than largest feature
                    # move all the other features down a notch
                    temp_count['five'] = temp_count['four']
                    temp_count['four'] = temp_count['three']
                    temp_count['three'] = temp_count['two']
                    temp_count['two'] = temp_count['one']
                    temp_count['one'] = item_count # make this feature the largest feature

                elif item_count > temp_count['two']:
                    temp_count['five'] = temp_count['four']
                    temp_count['four'] = temp_count['three']
                    temp_count['three'] = temp_count['two']
                    temp_count['two'] = item_count

                elif item_count > temp_count['three']:
                    temp_count['five'] = temp_count['four']
                    temp_count['four'] = temp_count['three']
                    temp_count['three'] = item_count

                elif item_count > temp_count['four']:
                    temp_count['five'] = temp_count['four']
                    temp_count['four'] = item_count

                elif item_count > temp_count['five']:
                    temp_count['five'] = item_count

            keys = list(category_dict[key]['data'].keys()) # a list of the keys
            values = list(category_dict[key]['data'].values()) # a list of the values

            one = keys[values.index(temp_count['one'])] # finding the key associated with the value pair
            two = keys[values.index(temp_count['two'])]
            three = keys[values.index(temp_count['three'])]
            four = keys[values.index(temp_count['four'])]
            five = keys[values.index(temp_count['five'])]

            top_five_dict[key] = temp_count
            top_five_dict[key]['one'] = {one: temp_count['one']}
            top_five_dict[key]['two'] = {two: temp_count['two']}
            top_five_dict[key]['three'] = {three: temp_count['three']}
            top_five_dict[key]['four'] = {four: temp_count['four']}
            top_five_dict[key]['five'] = {five: temp_count['five']}

        return top_five_dict

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
    develop = DeveloperStats()
    filename = 'stats.csv'
    result = develop.get_column_names(filename)
    print(f' column names in {filename} are: {result}')
    print("\n")

    result = develop.categorize_data(filename)
    print(f' categorized data in {filename} is: {result}')
    print("\n")

    category_dict = develop.count_data(filename)
    print(f' counted categories in {filename} are: {category_dict}')
    print("\n")

    top_five_dict = develop.top_five(category_dict)
    print(f' the top five occurring features are {top_five_dict}')


if __name__ == '__main__':
    main()
