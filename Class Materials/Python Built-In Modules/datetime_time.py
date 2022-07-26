# '''
# Python Dates
# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
# '''
# # Example
# # Import the datetime module and display the current date:
# # import datetime

# # x = datetime.datetime.now()
# # print(x)

# # The date contains year, month, day, hour, minute, second, and microsecond.

# # The datetime module has many methods to return information about the date object.

# # Here are a few examples, you will learn more about them later in this chapter:

# # Example
# # Return the year and name of weekday:

# # import datetime

# # x = datetime.datetime.now()

# # print(x.year)
# # print(x.strftime("%a"))

# # Creating Date Objects
# # To create a date, we can use the datetime() class (constructor) of the datetime module.

# # The datetime() class requires three parameters to create a date: year, month, day.

# # Example
# # Create a date object:

# # import datetime

# # x = datetime.datetime(2020, 10, 17)

# # print(x)

# # The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).

# # The strftime() Method
# # The datetime object has a method for formatting date objects into readable strings.

# # The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

# # Example
# # Display the name of the month:

# # import datetime

# # x = datetime.datetime(2018, 6, 1)

# # print(x.strftime("%B"))
# '''
# A reference of all the legal format codes:

# Directive	Description	Example	Try it
# %a	Weekday, short version	Wed	
# %A	Weekday, full version	Wednesday	
# %w	Weekday as a number 0-6, 0 is Sunday	3	
# %d	Day of month 01-31	31	
# %b	Month name, short version	Dec	
# %B	Month name, full version	December	
# %m	Month as a number 01-12	12	
# %y	Year, short version, without century	18	
# %Y	Year, full version	2018	
# %H	Hour 00-23	17	
# %I	Hour 00-12	05	
# %p	AM/PM	PM	
# %M	Minute 00-59	41	
# %S	Second 00-59	08	
# %f	Microsecond 000000-999999	548513	
# %z	UTC offset	+0100	
# %Z	Timezone	CST	
# %j	Day number of year 001-366	365	
# %U	Week number of year, Sunday as the first day of week, 00-53	52	
# %W	Week number of year, Monday as the first day of week, 00-53	52	
# %c	Local version of date and time	Mon Dec 31 17:41:00 2018	
# %C	Century	20	
# %x	Local version of date	12/31/18	
# %X	Local version of time	17:41:00	
# %%	A % character	%	
# %G	ISO 8601 year	2018	
# %u	ISO 8601 weekday (1-7)	1	
# %V	ISO 8601 weeknumber (01-53)	01
# '''

# '''
# time module
# This module has many time related functions.


# '''

# # This function returns current system time in ticks. The ticks is number of seconds elapsed after epoch time i.e. 12.00 am, January 1, 1970.

# import time
# timemodule=time.time()
# # print(timemodule)


# # localtime():

# # This function translates time in ticks in a time tuple notation.

# tk=time.time()
# localtime=time.localtime(tk)
# # structtime=time.struct_time(tm_year=2018, tm_mon=12, tm_mday=9, tm_hour=15, tm_min=11, tm_sec=25, tm_wday=6, tm_yday=343, tm_isdst=0)
# # structtime=time.struct_time(tm_year=2018, tm_mon=12)

# # print(tk)
# # print(localtime)
# # print(structtime)

# # asctime():
# # This functions returns a readable format of local time

# # tk=time.time()
# # tp=time.localtime(tk)
# # time.asctime(tp)

# # ctime():
# # This function returns string representation of system's current time

# # print(time.ctime())

# # sleep():
# # This function halts current program execution for a specified duration in seconds.
# def f1():
#   print(time.ctime())
#   time.sleep(30)
#   print(time.ctime())
# f1()
