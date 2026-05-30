# Unit Converter
from length import *
from mass import *

# CLI
home = input('Choose which type of data you want to convert: 1. Length, 2. Mass, 3. Power, 4. Speed, 5. Temperature, 6. Time, 7. Volume, 8. Pression, 9. Strength, 10. Angle, 11. Area? ')

try:
    val = int(home)
except ValueError:
    print("That's not an int!")

home = int(home)

if home > 11:
    print('Select an number between 1 and 11!')

# Length
if home == 1:
    length_converter()

# Mass
if home == 2:
    mass_converter()