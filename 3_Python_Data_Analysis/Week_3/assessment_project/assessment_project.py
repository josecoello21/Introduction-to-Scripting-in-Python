"""
Project for Week 3 of "Python Data Analysis".
Read and write CSV files using a dictionary of dictionaries.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv

def read_csv_fieldnames(filename, separator = ',', quote = '"'):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Ouput:
      A list of strings corresponding to the field names in
      the given CSV file.
    """
    
    with open(filename, newline = '') as csvfile:
        csv_file = csv.DictReader(csvfile, delimiter = separator, 
                                  quotechar = quote)
        names = csv_file.fieldnames
        return names

# # some tests
# import os
# 
# # folder path
# dir_path = '3_Python_Data_Analysis/Week_3/assessment_project'
# my_files = []
# for file in os.listdir(dir_path):
#     if file not in my_files and '.csv' in file:
#         my_files.append(dir_path + '/' + file)
# my_files.sort()
# 
# for file in my_files:
#     print(read_csv_fieldnames(file, ',', quote='"'))

def read_csv_as_list_dict(filename, separator = ',', quote = '"'):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
    with open(filename, newline = '') as csvfile:
        csv_file = csv.DictReader(csvfile, delimiter = separator, 
                                  quotechar = quote)
        my_list = []
        for line in csv_file:
            my_list.append(line)
    return my_list

# with open(my_files[3], newline = '') as csvfile:
#     csv_file = csv.DictReader(csvfile, delimiter = ',', quotechar = '"')
#     for line in csv_file:
#         print(line)

def read_csv_as_nested_dict(filename, keyfield = 0, separator = ',', quote = '"'):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    with open(filename, newline = '') as csvfile:
        csv_file = csv.DictReader(csvfile, delimiter = separator, quotechar = quote)
        # check the index of the column whose values will be used as row keys 
        names = csv_file.fieldnames
        idx = names.index(keyfield)
        my_dict = {}
        
        for line in csv_file:
            key = list(line.values())[idx]
            my_dict[key] = line
            
    return my_dict
# 
# 
def write_csv_from_list_dict(filename, table, fieldnames = None, 
                             separator = ',', quote = '"', 
                             quotestrategy = csv.QUOTE_NONNUMERIC):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """
    with open(filename, 'w', newline = '') as csvtable:
        if fieldnames is None:
            fieldnames = list(table[0].keys())
        
        csv_write = csv.DictWriter(f=csvtable, fieldnames = fieldnames, 
                                   delimiter = separator, quotechar = quote, 
                                   quoting = quotestrategy)
        csv_write.writeheader()
        for row in table:
            csv_write.writerow(row)
            
