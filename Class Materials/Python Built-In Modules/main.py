# # import datetime_time
# import custommath
# # import sys
# # import os
import regex
# import customrandom

# print(int(2.0))
# print((1.1 + 2.2) == 3.3)
# print((1.1 + 2.2))
# # print(100.000000001)
# print(complex(1.25))
# print(abs(-45.300))
import re
stri = 'From: stephen.a.smith@espn.com, drake@hotmail.com, frenchMontana@gmail.com'
stri = stri.rstrip()
print(re.findall('From:.+@', stri))