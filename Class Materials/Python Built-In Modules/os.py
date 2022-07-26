'''
os module
This module has functions to perform many tasks of operating system.
'''
# mkdir():
# We can create a new directory using mkdir() function from os module.

# import os
# os.mkdir("d:\\tempdir")
# A new directory corresponding to path in string argument in the function will be created. If we open D drive in Windows explorer we should notice tempdir folder created.

# chdir():
# To change current working directory to use chdir() function.

# import os
# os.chdir("d:\\temp")
# getcwd():os.chdir("d:\\temp")
# getcwd():
# This function in returns name off current working directory.

# os.getcwd()
# 'd:\\temp'
# Directory paths can also be relative. If current directory is set to D drive and then to temp without mentioning preceding path, then also current working directory will be changed to d:\temp

# os.chdir("d:\\")
# os.getcwd()
# 'd:\\'
# os.chdir("temp")
# os.getcwd()
# 'd:\\temp'
# In order to set current directory to parent directory use ".." as the argument to chdir() function.

# os.chdir("d:\\temp")
# os.getcwd()
# 'd:\\temp'
# os.chdir("..")
# os.getcwd()
# 'd:\\'
# rmdir():
# The rmdir() function in os module removes a specified directory either with absolute or relative path. However it should not be the current working directory and it should be empty.

# os.chdir("tempdir")
# os.getcwd()
# 'd:\\tempdir'
# os.rmdir("d:\\temp")
# PermissionError: [WinError 32] The process cannot access the file because it is being used by another process: 'd:\\temp'
# os.chdir("..")
# os.rmdir("temp")
# listdir():
# The os module has listdir() function which returns list of all files in specified directory.

# os.listdir("c:\\Users")os.listdir("c:\\Users")
# ['ani', 'All Users', 'Default', 'Default User', 'desktop.ini', 'Public']