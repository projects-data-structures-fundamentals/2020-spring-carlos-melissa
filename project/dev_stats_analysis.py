
import plotly.graph_objects as go

"""
project.py
Final project for COMP 525
Carlos Sandoval & Melissa Mullen
Updated April 26, 2020
"""


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
                del row[0]  # respondant id
                del row[3]  # salary
                del row[4]  # gender
                del row[4]  # race
                del row[6]  # age
                if field_salary <= 50000:
                    # appends this response to low_salary_list
                    low_salary_list.append(row)
                    # count increases
                    frequency_data['low_salary']['count'] += 1
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
    def count_data(cls, category_dict):
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
        frequency_data = {
            'low_salary': {'count': 0, 'min': 0, 'max': 50000, 'data': {}},
            'medium_salary': {'count': 0, 'min': 50001, 'max': 80000, 'data': {}},
            'high_salary':  {'count': 0, 'min': 80001, 'max': 200000, 'data': {}}
        }
        for salary_category in category_dict:
            # makes the count values the same as the previous method
            frequency_data[salary_category]['count'] = category_dict[salary_category]['count']
            temp_frequency_holder_dic = {}
            # for responses in each salary category
            for responses in category_dict[salary_category]['data']:
                # picks out the LanguageWorkedWith column
                languages = responses[-1]
                list_of_languages = languages.split(';')  # parses it
                for language in list_of_languages:
                    # if it's not a key already...
                    if(language not in temp_frequency_holder_dic):
                        # make it a key value pair
                        temp_frequency_holder_dic[language] = 0
                    # increment by one with each occurrance
                    temp_frequency_holder_dic[language] += 1
                # for all other features except languages
                for item in responses[:-1]:
                    if(item not in temp_frequency_holder_dic):
                        temp_frequency_holder_dic[item] = 0
                    temp_frequency_holder_dic[item] += 1
            frequency_data[salary_category]['data'] = temp_frequency_holder_dic

        return frequency_data

    @classmethod
    def top_five(cls, count_dict):
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
        for key in count_dict.keys():
            top_five_dict[key] = {}
            temp_count = {'one': 0, 'two': 0, 'three': 0, 'four': 0, 'five': 0}
            # for responses in each salary category
            for category in count_dict[key]['data']:
                item_count = (count_dict[key]['data']
                              [category])  # count of feature
                # if count is greater than largest feature
                if item_count > temp_count['one']:
                    # move all the other features down a notch
                    temp_count['five'] = temp_count['four']
                    temp_count['four'] = temp_count['three']
                    temp_count['three'] = temp_count['two']
                    temp_count['two'] = temp_count['one']
                    # make this feature the largest feature
                    temp_count['one'] = item_count

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

            keys = list(count_dict[key]['data'].keys())  # a list of the keys
            # a list of the values
            values = list(count_dict[key]['data'].values())

            # finding the key associated with the value pair
            one = keys[values.index(temp_count['one'])]
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

        # for salary in top_five_dict:
        #     for rankings in top_five_dict[salary]:
        #         for data in top_five_dict[salary][rankings]:
        #             print(data)
        # animals=['giraffes', 'orangutans', 'monkeys']
        #
        # fig = go.Figure([go.Bar(x=animals, y=[20, 14, 23])])
        # fig.show()


def main():
    """
    Contains test cases for the DeveloperStats class methods
    """
    develop = DeveloperStats()
    filename = 'stats.csv'
    result = develop.get_column_names(filename)
    print(f' column names in {filename} are: {result}')
    print("\n")

    category_dict = develop.categorize_data(filename)
    print(f' categorized data in {filename} is: {result}')
    print("\n")

    count_dict = develop.count_data(category_dict)
    print(f' counted categories in {filename} are: {category_dict}')
    print("\n")

    top_five_dict = develop.top_five(count_dict)
    print(f' the top five occurring features are {top_five_dict}')
    print('\n')

    plot = develop.plot_data(top_five_dict)
    print(f' the top five occurring features are {plot}')


if __name__ == '__main__':
    main()
