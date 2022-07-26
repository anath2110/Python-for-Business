# Python - Built-In Modules
* In programming terminology, function is a separate, complete and reusable software component. Long and complex logic in a program is broken into smaller, independent and reusable blocks of instructions usually called a module, a subroutine or function. It is designed to perform a specific task that is a part of entire process. This approach towards software development is called modular programming.

* Such a program has a main routine through which smaller independent modules (functions) are called upon. Each When called, a function performs a specified task and returns the control back to the calling routine, optionally along with result of its process.

* Python interpreter has a number of built-in functions. They are always available for use in every interpreter session. Many of them have been discussed in previously. For example print() and input() for I/O, number conversion functions (int(), float(), complex()), data type conversions (list(), tuple(), set()) etc. Here is complete list of Python's built-in functions:

## Built-in Functions
abs()	delattr()	hash()	memoryview()	set()
all()	dict()	help()	min()	setattr()
any()	dir()	hex()	next()	slice()
ascii()	divmod()	id()	object()	sorted()
bin()	enumerate()	input()	oct()	staticmethod()
bool()	eval()	int()	open()	str()
breakpoint()	exec()	isinstance()	ord()	sum()
bytearray()	filter()	issubclass()	pow()	super()
bytes()	float()	iter()	print()	tuple()
callable()	format()	len()	property()	type()
chr()	frozenset()	list()	range()	vars()
classmethod()	getattr()	locals()	repr()	zip()
compile()	globals()	map()	reversed()	__import__()
complex()	hasattr()	max()

## Built-in Modules
In addition to built-in functions, a large number of pre-defined functions are also available as a part of libraries bundled with Python distributions. However they are not available for use automatically. These functions are defined in modules. A module is a file containing definition of functions, classes, variables, constants or any other Python object. Standard distribution of Python contains a large number of modules, generally known as built-in modules. Each built-in module contains resources for certain specific functionalities such as OS management, disk IO, networking, database connectivity etc.

Note: Most of the times, built-in modules are written in C and integrated with Python interpreter.

### How to use Built-in Modules
A built-in module may be a Python script (with .py extension) containing useful utilities.

To display list of all available modules, use following command in Python console:

>>> help('modules')

Resources from other modules are loaded by import statement. The general format of using a function in any module is like this:

>>>import modulename

>>>modulename.functionname([arguments if any])

**Here, we shall discuss some of the frequently used functions from certain built-in modules.**

os module

sys module

datetime module

time module

math module

random module

regex module





