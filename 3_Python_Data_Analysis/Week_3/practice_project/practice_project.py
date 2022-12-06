"""
Week 3 practice project template for Python Data Analysis
Reading and writing CSV files using lists
"""


import csv
path = '3_Python_Data_Analysis/Week_3/practice_project/cancer_risk05_v4_county.csv'
path_to_write = '3_Python_Data_Analysis/Week_3/practice_project/cancer_risk05_v4_county_copy.csv'
path_test = '3_Python_Data_Analysis/Week_3/practice_project/test_case.csv'
#########################################################
# Part 1 - Week 3



def print_table(table):
    """
    Echo a nested listto the console
    """
    for row in table:
        print(row)


def read_csv_file(file_name):
    """
    Given a CSV file, read the data into a nested list
    Input: String corresponding to comma-separated  CSV file
    Output: Lists of lists consisting of the fields in the CSV file
    """
    table = []
    with open(file_name, 'r', newline = '') as csvfile:
        csv_file = csv.reader(csvfile, skipinitialspace = True)
        for line in csv_file:
            table.append(line)
    return table



def write_csv_file(csv_table, file_name):
    """
    Input: Nested list csv_table and a string file_name
    Action: Write fields in csv_table into a comma-separated CSV file with the name file_name
    """
    with open(file_name, 'w', newline = '') as csvfile:
        csv_file = csv.writer(csvfile, delimiter = ',')
        for row in csv_table:
            csv_file.writerow(row)
    
def test_part1_code(file_name, copy_file_name, test_file):
    """
    Run examples that test the functions for part 1
    """
    
    # Simple test for reader
    test_table = read_csv_file(test_file)  # create a small CSV for this test
    print_table(test_table)
    print()

    # Test the writer
    cancer_risk_table = read_csv_file(file_name)
    write_csv_file(cancer_risk_table, copy_file_name)
    cancer_risk_copy = read_csv_file(copy_file_name)
    
    # Test whether two tables are the same

test_part1_code(file_name = path, copy_file_name = path_to_write, test_file = path_test)


# some extra tests
original_file = read_csv_file(file_name = path)
copy_file = read_csv_file(file_name = path_to_write)

count = 0
for item in range(len(copy_file)):
    count += original_file[item] == copy_file[item]

count == len(copy_file) == len(original_file)

