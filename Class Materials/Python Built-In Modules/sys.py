'''
sys module
This module provides functions and variables used to manipulate different parts of the Python runtime environment.

sys.argv
This return list of command line arguments passed to a Python script.  Item at 0th index of this list is always the name of the script. Rest of the arguments are stored at subsequent indices.

Here is a Python script (test.py) consuming two arguments from command line.
'''

# import sys
# print ("My name is {}. I am {} years old".format(sys.argv[1], sys.argv[2]))
# This script is executed from command line as follows:

# C:\python37>python tmp.py Anil 23
# My name is Anil. I am 23 years old
# sys.exit
# This causes program to end and return to either Python console or command prompt. It is used to safely exit from program in case of exception.

# sys.maxsize
# It returns the largest integer a variable can take.

# import sys
# sys.maxsize
# 9223372036854775807
# sys.path
# This is an environment variable that returns search path for all Python modules.

# sys.path
# ['', 'C:\\python37\\Lib\\idlelib', 'C:\\python37\\python36.zip', 'C:\\python37\\DLLs', 'C:\\python37\\lib', 'C:\\python37', 'C:\\Users\\acer\\AppData\\Roaming\\Python\\Python37\\site-packages', 'C:\\python37\\lib\\site-packages']

# sys.stdin, sys.stdout, sys.stderr
# These are file objects used by the interpreter for standard input, output and errors. stdin is used for all interactive input (Python shell). stdout is used for the output of print() and of input(). The interpreter’s prompts and error messages go to stderr.

# sys.version
# This attribute displays a string containing version number of current Python interpreter.