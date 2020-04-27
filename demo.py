

def getColumnsNames(filename):
    with open(filename, 'r') as file_ref:
        return file_ref.readline().strip().split('|')


def group_by_category(filename):
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



def demo(filename):
    features_frequency = {}
    data_columns = getColumnsNames(filename)

    with open(filename, 'r') as file_ref:

        for line in file_ref.readlines()[1:]:
            row = line.strip().split('|')

            for index, field in enumerate(row):
                column_name = data_columns[index]
                if(column_name not in features_frequency):
                    features_frequency[column_name] = {}

                if(field not in features_frequency[column_name]):
                    features_frequency[column_name][field] = 0
                features_frequency[column_name][field] += 1

    return features_frequency


if __name__ == '__main__':
    # print(len(getColumnsNames('data.csv')))
    # print(demo('data.csv'))
    data = group_by_category('data.csv')
    for data_by_salaries in data:
        print(data[data_by_salaries], '\n')
