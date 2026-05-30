# Mass Converter

# Maths Code

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

# Mass
def mass_converter():
    mass_input = input('Select your mass unit: g, kg, lb, oz or ct? ')
    mass_input_list = ['g', 'kg', 'lb', 'oz', 'ct']
    if mass_input in mass_input_list:
        mass_output_list = ['g', 'kg', 'lb', 'oz', 'ct']
        mass_output_list.remove(mass_input)
        mass_output_list_question = mass_output_list[0] + ", " + mass_output_list[1] + ", " + mass_output_list[2] + " or " + mass_output_list[3]
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