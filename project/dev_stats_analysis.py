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
        the responses into three categories based on their salary values:
        low_salary, medium_salary,and high_salary. Each category has a min, max
        for the range, and data. Where data is a nested list of records containing
        the records that belong within the category.

        filename: name of a CSV file (string)
        returns: dictionary
            keys: salary category (string)
            values:
              - type integer numbers, for max and min.
              - nested list for data 
        """

        frequency_data = {
          'low_salary': { 'min': 0, 'max': 50000, 'data': []},
          'medium_salary': { 'min': 50001, 'max': 80000, 'data': []},
          'high_salary':  { 'min': 80001, 'max': 200000, 'data': []}
        }
        #creating a list of the column names and finding index for salary column
        data_columns = cls.get_column_names(filename)
        salary_index = (data_columns.index('ConvertedSalary'))

        with open(filename, 'r') as file_ref:

            #temporal dict to store frequency of values
            temp_frequency_holder_dic = {}

            for column_index, line in enumerate(file_ref.readlines()[1:]):

                record = line.strip().split('|')

                #taking value from the salary field
                field_salary = float(record[salary_index])

                #ignore the following columns
                if column_index in [0, 3, 4, 6]: #add any column to be ignore here
                
                  #categorizing record according to the salary range
                  if field_salary <= 50000:
                      frequency_data['low_salary']['data'].append(record)

                  elif field_salary <= 80000:
                      frequency_data['medium_salary']['data'].append(record)

                  else:
                      frequency_data['high_salary']['data'].append(record)

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
        salary_count_list = []
        for salary_category in category_dict:
            frequency_data[salary_category]['count'] = (
                len(category_dict[salary_category]['data']))  # makes the count values the same as the previous method
            salary_count_list.append(
                len(category_dict[salary_category]['data']))
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

        return frequency_data, salary_count_list
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
            for category in count_dict[key]['data']: # for responses in each salary category
                item_count = (count_dict[key]['data'][category]) # count of feature
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

            keys = list(count_dict[key]['data'].keys()) # a list of the keys
            values = list(count_dict[key]['data'].values()) # a list of the values

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
    def plot_data(cls, top_five_dict, counts):
        """
        This method requires the plotly library
        This method sorts through the dictionary returned from top_five() and
        plots the occurrance of answers for each salary category
        top_five_dict: the dictionary returned from top_five()
        Returns: three plots that display the results of top_five_dict
        """
        for salary in top_five_dict:
            keys = []
            values = []
            for rankings in top_five_dict[salary]:
                counter = 0
                for data in top_five_dict[salary][rankings]:
                    rounded_value = round(top_five_dict[salary][rankings][data]/counts[counter], 4)
                    values.append(rounded_value * 100)
                    if data == 'Computer science, computer engineering, or software engineering':
                        data = 'Computer Science'
                    keys.append(data)
                counter += 1
            fig = go.Figure([go.Bar(x=keys, y=values)])
            #fig.update_xaxes(tickangle=10)
            fig.update_layout(
                title = (str(salary) + " top five occurring features"),
                xaxis_title = "Features",
                yaxis_title = "Percentages"
            )
            fig.show()
        return("Created plots")

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
    print(f' categorized data in {filename} is: {category_dict}')
    print("\n")

    count_dict, counts = develop.count_data(category_dict)
    print(f' counted categories in {filename} are: {count_dict}')
    print("\n")

    top_five_dict = develop.top_five(count_dict)
    print(f' the top five occurring features are {top_five_dict}')
    print('\n')

    plot = develop.plot_data(top_five_dict, counts)
    print(f'{plot}')

if __name__ == '__main__':
    main()
