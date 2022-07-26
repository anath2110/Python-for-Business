
"""
Python For Loops
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
"""

"""
The range() Function
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
"""
list1=[1,"aaa",2,"bbb"]
for index in range(len(list1)):
  print(index)
  print(list1[index])
for index,elements in enumerate(list1):
  print(index)
  print(elements)
# 

"""
Nested Loops
A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop":

"""

# Example
# Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:#x=red, x=big, x=tasty
  for y in fruits:#y=apple/banana/cherry
    print(x,y)
    #red apple#red banana # red cherry 


"""
The pass Statement
for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
"""
# list1=[0,1,2]
# for x in list1:
#   print(x)

# # Example
# for x in [0, 1, 2]:
#   pass
# print("outside pass")
