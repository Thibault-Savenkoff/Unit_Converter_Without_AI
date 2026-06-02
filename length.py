# Length Converter

# Maths Code

# Nanometers

# Nanometers to Micrometers
def nm_to_µm(x):
    sum = float(x) * float(10**(-3))
    return str(sum)

# Nanometers to Millimeters
def nm_to_mm(x):
    sum = float(x) * float(10**(-6))
    return str(sum)

# Nanometers to Centimeters
def nm_to_cm(x):
    sum = float(x) * float(10**(-7))
    return str(sum)

# Nanometers to Meters
def nm_to_m(x):
    sum = float(x) * float(10**(-9))
    return str(sum)

# Nanometers to Kilometers
def nm_to_km(x):
    sum = float(x) * float(10**(-12))
    return str(sum)

# Nanometers to Inchs
def nm_to_in(x):
    sum = float(x) * float(3.9370078740157*10**(-8))
    return str(sum)

# Nanometers to Feet
def nm_to_ft(x):
    sum = float(x) * float(3.2808398950131*10**(-9))
    return str(sum)

# Nanometers to Yards
def nm_to_yd(x):
    sum = float(x) * float(1.0936132983377*10**(-9))
    return str(sum)

# Nanometers to Miles
def nm_to_mi(x):
    sum = float(x) * float(6.2137119223733*10**(-13))
    return str(sum)

