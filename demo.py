

def getColumnsNames(filename):
    with open(filename, 'r') as file_ref:
        return file_ref.readline().strip().split('|')


def group_by_category(filename):
    data_columns = getColumnsNames(filename)
    target_column_index = 4
    with open('stats.csv', 'r') as file_ref:
        temp_frequency_holder_dic = {}
        frequency_data = {
            'min_salary': {'count': 0, 'min': 0, 'max': 50000, 'data': {}},
            'mid_salary': {'count': 0, 'min': 50001, 'max': 80000, 'data': {}},
            'hig_salary':  {'count': 0, 'min': 80001, 'max': 200000, 'data': {}}
        }

        for line in file_ref.readlines()[1:]:

            row = line.strip().split('|')

            field_salary = float(row[target_column_index])

            for index, field in enumerate(row):
                column_name = data_columns[index]
                if(column_name not in temp_frequency_holder_dic):
                    temp_frequency_holder_dic[column_name] = {}

                # it's skipping language for now """"if(index not in [0, 4, 12]): this is for skiping programming languages( for now) and along with salary and responded which are not needed"""

                if(index not in [0, 4, 12]):
                    if(field not in temp_frequency_holder_dic[column_name]):
                        temp_frequency_holder_dic[column_name][field] = 0
                    temp_frequency_holder_dic[column_name][field] += 1

            if(field_salary < frequency_data['mid_salary']['min']):

                frequency_data['min_salary']['data'] = temp_frequency_holder_dic
                frequency_data['min_salary']['count'] += 1

            elif(field_salary < frequency_data['hig_salary']['min']):

                frequency_data['mid_salary']['data'] = temp_frequency_holder_dic
                frequency_data['mid_salary']['count'] += 1

            else:

                frequency_data['hig_salary']['data'] = temp_frequency_holder_dic
                frequency_data['hig_salary']['count'] += 1

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
