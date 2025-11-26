# Parallel Resistance Calculator
import math

loop_switch = 1
resistor_count = 1
resistor_array = []

print("Type 'stop' to finish")

# Input loop to store all resistance values in array
while loop_switch == 1:
    print("Enter Resistor", resistor_count)
    resistor_value = input()
    
    # exit while loop
    if resistor_value == "stop":
        loop_switch = 0
        continue
    
    resistor_array.append(resistor_value)
    resistor_count += 1    

# Check if minimum resistors is 2
if len(resistor_array) < 2:
    print("Not enough resistors")
    exit()

# Parallel resistance calculator
array_count = 0

for value in resistor_array:
    value = 1/int(value)
    resistor_array[array_count] = value
    array_count += 1

parallel_resistance = 1/(sum(resistor_array))
print(parallel_resistance)