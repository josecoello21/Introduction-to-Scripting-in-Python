"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
        line1 - first single line string
        line2 - second single line string
    Output:
        Returns the index where the first difference between
        line1 and line2 occurs.

        Returns IDENTICAL if the two lines are the same.
    """
    # check entry conditions 
    if line1 == line2:
        return IDENTICAL
    elif line1 == '' or line2 == '':
        return 0
      
    len_line_one, len_line_two = len(line1), len(line2)
      
    # find the index where the first difference is 
    my_range = min(len_line_one, len_line_two)
    for idx in range(my_range):
        if line1[idx] != line2[idx]:
            return idx
        elif idx == (my_range-1):
            return my_range
    
    return None 

def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
        line1 - first single line string
        line2 - second single line string
        idx   - index at which to indicate difference
    Output:
        Returns a three line formatted string showing the location
        of the first difference between line1 and line2.

        If either input line contains a newline or carriage return,
        then returns an empty string.

        If idx is not a valid index, then returns an empty string.
    """
    all_lines = line1 + line2
    if all_lines.find('\n') != -1 or all_lines.find('\r') != -1:
        return ''
    elif idx < 0 or idx > min(len(line1), len(line2)):
        return ''
    else:
        return line1 + '\n' + (idx) * "=" + '^' '\n' + line2 + '\n'

def multiline_diff(lines1, lines2):
    """
    Inputs:
        lines1 - list of single line strings
        lines2 - list of single line strings
    Output:
        Returns a tuple containing the line number (starting from 0) and
        the index in that line where the first difference between lines1
        and lines2 occurs.

        Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    # extract string contained in lists
    line1, line2 = '', ''
    for idx in lines1:
        line1 += idx
    for idx in lines2:
        line2 += idx
    
    if singleline_diff(line1 = line1, line2 = line2) == IDENTICAL:
        return (IDENTICAL, IDENTICAL)
    # check if any line is empty
    elif singleline_diff(line1 = line1, line2 = line2) == 0:
        return(0, 0)
    else:
        my_range = min(len(lines1), len(lines2))
        for idx2 in range(my_range):
            if lines1[idx2] != lines2[idx2]:
                return ( idx2, singleline_diff(lines1[idx2], lines2[idx2]) )
            elif idx2 == (my_range - 1):
                return (my_range, 0)
    
    return None

def get_file_lines(filename):
    """
    Inputs:
        filename - name of file to read
    Output:
        Returns a list of lines from the file named filename. Each
        line will be a single line string with no newline ('\n') or
        return ('\r') characters.
    
        If the file does not exist or is not readable, then the
        behavior of this function is undefined.
    """
    with open(filename, 'rt') as my_file:
        my_list = []
        for line in my_file:
            if line.find('\n') == 0 or line.find('\r') == 0:
                continue
            # remove any new line or return characters and add all lines to the list
            my_line = line.replace('\n', '')
            my_line = my_line.replace('\r', '')
            my_list.append(my_line)
    
    return my_list
  
def file_diff_format(filename1, filename2):
    """
    Inputs:
        filename1 - name of first file
        filename2 - name of second file
    Output:
        Returns a four line string showing the location of the first
        difference between the two files named by the inputs.

        If the files are identical, the function instead returns the
        string "No differences\n".

        If either file does not exist or is not readable, then the
        behavior of this function is undefined.
    """
    # we first read the files and each file is returned in a list where each 
    # element of the list is a line of the file
    file1, file2 = get_file_lines(filename1), get_file_lines(filename2)
  
    # extract the line and string index where the first difference is
    my_difference = multiline_diff(lines1 = file1, lines2 = file2)
    line = my_difference[0]
    idx = my_difference[1]

    # when both files are the same
    if my_difference == (-1, -1):
        return "No differences\n"
    # when any file is empty
    elif len(file1) == 0 or len(file2) == 0:
        first = 'Line ' + str(line) + ':\n'
        if len(file1) == 0 and len(file2) == 0:
            second = singleline_diff_format('', '', idx)
        elif len(file1) == 0:
            second = singleline_diff_format('', file2[line], idx)
        else:
            second = singleline_diff_format(file1[line], '', idx)
        return first + second
    # when the files aren't empty, but they have a difference
    else:
        first = 'Line ' + str(line) + ':\n'
        second = singleline_diff_format(file1[line], file2[line], idx)
        return first + second

# # some tests
# import os
# 
# # folder path
# dir_path = '2_Python_Data_Representations/Week_4/project_file_diff/isp_diff_files'
# my_files = []
# for i in os.listdir(dir_path):
#     if i not in my_files:
#         my_files.append(i)
# my_files.sort()
# 
# for i in range(len(my_files)):
#     if i <= len(my_files)-2:
#         print('Comparison ' + str(i))
#         print(file_diff_format(dir_path +'/'+ my_files[i], dir_path +'/'+ my_files[i+1]))
#         print('------------------------------------------------------------')
