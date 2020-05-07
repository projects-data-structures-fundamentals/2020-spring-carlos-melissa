### project.py
Carlos Sandoval & Melissa Mullen

### Class: DeveloperStats():
```
class DeveloperStats():
    """
    Reads information from a CSV file, categorizes the data by salary, counts
    the occurrence of features, and plots the results
    """
```

### Method: get_column_names():
```
@classmethod
def get_column_names(cls, filename):
    """
    This method sorts through the first line of the CSV file provided
    from filename and parses the column names into a list
    filename: name of a CSV file (string)
    returns: list of strings (the names of the columns)
    """
```
This method should only require two lines of code:
* open filename in read mode
* strip the first line of the file, separate it by the character "|", and return the newly formed list

### Method: categorize_data():
```
@classmethod
def categorize_data(cls, filename):
    """
    This method sorts through the CSV file provided from filename and sorts
    the responses into three categories based on their salary values:
    low_salary, medium_salary, and high_salary. Each category has a min, max
    for the range, and data. Where data is a nested list of records containing
    the records that belong within the category.

    filename: name of a CSV file (string)
    returns: dictionary
        keys: salary category (string)
        values:
          - type integer numbers, for max and min.
          - nested list for for survey responses (strings)
    """
```
To create this method, we will need to use the accumulation pattern and do the following:
* Define and initialize **categorized_data**, which is a dictionary containing the following information:
    * Three keys: **low_salary**, **medium_salary**, and **high_salary**. Each key will have a dictionary value, where the keys will be **min**, **max**, and **data**. Min is the minimum salary for that category, max is the maximum salary for that category, and data is a list which will contain a list of the survey responses.
    * The salary ranges are: low_salary: 0 - 50000, medium_salary: 50001 - 80000, high_salary: 80001 - 200000.
* Access the output from get_column_names() with the line `cls.get_column_names(filename)`. Assign this output to the variable **data_columns**
* Using data columns and the index method, find the index of the ConvertedSalary column, and assign that index to the variable **salary_index**

#### Working with filename:
* Open filename in read mode as **file_ref**
* For each line after the first line:
    * Define and initialize an empty dictionary named **temp_frequency_holder_dic**. This dictionary will be used to temporarily store the frequency of values during the iterations.
    * Strip the line, and split it by the character "|".
    * Define and initialize the variable **field_salary**, which will be the salary value accessed through salary index
    * Use a nested conditional to check the following:
        * `if` field_salary is less than or equal to 50000, append the line to the list paired with the data key within the low_salary key of the categorized_data dictionary. AKA, `categorized_data['low_salary']['data'].append()`
        * `elif` the field_salary is less than or equal to 80000, append the line to the list paired with the data key within the medium_salary key of the categorized_data dictionary. AKA, `categorized_data['medium_salary']['data'].append()`
        * `else`, append the line to the list paired with the data key within the medium salary key of the categorize_data dictionary. AKA,    
        `categorized_data['high_salary']['data'].append()`
* After the iteration terminates, return categorized data

### Method: count_data():  

### Method: top_five():

### Method: plot_data():
