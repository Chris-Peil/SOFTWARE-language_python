# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 12:34:14 2025

@author: Chris

AoE Q1.10 Voltage Dividers
"""

voltage_supply = 1
resistor_1 = 10*10**3
resistor_2 = 10*10**3
resistor_load = 20*10**3

#A: Find the voltage divider output
voltage_divider_output = voltage_supply*(resistor_2/(resistor_1 + resistor_2))
print("Vout:", voltage_divider_output,"v")

#B: Find the voltage divider output with a 10K load
resistor_parallel_load = (resistor_2 * resistor_load)/(resistor_2 + resistor_load)
print("Parallel load resistance:", resistor_parallel_load, "R")

voltage_divider_load = voltage_supply*(resistor_parallel_load/(resistor_1 + resistor_parallel_load))
print("Vout with load:", voltage_divider_load, 'v')


#E: Power dissipated in each resistor
#Resistor 1
total_resistance = resistor_1 + resistor_parallel_load
total_current = voltage_supply/total_resistance
Resistor_1_power = (total_current**2)*resistor_1
print("Power R1:", Resistor_1_power, "W")

#Resistor 2
resistor_2_current =  voltage_divider_load/resistor_2
resistor_2_power = (resistor_2_current**2)*resistor_2
print("Power R2:", resistor_2_power, "W")

#Resistor load
resistor_load_current =  voltage_divider_load/resistor_load
resistor_load_power = (resistor_load_current**2)*resistor_load
print("Power Rload:", resistor_load_power, "W")