"""
Week 4 practice project solution for Python Data Representation
Update syntax for print in CodeSkulptor Docs
from "print ..." syntax in Python 2 to "print(...)" syntax for Python 3
"""

# HTML tags that bounds example code
PREFIX = "<pre class='cm'>"
POSTFIX = "</pre>"
PRINT = "print"

def update_line(line):
    """
    Takes a string line representing a single line of code
    and returns a string with print updated
    """

    # count the number of spaces at the beginning
    if line.startswith(' '):
      # function to count spaces
      def spaces(word = line, c = 0):
        if word.startswith(' '):
          c += 1
        else:
          return c
        return spaces(line[c:], c = c)
      spaces = spaces()
    else:
      spaces = 0
      
    # Strip left white space using built-in string method lstrip()    
    my_stripline = line.lstrip()

    # If line is print statement,  use the format() method to add insert parentheses
    if my_stripline.startswith(PRINT):
      argument = my_stripline[len(PRINT) + 1:]
      return spaces * ' ' + 'print({})'.format(argument)

    # Note that solution does not handle white space/comments after print statememt
    return line

# Some simple tests
print(update_line(""))
print(update_line("foobar()"))  
print(update_line("print 1 + 1"))      
print(update_line("    print 2, 3, 4"))

# Expect output
##
##foobar()
##print(1 + 1)
##    print(2, 3, 4)

def update_pre_block(pre_block):
    """
    Take a string that correspond to a <pre> block in html and parses it into lines.
    Returns string corresponding to updated <pre> block with each line
    updated via process_line()
    """

    line_list = pre_block.split('\n')
    updated_block = ''
    for line in line_list:
      updated_block += update_line(line) + '\n'

    return updated_block[:len(updated_block)-1]

# Some simple tests
print(update_pre_block(""))
print(update_pre_block("foobar()"))
print(update_pre_block("if foo():\n    bar()"))
print(update_pre_block("print\nprint 1+1\nprint 2, 3, 4"))
print(update_pre_block("    print a + b\n    print 23 * 34\n        print 1234"))

# # Expected output
# ##
# ##foobar()
# ##if foo():
# ##    bar()
# ##print()
# ##print(1+1)
# ##print(2, 3, 4)
# ##    print(a + b)
# ##    print(23 * 34)
# ##        print(1234)
# 
def update_file(input_file_name, output_file_name):
    """
    Open and read the file specified by the string input_file_name
    Proces the <pre> blocks in the loaded text to update print syntax)
    Write the update text to the file specified by the string output_file_name
    """
    # open file and read text in file as a string
    with open(input_file_name) as doc_file:
        doc_text = doc_file.read()

    # split text in <pre> blocks and update using update_pre_block()
    parts = doc_text.split(PREFIX)
    updated_text = parts[0]
    for part in parts[1:]:
        updated_text += PREFIX
        [pre_block, filler] = part.split(POSTFIX, 1)
        updated_text += update_pre_block(pre_block)
        updated_text += POSTFIX
        updated_text += filler

    # Write the answer in the specified output file
    with  open(output_file_name, "w") as processed_file:
        processed_file.write(updated_text)
# 
# # A couple of test files
table_path = '2_Python_Data_Representations/Week_4/practice_project/table.mhtml'
docs_path = '2_Python_Data_Representations/Week_4/practice_project/docs.mhtml'
update_file(table_path, "2_Python_Data_Representations/Week_4/practice_project/table_updated.html")
update_file(docs_path, "2_Python_Data_Representations/Week_4/practice_project/docs_updated.html")
# 
# # Import some code to check whether the computed files are correct
WINDOW_SIZE = 10
def compare_files(file1_name, file2_name):
    """
    Given two files (whose paths are specified as strings),
    find the first location in the files that differ and
    print a small portion of both files around this location
    """

    # open and read both files
    file1 = open(file1_name)
    file2 = open(file2_name)
    file1_text = file1.read()
    file2_text = file2.read()

    smaller_length = min(len(file1_text), len(file2_text))

    for idx in range(smaller_length):
        if file1_text[idx] != file2_text[idx]:
            start_window = max(0, idx - WINDOW_SIZE)
            end_window = min(smaller_length, idx + WINDOW_SIZE)
            print("Found difference at position", idx)
            print(file1_name, "has the characters", file1_text[start_window : end_window])
            print(file2_name, "has the characters", file2_text[start_window : end_window])
            return
        
    if len(file1_text) < len(file2_text):
        print(file1_name, "is a prefix of", file2_name)
    elif len(file2_text) < len(file1_text):
        print(file2_name, "is a prefix of", file1_name)
    else:
        print(file1_name, "and", file2_name, "are the same")


table_html = '2_Python_Data_Representations/Week_4/practice_project/table_updated.html'
table_sol_html = "2_Python_Data_Representations/Week_4/practice_project/table_updated_solution.html"
compare_files(table_html, table_sol_html)

docs_html = '2_Python_Data_Representations/Week_4/practice_project/docs_updated.html'
docs_sol_html = '2_Python_Data_Representations/Week_4/practice_project/docs_updated_solution.html'
compare_files(docs_html, docs_sol_html)

# Expected output
##table_updated.html and table_updated_solution.html are the same
##docs_updated.html and docs_updated_solution.html are the same
