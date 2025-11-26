# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 09:55:32 2025

@author: Chris

AoE Exercise 1.6
"""
import math

watts = 10
volts = 115
cable_resistance_per_ft = 5*10**-8      #0.05uR


#A: Calculate the power lost per foot from "I2R losses"
current = watts/volts
ir_losses = (current**2)*cable_resistance_per_ft

print("I2R Losses:", ir_losses, "W")

#B: Calculate the length of cable over which you will lose all 10 watts
total_cable_ft = 1
cable_length_ratio = watts/ir_losses

ft_cable_length_at_10W_losses = total_cable_ft*cable_length_ratio
km_cable_length_at_10W_losses = ft_cable_length_at_10W_losses*0.0003048

print("Length of cable:", km_cable_length_at_10W_losses, "km")

#C: How hot will the cable get?
sigma = 6*10**-12

diameter_ft = 1 
diameter_cm = diameter_ft*30.48
radius_cm = diameter_cm/2 
cable_surface_area_per_cm = 2*math.pi*radius_cm*diameter_cm

# Using Stefan-Boltzmann Equation
temperature4 = ir_losses/(sigma*cable_surface_area_per_cm)
kelvin_temperature = temperature4**(1/4)
print("Cable temperature:", kelvin_temperature, "K")