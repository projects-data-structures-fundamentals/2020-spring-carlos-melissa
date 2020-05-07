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

        categorized_data = {
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

            for line in file_ref.readlines()[1:]:

                record = line.strip().split('|')

                #taking value from the salary field
                field_salary = float(record[salary_index])

                #categorizing record according to the salary range
                if field_salary <= 50000:
                    categorized_data['low_salary']['data'].append(record)

                elif field_salary <= 80000:
                    categorized_data['medium_salary']['data'].append(record)

                else:
                    categorized_data['high_salary']['data'].append(record)

        return categorized_data

    @classmethod
    def count_data(cls, categorized_data):
        """
        This methid goes though the 'data' fierld in the categorize_data 
        paramenter, which is a list of records, and count the frequency in 
        which they appear on all data within the category. it returns
        a new dictionary containing a string key for every category, and a dictionary 
        as a value which contains a 'count' (number of records/entries) on the category,
        min and max integer values (for the range), and data dictionary, which contains 
        a dictionary with the values name string as key, a the frequency in which they
        repeat within the category as a integer value 

        """
        frequency_data = {
            'low_salary': {'count': 0, 'min': 0, 'max': 50000, 'data': {}},
            'medium_salary': {'count': 0, 'min': 50001, 'max': 80000, 'data': {}},
            'high_salary':  {'count': 0, 'min': 80001, 'max': 200000, 'data': {}}
        }
    
        #iterating though the categories in data
        for category_name in categorized_data:
          
          #creating placeholder variables
          category_dict = categorized_data[category_name]
          category_data_list = category_dict['data']

          #updating count according to number of records/entries in category data
          frequency_data[category_name]['count'] = len(category_dict['data'])

          #iterating though records/entries in the current category data
          for records in category_data_list:

            #iterating though the fields of those records
            for column_index, field in enumerate(records):

              #ignore the following columns
              if column_index not in [0, 4, 6, 12]: # add any column to be ignore here (NOTE: I'm ignoring programing language for now)

                #inserting new fields into the corresponging 'data' dictionary in category if it doesnt' exit, and increment
                if field not in frequency_data[category_name]['data']:
                  frequency_data[category_name]['data'][field] = 0
                frequency_data[category_name]['data'][field] += 1

        return frequency_data

    @classmethod
    def top_five(cls, count_dict):
        """
        This method sorts through the dictionary returned from
        count_data() and determines the top five highest frequency
        fields results for each salary category.
        category_dict: the dictionary returned from count_data()
        Returns: dictionary
            keys: salary category (strings)
            values: dictionary
                keys: rankings (strings)
                values: dictionary
                    keys: name of feature (string)
                    values: count of occurrence of feature (integer)
        """
        #shallow copy works perfectly bc we actually need data dict empty
        top_five = count_dict.copy()

        for category_name in count_dict:

          category_data = count_dict[category_name]['data']
          top_five[category_name]['data'] = {}

          for tuple_field in sorted(category_data.items(), key=lambda tuple_item: tuple_item[1])[-5:]:
            field, value = tuple_field
            
            top_five[category_name]['data'][field] = value

        return top_five

    @classmethod
    def plot_data(cls, top_five_dict):
        """
        This method requires the plotly library
        This method sorts through the dictionary returned from top_five() and
        plots the occurrance of answers for each salary category
        top_five_dict: the dictionary returned from top_five()
        Returns: three plots that display the results of top_five_dict
        """

        for salary_category in top_five_dict:
          labels = []
          percentages = []

          for field_name in top_five_dict[salary_category]['data']:

            field_frequency = top_five_dict[salary_category]['data'][field_name]
            total_frequency = top_five_dict[salary_category]['count']
            
            percentage = int((field_frequency / total_frequency) * 100)
            percentages.append(percentage)

            label = field_name

            if label == 'Computer science, computer engineering, or software engineering':
                label = label[:16]
            labels.append(label + " " + str(percentage) + "%")

          #displaying data
          fig = go.Figure([go.Bar(x=labels, y=percentages)])
          #fig.update_xaxes(tickangle=10)
          fig.update_layout(
              title = (str(salary_category).replace('_', ' ') + " - top five occurring features"),
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
    # result = develop.get_column_names(filename)
    # print(f' column names in {filename} are: {result}')
    # print("\n")

    category_dict = develop.categorize_data(filename)
    # print(f' categorized data in {filename} is: {category_dict}')
    # print("\n")

    count_dict = develop.count_data(category_dict)
    # print(f' counted categories in {filename} are: {count_dict}')
    # print("\n")

    top_five_dict = develop.top_five(count_dict)
    # print(f' the top five occurring features are {top_five_dict}')
    # print('\n')

    plot = develop.plot_data(top_five_dict)
    # print(f'{plot}')

if __name__ == '__main__':
    main()
