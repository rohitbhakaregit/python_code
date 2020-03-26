"""
this is code for exception handling
not divisible by zero
-Rohit Bhakare
"""
from __future__ import print_function
X = 5
Y = 0
try:
    Z = X/Y
except ZeroDivisionError:
    print("execption:")
finally:
    print("Wont run")
