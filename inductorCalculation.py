import math

# Constants
permeabilityOfFreeSpace = 4*math.pi*10**-7  # Permeability of free space

# Variables
# Currently setup for the CX backplane
relativePermeability = 1                    # Permeability of air = 1
numberOfTurns = 110                        
crossSectionalAreaOfCoil = 0.02                # Unit of measurement in meters
lengthOfCoil = 0.0016                            # Unit of measurement in meters

# Calculation
inductance = (relativePermeability*permeabilityOfFreeSpace*(numberOfTurns**2)*crossSectionalAreaOfCoil)/lengthOfCoil
print(inductance)
