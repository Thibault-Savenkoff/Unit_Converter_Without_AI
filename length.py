# Length Converter

# Maths Code

def length_converter():
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