# -*- coding: utf-8 -*-
"""
VOM Calculations

AoE Q1.8
"""

meter_movement_current = 50*10**-6
meter_movement_resistance = 5000
meter_voltage_range = meter_movement_current*meter_movement_resistance
print("Meter voltage range:", meter_voltage_range, "v")

#A: What shunt reistance is needed to convert the meter from 50uA to 1A
meter_current_measurement = 1

# This is incorrect
# shunt_resistor = meter_current_measurement/meter_movement_current

shunt_current = meter_current_measurement - meter_movement_current
shunt_resistor = meter_voltage_range/shunt_current
print("Shunt resistor:", shunt_resistor, "R")

#B: What series resistance is needed to convert the meter from 0.3v to 10v
meter_voltage_measurement = 10

# This is incorrect
#meter_series_resistor = meter_voltage_measurement/meter_movement_current

total_resistance = meter_voltage_measurement/meter_movement_current
series_resistor = total_resistance - meter_movement_resistance
print("Series resistor:", series_resistor, "R")