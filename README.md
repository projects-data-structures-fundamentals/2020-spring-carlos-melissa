### project.py
Carlos Sandoval & Melissa Mullen

### Method: get_column_names():

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
### Method: count_data():

### Method: top_five():

### Method: plot_data():
