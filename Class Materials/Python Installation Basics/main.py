# import this
# outputs the Zen of Python on screen

#New lines: complete a command and not semicolons ;
#print("Hello, World!") # uncomment line to see the output on console
# write anything on screen/console
#anything within double quotes in a print statement gets printed as a string on the console
#print("This is the first class") # uncomment line to see the output on console
#.................................................#
"""
# Indentation
#   indicate a block of code
#   scope of loops, functions and classes
#   whitespaces at the beginning of a code line
#   Other languages: curly-brackets, parenthesis
#   Its significant and crucial in Python
"""
# uncomment 16-17 to see the output on console
# if 5 > 2:
#   print("Five is greater than two!")
"""
Syntax Error if:
  you skip the indentation
  different number of spaces in the same block of code 
"""
#Syntax Error: No Indentation
# uncomment 25-26 to see the output on console
if 5 > 2:
 print("Five is greater than two!")
# No error: As many spaces but atleast one, in one particular block
# uncomment 29-33 to see the output on console
# if 5 > 2:
#     print("Five is greater than two!")
#     print("same block but different number of spaces")
# if(3<9):
#       print("in different block")

# Syntax Error: Difference in number of spaces within the same block
# uncomment 37-39 to see the output on console
# if 5 > 2:
#  print("Five is greater than two!")
#         print("Five is greater than two!")


def code_block():
    #Everything in this function is part of the same code #block

    print(1)

    print(2)


for i in range(4):

    #Everyting in this loop is part of the same code block

    print(i)

for i in range(4):
    print(i)
    print(i * 2)
print("Outside block")
#...................................................#
#Comments
#Python ignores
# Explain code
# Make it readable
# This is a comment
# uncomment 47 to see the output on console
#print("Below the comment")
# prevent execution when testing code.
# print("Hello, World!")
# uncomment 51 to see the output on console
#print("Cheers, Mate!")

#Multi Line Comments:
#insert a # for each line
#This is a comment
#written in
#more than just one line
# or
# triple quotes
"""
This is a comment
written in
more than just one line
"""
# uncomment 66 to see the output on console
#print("After multi-line comment")
#.................................................#
"""
Variables
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.
"""
"""
Legal Variable Names
"""
# uncomment 77-82 to see the output on console
# myvar = "John"
# myvar2 = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
"""
Illegal Variable Names
"""
# uncomment 87-89 to see the output on console
# 2myvar = "John" # Syntax Error, fix it
# my-var = "John"
# my var = "John"
"""
Multi Words Variable Names
Variable names with more than one word can be difficult to read.
"""
"""
Camel Case
Each word, except the first, starts with a capital letter.
"""
# uncomment 100 to see the output on console
myVariableName = "John"
"""
Pascal Case
Each word starts with a capital letter.
"""
# uncomment 105 to see the output on console
MyVariableName = "John"
"""
Most widely and commonly used in Python
Snake Case
Each word is separated by an underscore character.
"""
# uncomment 113 to see the output on console
my_variable_name = "John"
"""
print the variables 
"""
# uncomment 118-121 to see the output on console
# x = 5
# y = "John"
# print(x)
# print(y)
"""
Variables do not need to be declared with any particular type, and can even change type after they have been set.
"""
# uncomment 126-128 to see the output on console
# x = 4       # x is of type int
# x = "Sally" # x is now of type str
# print(x)
"""
Single or Double Quotes?
String variables can be declared either by using single or double quotes:
"""
# uncomment 135-137 to see the output on console
# x = "John"
# # is the same as
# x = 'John'

#Case-Sensitive
# uncomment 141-142 to see the output on console
# a = 4
# A = "Sally"
#A will not overwrite a
#Many Values to Multiple Variables
# uncomment 146-149 to see the output on console
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#One Value to Multiple Variables
# uncomment 152-155 to see the output on console
x = y = z = "Orange"
print(x)
print(y)
print(z)
"""
Output Variables
To combine both text and a variable, Python uses the + character:
"""
# uncomment 161-162 to see the output on console
x = "awesome"
print(x)
print("Python is " + x)

# add a variable to another variable:
# uncomment 166-169 to see the output on console
x = "Python is "
y = "awesome"
z = x + y
print(z)
#For numbers, the + character works as a mathematical operator:
# uncomment 172-174 to see the output on console
x = 5
y = 10
print(x + y)
#If you try to combine a string and a number, Python will give you an error:
# uncomment 177-179 to see the output on console
x = 5
y = "John"
print(x + y)
