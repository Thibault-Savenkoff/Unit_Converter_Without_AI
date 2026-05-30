# Unit Converter


# Maths Code

# Mass

# Grams

# Grams to Kilograms
def g_to_kg(x):
    sum = float(x) / float(10**(3))
    return str(sum)

# Grams to Pounds
def g_to_lb(x):
    sum = float(x) / float(453.59237)
    return str(sum)

# Grams to Ounces
def g_to_oz(x):
    sum = float(x) / float(28.34952)
    return str(sum)

# Grams to Carats
def g_to_ct(x):
    sum = float(x) * float(5)
    return str(sum)

# Kilograms

# Kilograms to Grams
def kg_to_g(x):
    sum = float(x) * float(10**(3))
    return str(sum)

# Kilograms to Pounds
def kg_to_lb(x):
    sum = float(x) / float(0.45359237)
    return str(sum)

# Kilograms to Ounces
def kg_to_oz(x):
    sum = float(x) * float(35.27396195)
    return str(sum)

# Kilograms to Carats
def kg_to_ct(x):
    sum = float(x) * float(5*10**3)
    return str(sum)

# Pounds

# Pounds to Grams
def lb_to_g(x):
    sum = float(x) * float(453.59290944)
    return str(sum)

# Pounds to Kilograms
def lb_to_kg(x):
    sum = float(x) / float(2.20462)
    return str(sum)

# Pounds to Ounces
def lb_to_oz(x):
    sum = float(x) * float(16)
    return str(sum)

# Pounds to Carats
def lb_to_ct(x):
    sum = float(x) * float(2267.96454718)
    return str(sum)

# Ounces

# Ounces to Grams
def oz_to_g(x):
    sum = float(x) * float(28.34949254)
    return str(sum)

# Ounces to Kilograms
def oz_to_kg(x):
    sum = float(x) / float(35.27400317)
    return str(sum)

# Ounces to Pounds
def oz_to_lb(x):
    sum = float(x) / float(16)
    return str(sum)

# Ounces to Carats
def oz_to_ct(x):
    sum = float(x) * float(141.74746272)
    return str(sum)

# Carats

# Carats to Grams
def ct_to_g(x):
    sum = float(x) / float(5)
    return str(sum)

# Carats to Kilograms
def ct_to_kg(x):
    sum = float(x) / float(5*10**3)
    return str(sum)

# Carats to Pounds
def ct_to_lb(x):
    sum = float(x) / float(2267.98512202)
    return str(sum)

