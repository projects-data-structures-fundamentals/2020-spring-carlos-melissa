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
    low_salary, medium_salary,and high_salary
    filename: name of a CSV file (string)
    returns: dictionary
        keys: salary category (string)
        values: dictionary
            keys: summary data from the method calculation (including count
            of responses, min salary, max salary, and data) (strings)
            values: the count of respondants (integer), minimum salary
            (integer), maximum salary (integer), and a list of lists
            containing string responses
    """
```
To create this method, we will need to use the accumulation pattern and do the following:
* Define and initialize three empty lists: **low_salary_list**, **medium_salary_list**, and **high_salary_list**. These lists will be used for sorting the survey responses into their salary categories.
* Define and initialize **frequency_data**, which is a dictionary containing the following information:
    * Three keys: **low_salary**, **medium_salary**, and **high_salary**. Each key will have a dictionary value, where the keys will be **count**, **min**, **max**, and **data**. Count is the number of survey responses in the salary category, min is the minimum salary for that category, max is the maximum salary for that category, and data is another dictionary which will contain a list of the survey responses.
    * The salary ranges are: low_salary: 0 - 50000, medium_salary: 50001 - 80000, high_salary: 80001 - 200000.
* Access the output from get_column_names() with the line `DeveloperStats.get_column_names(filename)`. Assign this output to the variable **data_columns**
* Using data columns and the index method, find the index of the ConvertedSalary column, and assign that index to the variable **salary_index**

#### Working with filename:
* Open filename in read mode as **file_ref**
* For each line after the first line:
    * Strip the line, and split it by the character "|".
    * Define and initialize the variable **field_salary**, which will be the salary value accessed through salary index
    * Delete the following rows: Respondent, ConvertedSalary, Gender, RaceEthnicity, and Age. These rows are irrelevant since we are trying to determine the top characteristics of each salary category so students will know what skills to acquire, but you can't acquire things like race and age.
*     
### Method: count_data():  

### Method: top_five():

### Method: plot_data():
