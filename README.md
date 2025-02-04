### project.py
Carlos Sandoval & Melissa Mullen

### Class: DeveloperStats(): (Melissa Mullen)
```
class DeveloperStats():
    """
    Reads information from a CSV file, categorizes the data by salary, counts
    the occurrence of answers, and plots the results
    """
```

### Method: get_column_names(): (Melissa Mullen)
```
@classmethod
def get_column_names(cls, filename):
    """
    This method sorts through the first line of the CSV file provided
    from filename and parses the column names into a list
    filename: name of a CSV file (string)
    returns: list containing the names of the columns (strings)
    """
```
This method should only require two lines of code:
* open filename in read mode.
* strip the first line of the file, separate it by the character "|", and return the newly formed list.

### Method: categorize_data(): (Melissa Mullen)
```
@classmethod
def categorize_data(cls, filename):
    """
    This method sorts through the CSV file provided from filename and sorts the responses into three categories based on their salary values: low_salary, medium_salary, and high_salary. Each category has min and max keys for the salary ranges as well as a data key. Data is a nested
    list of survey responses for each salary category.
    filename: name of a CSV file (string)
    returns: dictionary
        keys: salary categories (strings)
        values: dictionary
            keys: min, max, data (strings)
            values: min and max are positive integers (including zero), data is a nested list containing survey results (strings)    
    """
```
To create this method, we will need to use the accumulation pattern and do the following:

* Define and initialize **categorized_data**, which is a dictionary containing the following information:
    * Three keys: **low_salary**, **medium_salary**, and **high_salary**. Each key will have a dictionary value, where the keys will be **min**, **max**, and **data**. Min is the minimum salary for that category, max is the maximum salary for that category, and data is a list which will contain a list of the survey responses.
    * The salary ranges are: low_salary: 0 - 50000, medium_salary: 50001 - 80000, high_salary: 80001 - 200000.

#### Working with filename:
* Open filename in read mode as **file_ref**
* Check if filename is empty. To do this, read the first character of filename, and assign it to **empty_check**.
    * if the file is not empty (`if empty_check:`), access the output from get_column_names() with the line `cls.get_column_names(filename)`. Assign this output to the variable **data_columns**. Using data columns and the index method, find the index of the ConvertedSalary column, and assign that index to the variable **salary_index**.
    * if the file is empty, assign salary_index to 4.

* For each line after the first line:
    * Strip the line, and split it by the character "|". Assign this newly formed list to the variable **record**.
    * Define and initialize the variable **field_salary**, which will be the float type salary value accessed through salary_index.
    * Use a nested conditional to check the following:
        * `if` field_salary is less than or equal to 50000, append the line to the list paired with the data key within the low_salary key of the categorized_data dictionary. AKA, `categorized_data['low_salary']['data'].append()`.
        * `elif` the field_salary is less than or equal to 80000, append the line to the list paired with the data key within the medium_salary key of the categorized_data dictionary. AKA, `categorized_data['medium_salary']['data'].append()`.
        * `else`, append the line to the list paired with the data key within the high salary key of the categorize_data dictionary. AKA,    
        `categorized_data['high_salary']['data'].append()`.

* After the iteration terminates, return categorized data.


### Method: count_data(): (Melissa Mullen)
```
@classmethod
def count_data(cls, categorized_data):
    """
    This method sorts though the 'data' field in categorized_data, which is the dictionary returned from categorize_data(), and counts the frequency in which specific answers appear within the salary category.
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
```
Similar to categorize_data(), to create this method we need to use an accumulation pattern and do the following:

* Define and initialize a dictionary named **frequency_data**. This dictionary contains the same information as categorized_data in categorize_data() when it was first initialized, except it also contains the key 'count' for each salary category. Count will be used to count the number of salary responses (integers) in each salary category.

#### Iterating through categorize_data
* Use a `for` loop to iterate through categorized_data with the loop variable **category_name**, and do the following:

* Define and initialize two placeholder variables: **category_dict** and **category_data_list**. category_dict will contain all the info from the salary_category of that iteration, or `category_dict = categorized_data[category_name]`. category_data_list contains just the dictionary paired with the data key in category_dict.
* Assign the length of category_data_list to the count key in frequency data.
* Define and initialize the variable **category_data**, and assign it to `frequency_data[category_name]['data']`. This is purely to shorten the code within the `for` loops below, since accessing the data key requires a lot of characters.
* Iterate through category_data_list with the loop variable **record**, then iterate through enumerate(record) with the following line: `for column_index, field in enumerate(records):` This line allows us to access the index as well as the actual field in record while iterating.
* Using an `if` statement, check if column_index is not 0, 4, 6, 7, or 10. We ignore the values at these indices since they contain irrelevant information, such as respondent id and age. Within this same if statement, check if ';' is in the field. If ';' is in the field, the data is from the LanguageWorkedWith column and needs to be parsed. As a whole, the if statement will look like this: `if column_index not in [0, 4, 6, 7, 10] and ';' in field:`.
    * If this condition is met, split the field by ';' and assign the new list to **values**. This split will parse the LanguageWorkedWith column.
        * Iterate through values with the loop variable **value**.
        * if value is not already a key in category_data, make it a key and assign it to the integer 0.
        * If value is already a key, increment its value by 1.
* Else, check if the column index is not 0, 4, 6, 7, or 10 (without the ';' character).
    * If this condition is met, if field is not already a key in category_data, make it a key and assign it to the integer 0.
    * If field is already a key, increment its value by 1.

* After all the iterations complete, return frequency_data.

### Method: top_five(): (Carlos Sandoval)
```
@classmethod
def top_five(cls, count_dict):
    """
    This method sorts through the dictionary returned from
    count_data() and determines the top five answers with
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
```
For this method, we start by copying the existing **count_dict** parameter in a new placeholder
local variable **top_five** which is intended to be returned after the data is processed.

* we iterate through the categories within **count_dict** and store the dictionary of features
on a new variable **category_data**, then with help of the **sorted** function we pass the
variable with a lambda function that turns the sorting key from being the standard key to be the
value, returning a list of tuples containing the dictionary key, and values in order, within the
same line we iterate though the list and with the help of a `for ... in ...` loop we create a
variable called tuple_field. from there, we extract **name** and **value** from the **tuple_field**
and add that new field to the data from within the category the outer loop is in. Finally, once the
outer loop which iterates through every category within the **count_dict** is done, the method simply
returns the local variable **top_five**


### Method: plot_data(): (Carlos Sandoval)
```
@classmethod
def plot_data(cls, top_five_dict):
    """
    This method requires the plotly library
    This method sorts through the dictionary returned from top_five() and
    plots the occurrence of answers for each salary category
    top_five_dict: the dictionary returned from top_five()
    Returns: three plots that display the results of top_five_dict
    """
```
For this method, we start by copying the existing **count_dict** parameter in a new placeholder
local variable **top_five** which is intended to be returned after the data is processed.

* For this method, we start by iterating through the categories within **top_five_dict** and
create two local variables for the `for...in..` loop we use, called **labels** and **percentages**
for each category. Then, we store field name and frequency for each field into the two variables **label** and **percentage** and after initializing them, and formatting we append them to the **labels** and **percentages**
lists. Then using the methods provided by the `plotly` library, we create a new figure, using the **Figure()**
function, passing in the **labels** and **percentages**  lists, and update the layout using the **update_layout()**
method, and finally the **show()** method to render the data in a browser window.