def length_converter():
    length_input = input('Select your length unit: nm, µm, mm, cm, dm, m, km, in, ft, yd or mi? ')
    length_input_list = ['nm', 'µm', 'mm', 'cm', 'dm', 'm', 'km', 'in', 'ft', 'yd', 'mi']
    if length_input in length_input_list:
        length_output_list = ['nm', 'µm', 'mm', 'cm', 'dm', 'm', 'km', 'in', 'ft', 'yd', 'mi']
        length_output_list.remove(length_input)
        length_output_list_question = length_output_list[0] + ", " + length_output_list[1] + ", " + length_output_list[2] + ", " + length_output_list[3] + ", " + length_output_list[4] + ", " + length_output_list[5] + ", " + length_output_list[6] + ", " + length_output_list[7] + ", " + length_output_list[8] + ", " + length_output_list[9] + " or " + length_output_list[10]
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

            # Inchs
            # Inchs to Nanometers
            if length_input == length_input_list[7] and length_output == length_output_list[0]:
                print('Result: ' + in_to_nm(data) + " " + length_output)
            # Inchs to Micrometers
            if length_input == length_input_list[7] and length_output == length_output_list[1]:
                print('Result: ' + in_to_µm(data) + " " + length_output)
            # Inchs to Millimeters
            if length_input == length_input_list[7] and length_output == length_output_list[2]:
                print('Result: ' + in_to_mm(data) + " " + length_output)
            # Inchs to Centimeters
            if length_input == length_input_list[7] and length_output == length_output_list[3]:
                print('Result: ' + in_to_cm(data) + " " + length_output)
            # Inchs to Decimeters
            if length_input == length_input_list[7] and length_output == length_output_list[4]:
                print('Result: ' + in_to_dm(data) + " " + length_output)
            # Inchs to Meters
            if length_input == length_input_list[7] and length_output == length_output_list[5]:
                print('Result: ' + in_to_m(data) + " " + length_output)
            # Inchs to Kilometers
            if length_input == length_input_list[7] and length_output == length_output_list[6]:
                print('Result: ' + in_to_km(data) + " " + length_output)
            # Inchs to Feet
            if length_input == length_input_list[7] and length_output == length_output_list[7]:
                print('Result: ' + in_to_ft(data) + " " + length_output)
            # Inchs to Yards
            if length_input == length_input_list[7] and length_output == length_output_list[8]:
                print('Result: ' + in_to_yd(data) + " " + length_output)
            # Inchs to Miles
            if length_input == length_input_list[7] and length_output == length_output_list[9]:
                print('Result: ' + in_to_mi(data) + " " + length_output)

            # Feet
            # Feet to Nanometers
            if length_input == length_input_list[8] and length_output == length_output_list[0]:
                print('Result: ' + ft_to_nm(data) + " " + length_output)
            # Feet to Micrometers
            if length_input == length_input_list[8] and length_output == length_output_list[1]:
                print('Result: ' + ft_to_µm(data) + " " + length_output)
            # Feet to Millimeters
            if length_input == length_input_list[8] and length_output == length_output_list[2]:
                print('Result: ' + ft_to_mm(data) + " " + length_output)
            # Feet to Centimeters
            if length_input == length_input_list[8] and length_output == length_output_list[3]:
                print('Result: ' + ft_to_cm(data) + " " + length_output)
            # Feet to Decimeters
            if length_input == length_input_list[8] and length_output == length_output_list[4]:
                print('Result: ' + ft_to_dm(data) + " " + length_output)
            # Feet to Meters
            if length_input == length_input_list[8] and length_output == length_output_list[5]:
                print('Result: ' + ft_to_m(data) + " " + length_output)
            # Feet to Kilometers
            if length_input == length_input_list[8] and length_output == length_output_list[6]:
                print('Result: ' + ft_to_km(data) + " " + length_output)
            # Feet to Inchs
            if length_input == length_input_list[8] and length_output == length_output_list[7]:
                print('Result: ' + ft_to_in(data) + " " + length_output)
            # Feet to Yards
            if length_input == length_input_list[8] and length_output == length_output_list[8]:
                print('Result: ' + ft_to_yd(data) + " " + length_output)
            # Feet to Miles
            if length_input == length_input_list[8] and length_output == length_output_list[9]:
                print('Result: ' + ft_to_mi(data) + " " + length_output)

            # Yards
            # Yards to Nanometers
            if length_input == length_input_list[9] and length_output == length_output_list[0]:
                print('Result: ' + yd_to_nm(data) + " " + length_output)
            # Yards to Micrometers
            if length_input == length_input_list[9] and length_output == length_output_list[1]:
                print('Result: ' + yd_to_µm(data) + " " + length_output)
            # Yards to Millimeters
            if length_input == length_input_list[9] and length_output == length_output_list[2]:
                print('Result: ' + yd_to_mm(data) + " " + length_output)
            # Yards to Centimeters
            if length_input == length_input_list[9] and length_output == length_output_list[3]:
                print('Result: ' + yd_to_cm(data) + " " + length_output)
            # Yards to Decimeters
            if length_input == length_input_list[9] and length_output == length_output_list[4]:
                print('Result: ' + yd_to_dm(data) + " " + length_output)
            # Yards to Meters
            if length_input == length_input_list[9] and length_output == length_output_list[5]:
                print('Result: ' + yd_to_m(data) + " " + length_output)
            # Yards to Kilometers
            if length_input == length_input_list[9] and length_output == length_output_list[6]:
                print('Result: ' + yd_to_km(data) + " " + length_output)
            # Yards to Inchs
            if length_input == length_input_list[9] and length_output == length_output_list[7]:
                print('Result: ' + yd_to_in(data) + " " + length_output)
            # Yards to Feet
            if length_input == length_input_list[9] and length_output == length_output_list[8]:
                print('Result: ' + yd_to_ft(data) + " " + length_output)
            # Yards to Miles
            if length_input == length_input_list[9] and length_output == length_output_list[9]:
                print('Result: ' + yd_to_mi(data) + " " + length_output)

            # Miles
            # Miles to Nanometers
            if length_input == length_input_list[10] and length_output == length_output_list[0]:
                print('Result: ' + mi_to_nm(data) + " " + length_output)
            # Miles to Micrometers
            if length_input == length_input_list[10] and length_output == length_output_list[1]:
                print('Result: ' + mi_to_µm(data) + " " + length_output)
            # Miles to Millimeters
            if length_input == length_input_list[10] and length_output == length_output_list[2]:
                print('Result: ' + mi_to_mm(data) + " " + length_output)
            # Miles to Centimeters
            if length_input == length_input_list[10] and length_output == length_output_list[3]:
                print('Result: ' + mi_to_cm(data) + " " + length_output)
            # Miles to Decimeters
            if length_input == length_input_list[10] and length_output == length_output_list[4]:
                print('Result: ' + mi_to_dm(data) + " " + length_output)
            # Miles to Meters
            if length_input == length_input_list[10] and length_output == length_output_list[5]:
                print('Result: ' + mi_to_m(data) + " " + length_output)
            # Miles to Kilometers
            if length_input == length_input_list[10] and length_output == length_output_list[6]:
                print('Result: ' + mi_to_km(data) + " " + length_output)
            # Miles to Inchs
            if length_input == length_input_list[10] and length_output == length_output_list[7]:
                print('Result: ' + mi_to_in(data) + " " + length_output)
            # Miles to Feet
            if length_input == length_input_list[10] and length_output == length_output_list[8]:
                print('Result: ' + mi_to_ft(data) + " " + length_output)
            # Miles to Yards
            if length_input == length_input_list[10] and length_output == length_output_list[9]:
                print('Result: ' + mi_to_yd(data) + " " + length_output)