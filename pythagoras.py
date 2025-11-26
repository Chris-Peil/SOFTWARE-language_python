# Pythagoras
import math

a = 30
b = 4
c = None

if a == None:
    a = math.sqrt(c**2 - b**2)
    print(a)

elif b == None:
    b = math.sqrt(c**2 - a**2)
    print(b)

else:
    c = math.sqrt(a**2 + b**2)
    print(c)