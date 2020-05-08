"""
project.py
Final project for COMP 525
Carlos Sandoval & Melissa Mullen
Updated May 7, 2020
"""
import plotly.graph_objects as go


class DeveloperStats():
    """
    Reads information from a CSV file, categorizes the data by salary, counts
    the occurrence of features, and plots the results
    """
    @classmethod
    def get_column_names(cls, filename):
        """
        This method sorts through the first line of the CSV file provided
        from filename and parses the column names into a list
        filename: name of a CSV file (string)
        returns: list of the names of the columns (strings)
        """
        with open(filename, 'r') as file_ref:
            return file_ref.readline().strip().split('|')

    @classmethod
    def categorize_data(cls, filename):
        """
        This method sorts through the CSV file provided from filename and sorts
        the responses into three categories based on their salary values:
        low_salary, medium_salary,and high_salary. Each category has min and
        max keys for the salary range as well as a data key. Data is a nested
        list of survey responses for each salary category.
        filename: name of a CSV file (string)
        returns: dictionary
            keys: salary categories (strings)
            values: dictionary
                keys: min, max, data (strings)
                values: min and max are positive integers (including zero),
                data is a nested list containing survey results (strings)
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
        This method sorts though the 'data' field in categorize_data, which is
        the dictionary returned from categorize_data(), and counts the
        frequency in which specific answers appear within the salary category.
        categorized_data: dictionary returned from categorize_data()
        Returns: dictionary
            keys: salary categories (strings)
            values: dictionary
                keys: count, min, max, data (strings)
                values: count, min, and max are positive integers (including
                zero), data is a dictionary
                    keys: survey answers (strings)
                    values: positive integers (including zero)
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
          frequency_data[category_name]['count'] = len(category_data_list)

          #iterating though records/entries in the current category data
          for records in category_data_list:

            #iterating though the fields of those records
            for column_index, field in enumerate(records):

              #ignore the following columns
              if column_index not in [0, 4, 6, 7, 10]: # add any column to be ignore here (NOTE: I'm ignoring programing language for now)

                #check whether if field contains multiple values
                if ';' in field:
                  values = field.split(';')

                  for value in values:

                    if value not in frequency_data[category_name]['data']:
                      frequency_data[category_name]['data'][value] = 0
                    frequency_data[category_name]['data'][value] += 1
                else:
                  #append on this way this if field doesn't contain multiple value
                  #inserting new fields into the corresponging 'data' dictionary in category if it doesnt' exit, and increment
                  if field not in frequency_data[category_name]['data']:
                    frequency_data[category_name]['data'][field] = 0
                  frequency_data[category_name]['data'][field] += 1

        return frequency_data


    @classmethod
    def top_five(cls, count_dict):
        """
        This method sorts through the dictionary returned from
        count_data() and determines the top five features with
        the highest frequency in each salary category.
        count_dict: the dictionary returned from count_data()
        Returns: dictionary
            keys: salary category (strings)
            values: dictionary
                keys: count, min, max, data (strings)
                values: count, min, and max are positive integers
                (including zero), data is a dictionary
                    keys: features (strings)
                    values: frequency (positive integers including zero)
        """
        #shallow copy
        top_five = count_dict.copy()

        #iterating though the categories
        for category_name in count_dict:

          #place holder variable and cleaning top_five category data
          category_data = count_dict[category_name]['data']
          top_five[category_name]['data'] = {}

          #iterates though the list of tuples resurt of the sorted function
          #that uses lambda to sort list by items, intead of keys
          for tuple_field in sorted(category_data.items(), key=lambda tuple_item: tuple_item[1])[-5:]:
            field, value = tuple_field
            #assigning top sorted features to data fields
            top_five[category_name]['data'][field] = value

        return top_five

    @classmethod
    def plot_data(cls, top_five_dict):
        """
        This method requires the plotly library
        This method sorts through the dictionary returned from top_five() and
        plots the occurrence of answers for each salary category
        top_five_dict: the dictionary returned from top_five()
        Returns: three plots that display the results of top_five_dict
        """
        #iterates through categories
        for salary_category in top_five_dict:
          #create labels and percentages for category
          labels = []
          percentages = []

          for field_name in top_five_dict[salary_category]['data']:

            #get field name and frequency for each field
            field_frequency = top_five_dict[salary_category]['data'][field_name]
            total_frequency = top_five_dict[salary_category]['count']

            #calculate percentage
            percentage = int((field_frequency / total_frequency) * 100)
            percentages.append(percentage)

            #create and format labels
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

    count_dict = develop.count_data(category_dict)
    print(f' counted categories in {filename} are: {count_dict}')
    print("\n")

    top_five_dict = develop.top_five(count_dict)
    print(f' the top five occurring features are {top_five_dict}')
    print('\n')

    plot = develop.plot_data(top_five_dict)

if __name__ == '__main__':
    main()