# Carats to Ounces
def ct_to_oz(x):
    sum = float(x) / float(141.74746272)
    return str(sum)

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
    length_input = input('Select your length unit: nm, µm, mm, cm, dm, m, km, in, ft, yd, mi, nmi, au, ly or pc? ')
    length_input_list = ['nm', 'µm', 'mm', 'cm', 'dm', 'm', 'km', 'in', 'ft', 'yd', 'mi', 'nmi', 'au', 'ly', 'pc']
    if length_input in length_input_list:
        length_output_list = ['nm', 'µm', 'mm', 'cm', 'dm', 'm', 'km', 'in', 'ft', 'yd', 'mi', 'nmi', 'au', 'ly', 'pc']
        length_output_list.remove(length_input)
        length_output_list_question = length_output_list[0] + ", " + length_output_list[1] + ", " + length_output_list[2] + ", " + length_output_list[3]
        length_output = input('Select the length unit you want: ' + str(length_output_list_question) + "? ")
        if length_output in length_output_list:
            data = input('Enter your length: ')
            # Nanometers
            # Nanometers to Micrometers
            if length_input == length_input_list[0] and length_output == length_output_list[0]:
                print('Result: ' + nm_to_µm(data) + " " + length_output)
            # Nanometers to Millimeters
            if length_input == length_input_list[0] and length_output == length_output_list[1]:
                print('Result: ' + nm_to_mm(data) + " " + length_output)
            # Nanometers to Centimeters
            if length_input == length_input_list[0] and length_output == length_output_list[2]:
                print('Result: ' + nm_to_cm(data) + " " + length_output)
            # Nanometers to Decimeters
            if length_input == length_input_list[0] and length_output == length_output_list[3]:
                print('Result: ' + nm_to_dm(data) + " " + length_output)
            # Nanometers to Meters
            if length_input == length_input_list[0] and length_output == length_output_list[4]:
                print('Result: ' + nm_to_m(data) + " " + length_output)
            # Nanometers to Kilometers
            if length_input == length_input_list[0] and length_output == length_output_list[5]:
                print('Result: ' + nm_to_km(data) + " " + length_output)
            # Nanometers to Inchs
            if length_input == length_input_list[0] and length_output == length_output_list[6]:
                print('Result: ' + nm_to_in(data) + " " + length_output)
            # Nanometers to Feet
            if length_input == length_input_list[0] and length_output == length_output_list[7]:
                print('Result: ' + nm_to_ft(data) + " " + length_output)
            # Nanometers to Yards
            if length_input == length_input_list[0] and length_output == length_output_list[8]:
                print('Result: ' + nm_to_yd(data) + " " + length_output)
            # Nanometers to Miles
            if length_input == length_input_list[0] and length_output == length_output_list[9]:
                print('Result: ' + nm_to_mi(data) + " " + length_output)
            # Nanometers to Nautical miles
            if length_input == length_input_list[0] and length_output == length_output_list[10]:
                print('Result: ' + nm_to_nmi(data) + " " + length_output)
            # Nanometers to Astronomical units
            if length_input == length_input_list[0] and length_output == length_output_list[11]:
                print('Result: ' + nm_to_au(data) + " " + length_output)
            # Nanometers to Light-years
            if length_input == length_input_list[0] and length_output == length_output_list[12]:
                print('Result: ' + nm_to_ly(data) + " " + length_output)
            # Nanometers to Parsecs
            if length_input == length_input_list[0] and length_output == length_output_list[13]:
                print('Result: ' + nm_to_pc(data) + " " + length_output)

            # Micrometers
            # Micrometers to Nanometers
            if length_input == length_input_list[1] and length_output == length_output_list[0]:
                print('Result: ' + µm_to_nm(data) + " " + length_output)
            # Micrometers to Millimeters
            if length_input == length_input_list[1] and length_output == length_output_list[1]:
                print('Result: ' + µm_to_mm(data) + " " + length_output)
            # Micrometers to Centimeters
            if length_input == length_input_list[1] and length_output == length_output_list[2]:
                print('Result: ' + µm_to_cm(data) + " " + length_output)
            # Micrometers to Decimeters
            if length_input == length_input_list[1] and length_output == length_output_list[3]:
                print('Result: ' + µm_to_dm(data) + " " + length_output)
            # Micrometers to Meters
            if length_input == length_input_list[1] and length_output == length_output_list[4]:
                print('Result: ' + µm_to_m(data) + " " + length_output)
            # Micrometers to Kilometers
            if length_input == length_input_list[1] and length_output == length_output_list[5]:
                print('Result: ' + µm_to_km(data) + " " + length_output)
            # Micrometers to Inchs
            if length_input == length_input_list[1] and length_output == length_output_list[6]:
                print('Result: ' + µm_to_in(data) + " " + length_output)
            # Micrometers to Feet
            if length_input == length_input_list[1] and length_output == length_output_list[7]:
                print('Result: ' + µm_to_ft(data) + " " + length_output)
            # Micrometers to Yards
            if length_input == length_input_list[1] and length_output == length_output_list[8]:
                print('Result: ' + µm_to_yd(data) + " " + length_output)
            # Micrometers to Miles
            if length_input == length_input_list[1] and length_output == length_output_list[9]:
                print('Result: ' + µm_to_mi(data) + " " + length_output)
            # Micrometers to Nautical miles
            if length_input == length_input_list[1] and length_output == length_output_list[10]:
                print('Result: ' + µm_to_nmi(data) + " " + length_output)
            # Micrometers to Astronomical units
            if length_input == length_input_list[1] and length_output == length_output_list[11]:
                print('Result: ' + µm_to_au(data) + " " + length_output)
            # Micrometers to Light-years
            if length_input == length_input_list[1] and length_output == length_output_list[12]:
                print('Result: ' + µm_to_ly(data) + " " + length_output)
            # Micrometers to Parsecs
            if length_input == length_input_list[1] and length_output == length_output_list[13]:
                print('Result: ' + µm_to_pc(data) + " " + length_output)

            # Millimeters
            # Millimeters to Nanometers
            if length_input == length_input_list[2] and length_output == length_output_list[0]:
                print('Result: ' + mm_to_nm(data) + " " + length_output)
            # Millimeters to Micrometers
            if length_input == length_input_list[2] and length_output == length_output_list[1]:
                print('Result: ' + mm_to_µm(data) + " " + length_output)
            # Millimeters to Centimeters
            if length_input == length_input_list[2] and length_output == length_output_list[2]:
                print('Result: ' + mm_to_cm(data) + " " + length_output)
            # Millimeters to Decimeters
            if length_input == length_input_list[2] and length_output == length_output_list[3]:
                print('Result: ' + mm_to_dm(data) + " " + length_output)
            # Millimeters to Meters
            if length_input == length_input_list[2] and length_output == length_output_list[4]:
                print('Result: ' + mm_to_m(data) + " " + length_output)
            # Millimeters to Kilometers
            if length_input == length_input_list[2] and length_output == length_output_list[5]:
                print('Result: ' + mm_to_km(data) + " " + length_output)
            # Millimeters to Inchs
            if length_input == length_input_list[2] and length_output == length_output_list[6]:
                print('Result: ' + mm_to_in(data) + " " + length_output)
            # Millimeters to Feet
            if length_input == length_input_list[2] and length_output == length_output_list[7]:
                print('Result: ' + mm_to_ft(data) + " " + length_output)
            # Millimeters to Yards
            if length_input == length_input_list[2] and length_output == length_output_list[8]:
                print('Result: ' + mm_to_yd(data) + " " + length_output)
            # Millimeters to Miles
            if length_input == length_input_list[2] and length_output == length_output_list[9]:
                print('Result: ' + mm_to_mi(data) + " " + length_output)
            # Millimeters to Nautical miles
            if length_input == length_input_list[2] and length_output == length_output_list[10]:
                print('Result: ' + mm_to_nmi(data) + " " + length_output)
            # Millimeters to Astronomical units
            if length_input == length_input_list[2] and length_output == length_output_list[11]:
                print('Result: ' + mm_to_au(data) + " " + length_output)
            # Millimeters to Light-years
            if length_input == length_input_list[2] and length_output == length_output_list[12]:
                print('Result: ' + mm_to_ly(data) + " " + length_output)
            # Millimeters to Parsecs
            if length_input == length_input_list[2] and length_output == length_output_list[13]:
                print('Result: ' + mm_to_pc(data) + " " + length_output)

            # Centimeters
            # Centimeters to Nanometers
            if length_input == length_input_list[3] and length_output == length_output_list[0]:
                print('Result: ' + cm_to_nm(data) + " " + length_output)
            # Centimeters to Micrometers
            if length_input == length_input_list[3] and length_output == length_output_list[1]:
                print('Result: ' + cm_to_µm(data) + " " + length_output)
            # Centimeters to Millimeters
            if length_input == length_input_list[3] and length_output == length_output_list[2]:
                print('Result: ' + cm_to_mm(data) + " " + length_output)
            # Centimeters to Decimeters
            if length_input == length_input_list[3] and length_output == length_output_list[3]:
                print('Result: ' + cm_to_dm(data) + " " + length_output)
            # Centimeters to Meters
            if length_input == length_input_list[3] and length_output == length_output_list[4]:
                print('Result: ' + cm_to_m(data) + " " + length_output)
            # Centimeters to Kilometers
            if length_input == length_input_list[3] and length_output == length_output_list[5]:
                print('Result: ' + cm_to_km(data) + " " + length_output)
            # Centimeters to Inchs
            if length_input == length_input_list[3] and length_output == length_output_list[6]:
                print('Result: ' + cm_to_in(data) + " " + length_output)
            # Centimeters to Feet
            if length_input == length_input_list[3] and length_output == length_output_list[7]:
                print('Result: ' + cm_to_ft(data) + " " + length_output)
            # Centimeters to Yards
            if length_input == length_input_list[3] and length_output == length_output_list[8]:
                print('Result: ' + cm_to_yd(data) + " " + length_output)
            # Centimeters to Miles
            if length_input == length_input_list[3] and length_output == length_output_list[9]:
                print('Result: ' + cm_to_mi(data) + " " + length_output)
            # Centimeters to Nautical miles
            if length_input == length_input_list[3] and length_output == length_output_list[10]:
                print('Result: ' + cm_to_nmi(data) + " " + length_output)
            # Centimeters to Astronomical units
            if length_input == length_input_list[3] and length_output == length_output_list[11]:
                print('Result: ' + cm_to_au(data) + " " + length_output)
            # Centimeters to Light-years
            if length_input == length_input_list[3] and length_output == length_output_list[12]:
                print('Result: ' + cm_to_ly(data) + " " + length_output)
            # Centimeters to Parsecs
            if length_input == length_input_list[3] and length_output == length_output_list[13]:
                print('Result: ' + cm_to_pc(data) + " " + length_output)

            # Decimeters
            # Decimeters to Nanometers
            if length_input == length_input_list[4] and length_output == length_output_list[0]:
                print('Result: ' + dm_to_nm(data) + " " + length_output)
            # Decimeters to Micrometers
            if length_input == length_input_list[4] and length_output == length_output_list[1]:
                print('Result: ' + dm_to_µm(data) + " " + length_output)
            # Decimeters to Millimeters
            if length_input == length_input_list[4] and length_output == length_output_list[2]:
                print('Result: ' + dm_to_mm(data) + " " + length_output)
            # Decimeters to Centimeters
            if length_input == length_input_list[4] and length_output == length_output_list[3]:
                print('Result: ' + dm_to_cm(data) + " " + length_output)
            # Decimeters to Meters
            if length_input == length_input_list[4] and length_output == length_output_list[4]:
                print('Result: ' + dm_to_m(data) + " " + length_output)
            # Decimeters to Kilometers
            if length_input == length_input_list[4] and length_output == length_output_list[5]:
                print('Result: ' + dm_to_km(data) + " " + length_output)
            # Decimeters to Inchs
            if length_input == length_input_list[4] and length_output == length_output_list[6]:
                print('Result: ' + dm_to_in(data) + " " + length_output)
            # Decimeters to Feet
            if length_input == length_input_list[4] and length_output == length_output_list[7]:
                print('Result: ' + dm_to_ft(data) + " " + length_output)
            # Decimeters to Yards
            if length_input == length_input_list[4] and length_output == length_output_list[8]:
                print('Result: ' + dm_to_yd(data) + " " + length_output)
            # Decimeters to Miles
            if length_input == length_input_list[4] and length_output == length_output_list[9]:
                print('Result: ' + dm_to_mi(data) + " " + length_output)
            # Decimeters to Nautical miles
            if length_input == length_input_list[4] and length_output == length_output_list[10]:
                print('Result: ' + dm_to_nmi(data) + " " + length_output)
            # Decimeters to Astronomical units
            if length_input == length_input_list[4] and length_output == length_output_list[11]:
                print('Result: ' + dm_to_au(data) + " " + length_output)
            # Decimeters to Light-years
            if length_input == length_input_list[4] and length_output == length_output_list[12]:
                print('Result: ' + dm_to_ly(data) + " " + length_output)
            # Decimeters to Parsecs
            if length_input == length_input_list[4] and length_output == length_output_list[13]:
                print('Result: ' + dm_to_pc(data) + " " + length_output)

            # Meters
            # Meters to Nanometers
            if length_input == length_input_list[5] and length_output == length_output_list[0]:
                print('Result: ' + m_to_nm(data) + " " + length_output)
            # Meters to Micrometers
            if length_input == length_input_list[5] and length_output == length_output_list[1]:
                print('Result: ' + m_to_µm(data) + " " + length_output)
            # Meters to Millimeters
            if length_input == length_input_list[5] and length_output == length_output_list[2]:
                print('Result: ' + m_to_mm(data) + " " + length_output)
            # Meters to Centimeters
            if length_input == length_input_list[5] and length_output == length_output_list[3]:
                print('Result: ' + m_to_cm(data) + " " + length_output)
            # Meters to Decimeters
            if length_input == length_input_list[5] and length_output == length_output_list[4]:
                print('Result: ' + m_to_dm(data) + " " + length_output)
            # Meters to Kilometers
            if length_input == length_input_list[5] and length_output == length_output_list[5]:
                print('Result: ' + m_to_km(data) + " " + length_output)
            # Meters to Inchs
            if length_input == length_input_list[5] and length_output == length_output_list[6]:
                print('Result: ' + m_to_in(data) + " " + length_output)
            # Meters to Feet
            if length_input == length_input_list[5] and length_output == length_output_list[7]:
                print('Result: ' + m_to_ft(data) + " " + length_output)
            # Meters to Yards
            if length_input == length_input_list[5] and length_output == length_output_list[8]:
                print('Result: ' + m_to_yd(data) + " " + length_output)
            # Meters to Miles
            if length_input == length_input_list[5] and length_output == length_output_list[9]:
                print('Result: ' + m_to_mi(data) + " " + length_output)
            # Meters to Nautical miles
            if length_input == length_input_list[5] and length_output == length_output_list[10]:
                print('Result: ' + m_to_nmi(data) + " " + length_output)
            # Meters to Astronomical units
            if length_input == length_input_list[5] and length_output == length_output_list[11]:
                print('Result: ' + m_to_au(data) + " " + length_output)
            # Meters to Light-years
            if length_input == length_input_list[5] and length_output == length_output_list[12]:
                print('Result: ' + m_to_ly(data) + " " + length_output)
            # Meters to Parsecs
            if length_input == length_input_list[5] and length_output == length_output_list[13]:
                print('Result: ' + m_to_pc(data) + " " + length_output)

            # Kilometers
            # Kilometers to Nanometers
            if length_input == length_input_list[6] and length_output == length_output_list[0]:
                print('Result: ' + km_to_nm(data) + " " + length_output)
            # Kilometers to Micrometers
            if length_input == length_input_list[6] and length_output == length_output_list[1]:
                print('Result: ' + km_to_µm(data) + " " + length_output)
            # Kilometers to Millimeters
            if length_input == length_input_list[6] and length_output == length_output_list[2]:
                print('Result: ' + km_to_mm(data) + " " + length_output)
            # Kilometers to Centimeters
            if length_input == length_input_list[6] and length_output == length_output_list[3]:
                print('Result: ' + km_to_cm(data) + " " + length_output)
            # Kilometers to Decimeters
            if length_input == length_input_list[6] and length_output == length_output_list[4]:
                print('Result: ' + km_to_dm(data) + " " + length_output)
            # Kilometers to Meters
            if length_input == length_input_list[6] and length_output == length_output_list[5]:
                print('Result: ' + km_to_m(data) + " " + length_output)
            # Kilometers to Inchs
            if length_input == length_input_list[6] and length_output == length_output_list[6]:
                print('Result: ' + km_to_in(data) + " " + length_output)
            # Kilometers to Feet
            if length_input == length_input_list[6] and length_output == length_output_list[7]:
                print('Result: ' + km_to_ft(data) + " " + length_output)
            # Kilometers to Yards
            if length_input == length_input_list[6] and length_output == length_output_list[8]:
                print('Result: ' + km_to_yd(data) + " " + length_output)
            # Kilometers to Miles
            if length_input == length_input_list[6] and length_output == length_output_list[9]:
                print('Result: ' + km_to_mi(data) + " " + length_output)
            # Kilometers to Nautical miles
            if length_input == length_input_list[6] and length_output == length_output_list[10]:
                print('Result: ' + km_to_nmi(data) + " " + length_output)
            # Kilometers to Astronomical units
            if length_input == length_input_list[6] and length_output == length_output_list[11]:
                print('Result: ' + km_to_au(data) + " " + length_output)
            # Kilometers to Light-years
            if length_input == length_input_list[6] and length_output == length_output_list[12]:
                print('Result: ' + km_to_ly(data) + " " + length_output)
            # Kilometers to Parsecs
            if length_input == length_input_list[6] and length_output == length_output_list[13]:
                print('Result: ' + km_to_pc(data) + " " + length_output)

