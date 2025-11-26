# LED resistor caluclator
import math

# Voltage supply
vin = 12

# LED forward voltage
vf = 1.8 

# LED current
i = 20*10**-3

# Resistor calculation
resistor = (vin - vf)/ i
print(resistor)