import sys
sys.path.append('/app/util')  # Ensure Python knows where to look for test.py
from test import Test

val = 4
myTest = Test(val)
print(f"Square of {myTest.get_val()} is {myTest.square()}")
print(f"Double of {myTest.get_val()} is {myTest.double()}")
