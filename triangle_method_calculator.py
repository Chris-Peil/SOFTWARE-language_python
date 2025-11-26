"""
Revision Date: 10/06/2025

This is a simple scipt used for triangle method calculations.
Two famous examples:
    1. Newtons 2nd Law - F=ma
    2. Ohms Law - v=ir


Future updates:
    A dictionary will be added for equations that have been used.
    A visual representation should be drawn

Date information:
    10/06/2025 is used to equate Ohms Law as this is what is needed currently
"""

prefix = {
    'giga'  : 10 ** 9,
    'mega'  : 10 ** 6,
    'kilo'  : 10 ** 3,
    'milli' : 10 ** -3,
    'micro' : 10 ** -6,
    'nano'  : 10 ** -9,
    'pico'  : 10 ** -12
}

suffix = {
    'giga'  : 10 ** -9,
    'mega'  : 10 ** -6,
    'kilo'  : 10 ** -3,
    'milli' : 10 ** 3,
    'micro' : 10 ** 6,
    'nano'  : 10 ** 9,
    'pico'  : 10 ** 12
}



voltage = 3.3
resistance = 10000
current = voltage/resistance


print(current * suffix.get('milli'), 'mA')


