'''
Python has a built-in module that you can use to make random numbers.
random module
Python’s standard library contains random module which defines various functions for handling randomization. Python uses a pseudo-random generator based upon Mersenne Twister algorithm that produces 53-bit precision floats. Functions in this module depend on pseudo-random number generator function random() which generates a random float number between 0.0 and 1.0.

'''

# random.random(): Returns a random float number between 0.0 to 1.0. The function doesn’t need any arguments

import random
# print(random.random())

# Other functions in random module are described here:

# random.randint(): Returns a random integer between the specified integers

# import random
# print(random.randint(1,100))

# random.randint(1,100)

# random.randrange(): Returns a random element from the range created by start, stop and step arguments. The start , stop and step parameters behave similar to range() function.

# print(random.randrange(1,10))

# print(random.randrange(1,10,2))

# print(random.randrange(0,101,10))

# random.choice(): Returns a randomly selected element from a sequence object such as string, list or tuple. An empty sequence as argument raises IndexError

# import random
# print(random.choice('computer'))

# print(random.choice([12,23,45,67,65,43]))

# print(random.choice((12,23,45,67,65,43)))

# random.shuffle(): This functions randomly reorders elements in a list.

numbers=[12,23,45,67,65,43]
# print(numbers)
random.shuffle(numbers)
# print(numbers)

#random.shuffle(numbers)
'''

The random module has a set of methods:

Method	Description
seed()	Initialize the random number generator

getstate()	Returns the current internal state of the random number generator

setstate()	Restores the internal state of the random number generator

getrandbits()	Returns a number representing the random bits

randrange()	Returns a random number between the given range

randint()	Returns a random number between the given range

choice()	Returns a random element from the given sequence

choices()	Returns a list with a random selection from the given sequence

shuffle()	Takes a sequence and returns the sequence in a random order

sample()	Returns a given sample of a sequence

random()	Returns a random float number between 0 and 1

uniform()	Returns a random float number between two given parameters

triangular()	Returns a random float number between two given parameters, you can also set a mode 
parameter to specify the midpoint between the two other parameters

betavariate()	Returns a random float number between 0 and 1 based on the Beta distribution (used in statistics)

expovariate()	Returns a random float number based on the Exponential distribution (used in statistics)

gammavariate()	Returns a random float number based on the Gamma distribution (used in statistics)

gauss()	Returns a random float number based on the Gaussian distribution (used in probability theories)

lognormvariate()	Returns a random float number based on a log-normal distribution (used in probability theories)

normalvariate()	Returns a random float number based on the normal distribution (used in probability theories)

vonmisesvariate()	Returns a random float number based on the von Mises distribution (used in directional statistics)

paretovariate()	Returns a random float number based on the Pareto distribution (used in probability theories)

weibullvariate()	Returns a random float number based on the Weibull distribution (used in statistics)
'''