# Mass
if home == 2:
    mass_input = input('Select your mass unit: g, kg, lb, oz or ct? ')
    mass_input_list = ['g', 'kg', 'lb', 'oz', 'ct']
    if mass_input in mass_input_list:
        mass_output_list = ['g', 'kg', 'lb', 'oz', 'ct']
        mass_output_list.remove(mass_input)
        mass_output_list_question = mass_output_list[0] + ", " + mass_output_list[1] + ", " + mass_output_list[2] + ", " + mass_output_list[3]
        mass_output = input('Select the mass unit you want: ' + str(mass_output_list_question) + "? ")
        if mass_output in mass_output_list:
            data = input('Enter your mass: ')
            # Grams
            # Grams to Kilograms
            if mass_input == mass_input_list[0] and mass_output == mass_output_list[0]:
                print('Result: ' + g_to_kg(data) + " " + mass_output)
            # Grams to Pounds
            if mass_input == mass_input_list[0] and mass_output == mass_output_list[1]:
                print('Result: ' + g_to_lb(data) + " " + mass_output)
            # Grams to Ounces
            if mass_input == mass_input_list[0] and mass_output == mass_output_list[2]:
                print('Result: ' + g_to_oz(data) + " " + mass_output)
            # Grams to Carats
            if mass_input == mass_input_list[0] and mass_output == mass_output_list[3]:
                print('Result: ' + g_to_ct(data) + " " + mass_output)

            # Kilograms
            # Kilograms to Grams
            if mass_input == mass_input_list[1] and mass_output == mass_output_list[0]:
                print('Result: ' + kg_to_g(data) + " " + mass_output)
            # Kilograms to Pounds
            if mass_input == mass_input_list[1] and mass_output == mass_output_list[1]:
                print('Result: ' + kg_to_lb(data) + " " + mass_output)
            # Kilograms to Ounces
            if mass_input == mass_input_list[1] and mass_output == mass_output_list[2]:
                print('Result: ' + kg_to_oz(data) + " " + mass_output)
            # Kilograms to Carats
            if mass_input == mass_input_list[1] and mass_output == mass_output_list[3]:
                print('Result: ' + kg_to_ct(data) + " " + mass_output)

            # Pounds
            # Pounds to Grams
            if mass_input == mass_input_list[2] and mass_output == mass_output_list[0]:
                print('Result: ' + lb_to_g(data) + " " + mass_output)
            # Pounds to Kilograms
            if mass_input == mass_input_list[2] and mass_output == mass_output_list[1]:
                print('Result: ' + lb_to_kg(data) + " " + mass_output)
            # Pounds to Ounces
            if mass_input == mass_input_list[2] and mass_output == mass_output_list[2]:
                print('Result: ' + lb_to_oz(data) + " " + mass_output)
            # Pounds to Carats
            if mass_input == mass_input_list[2] and mass_output == mass_output_list[3]:
                print('Result: ' + lb_to_ct(data) + " " + mass_output)

            # Ounces
            # Ounces to Grams
            if mass_input == mass_input_list[3] and mass_output == mass_output_list[0]:
                print('Result: ' + oz_to_g(data) + " " + mass_output)
            # Ounces to Kilograms
            if mass_input == mass_input_list[3] and mass_output == mass_output_list[1]:
                print('Result: ' + oz_to_kg(data) + " " + mass_output)
            # Ounces to Pounds
            if mass_input == mass_input_list[3] and mass_output == mass_output_list[2]:
                print('Result: ' + oz_to_lb(data) + " " + mass_output)
            # Ounces to Carats
            if mass_input == mass_input_list[3] and mass_output == mass_output_list[3]:
                print('Result: ' + oz_to_ct(data) + " " + mass_output)

            # Carats
            # Carats to Grams
            if mass_input == mass_input_list[4] and mass_output == mass_output_list[0]:
                print('Result: ' + ct_to_g(data) + " " + mass_output)
            # Carats to Kilograms
            if mass_input == mass_input_list[4] and mass_output == mass_output_list[1]:
                print('Result: ' + ct_to_kg(data) + " " + mass_output)
            # Carats to Pounds
            if mass_input == mass_input_list[4] and mass_output == mass_output_list[2]:
                print('Result: ' + ct_to_lb(data) + " " + mass_output)
            # Carats to Ounces
            if mass_input == mass_input_list[4] and mass_output == mass_output_list[3]:
                print('Result: ' + ct_to_oz(data) + " " + mass_output)