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
        This method sorts through the CSV file provided from filename,
        categorizes the data into three categories: low_salary, medium_salary,
        and high_salary, and counts the occurrance of respondant's answers if __name__ == '__main__':
        each salary category
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
        # creating an array of the columns name in the csv file
        data_columns = DeveloperStats.get_column_names(filename)
        # target index for salary column
        target_column_index = 4
        # index for language column
        programming_languages_column = 12
        # opening the data file
        with open('stats.csv', 'r') as file_ref:
            # holding the frequency in which the items of the row appear this is temporal
            # bcause is going to be assigned to one of the groups we created below
            temp_frequency_holder_dic = {}
            # groups to hold the data, and has min and max baundaries as well count for analytics
            frequency_data = {
                'low_salary': {'count': 0, 'min': 0, 'max': 50000, 'data': {}},
                'medium_salary': {'count': 0, 'min': 50001, 'max': 80000, 'data': {}},
                'high_salary':  {'count': 0, 'min': 80001, 'max': 200000, 'data': {}}
            }
            # reading csv file, skiping first line bc is header (contains the column's name)
            for line in file_ref.readlines()[1:]:
                # create an array fields split by '|'
                row = line.strip().split('|')
                # taking the float value of the salary filed
                field_salary = float(row[target_column_index])

                # geting the element and index in every iteration
                for index, field in enumerate(row):
                    # get the column name from array using index
                    column_name = data_columns[index]
                    # check if the column name is not there, then create one
                    if(index not in [0, 4]):
                        if(column_name not in temp_frequency_holder_dic):
                            temp_frequency_holder_dic[column_name] = {}

                    # now that the column name it's created, filter data (skip 0=Respondent, and 4="salary", being that whe don't need to add salary to data, bc is already selected in 'field_salary' at the begining)
                    if(index not in [0, 4, 12]):
                        # if that field value is not within our data from the column in the temp variable then create one
                        if(field not in temp_frequency_holder_dic[column_name]):
                            # create the field name set it to 0
                            temp_frequency_holder_dic[column_name][field] = 0
                        # now that we have the field name just increment it by 1
                        temp_frequency_holder_dic[column_name][field] += 1
                    if(index == programming_languages_column):
                        # first check if is a special case as programming languages (this is kinda hardcoded, the optimal would be with a
                        # method that says whether or not the field contains multiple value as programming laguanges field does, for that
                        # just replace the line of code below for if (not hasMultipleValues(temp_frequency_holder_dic[column_name][field])))
                        # iterate through every field
                        list_of_languages = field.split(';')
                        for language in list_of_languages:
                            # now verify if this language is in upper level of the dictionary structure
                            if(language not in temp_frequency_holder_dic[column_name]):
                                # if is not there, then create one
                                temp_frequency_holder_dic[column_name][language] = 0
                            # increment it by 1
                            temp_frequency_holder_dic[column_name][language] += 1
                # these statements allocate the temp dictionary into the corresponding group
                # this repeats in each line the csv so that each row is sorted into a group
                if(field_salary < frequency_data['medium_salary']['min']):

                    frequency_data['low_salary']['data'] = temp_frequency_holder_dic
                    frequency_data['low_salary']['count'] += 1

                elif(field_salary < frequency_data['high_salary']['min']):

                    frequency_data['medium_salary']['data'] = temp_frequency_holder_dic
                    frequency_data['medium_salary']['count'] += 1

                else:

                    frequency_data['high_salary']['data'] = temp_frequency_holder_dic
                    frequency_data['high_salary']['count'] += 1

        # now we return the data
        return frequency_data


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
    develop = DeveloperStats()
    filename = 'stats.csv'
    # result = develop.get_column_names(filename)
    # print(f' column names in {filename} are: {result}')
    # print("\n")
    #
    result = develop.categorize_data(filename)
    print(f' example {filename} are: {result}')
    print("\n")

    # result = develop.parse_programming_languages(filename)
    # print(f' example {filename} are: {result}')

if __name__ == '__main__':
    main()
