import math
import sympy as sym

# Calculus Calculator

# Metric Prefixes
tera = 10**12
giga = 10**9
mega = 10**6
kilo = 10**3
milli = 10**-3
micro = 10**-6
nano = 10**-9
pico = 10**-12


# Declare variables based upon expression
x = sym.symbols('x')
diff_order = 1
num_x = 2

# Expression to solve
def expression(x):
    return 8*sym.exp(-0.2*x)

# Differentiating expression with respect to x per derivative order
def derivative(x):
    return sym.diff(expression(x), x, diff_order)

# Integrating expression with respect to x between lower and upper limits
def integrate(x):
    return sym.integrate(expression(x), x)

# Subsituting number into expression
diff = derivative(x).evalf(subs={x: num_x})
integ = integrate(x).evalf(subs={x: num_x})

print(expression(x))
print(diff)
print(integ)




