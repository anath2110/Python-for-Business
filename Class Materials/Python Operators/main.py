#.................................................#
"""
Data Types
"""
#Getting the Data Type
#Print the data type of the variable x:
#uncomment 8-9 to see the output
# x = 5
# print(type(x))

#Setting the Data Type
#assign a value to a variable
#Example	Data Type	Try it
#uncomment 15-24 to see the output
# x = "Hello World"	#str	
# x = 20	#int	
# x = 20.5	#float	
# x = 1j	#complex	
# x = ["apple", "banana", "cherry"]	#list	
# x = ("apple", "banana", "cherry")	#tuple	
# x = range(6)	#range	
# x = {"name" : "John", "age" : 36}	#dict	
# x = {"apple", "banana", "cherry"}	#set
# x = True	#bool	
#specify the data type with constructor functions:
#uncomment 27-35 to see the output
#x = str("Hello World")
#print(x)
#print(type(x))	#str	
# x = int(20)	#int	
# x = float(20.5)	#float	
# x = complex(1j)	#complex	
# x = list(("apple", "banana", "cherry"))	#list	
# x = tuple(("apple", "banana", "cherry"))	#tuple	
# x = range(6)	#range	
# x = dict(name="John", age=36)	#dict	
# x = set(("apple", "banana", "cherry")) #set

#.................................................#
"""
# Casting
Specify a Variable Type : specify a type on to a variable
constructor functions:
int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
"""
# Integer
#uncomment 48-50 to see the output
# x = int(1)   # x will be 1
# y = int(2.8) # y will be 2
# z = int("3") # z will be 3
# Floats
#uncomment 53-56 to see the output
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
#Strings
#uncomment 59-61 to see the output
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
"""
User input : need to learn to be able to do the exercises
"""
#uncomment 66-67 to see the output
#stringinput=input("Enter anything: ") # By default, every user input is treated a string
# integerinput=int(input("Enter a number:"))
#.................................................#
"""
Arithmetic Operators
"""
#uncomment 73-89 , one by one to see the output
a = 20
b = 10
c = 15
d = 5
e = 0
# print(c/d)
# print(c//d)
# print(c%d)

e = (a + b) * c //d       #( 30 * 15 ) //5
print ("Value of (a + b) * c / d is ",  e)

e = ((a + b) * c) / d     # (30 * 15 ) / 5
print ("Value of ((a + b) * c) / d is ",  e)

e = (a + b) * (c / d);    # (30) * (15/5)
print ("Value of (a + b) * (c / d) is ",  e)

e = a + (b * c) / d;      #  20 + (150/5)
print ("Value of a + (b * c) / d is ",  e)
