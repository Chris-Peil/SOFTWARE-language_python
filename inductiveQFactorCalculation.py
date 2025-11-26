import math
#Inductor Q Factor Calculation

# Metric Prefixes
tera = 10**12
giga = 10**9
mega = 10**6
kilo = 10**3
milli = 10**-3
micro = 10**-6
nano = 10**-9
pico = 10**-12


# Formula Parameters
freq = 200*kilo
ind = 96*micro
res = 17.7

# Formula
q_factor = (2*math.pi*freq*ind)/res

# Result
print(q_factor)
