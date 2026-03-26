# Unit Converter

# Grams to Kilograms
def g_to_kg(x):
    sum = float(x) * float(10**(-3))
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

# Mass
if home == 2:
    mass_input = input('Select your mass unit: g, kg, lb, oz, ct? ')
    mass_input_list = ['g', 'kg', 'lb', 'oz', 'ct']
    if mass_input in mass_input_list:
        mass_output_list = ['g', 'kg', 'lb', 'oz', 'ct']
        mass_output_list.remove(mass_input)
        mass_output_list_question = mass_output_list[0] + ", " + mass_output_list[1] + ", " + mass_output_list[2] + ", " + mass_output_list[3]
        mass_output = input('Select the mass unit you want: ' + str(mass_output_list_question) + "? ")
        if mass_output in mass_output_list:
            data = input('Enter your mass: ')
            # Grams
            if mass_input == mass_input_list[0] and mass_output == mass_output_list[0]:
                print('Result: ' + g_to_kg(data) + " " + mass_output)
            if mass_input == mass_input_list[0] and mass_output == mass_output_list[1]:
                print('Result: ' + g_to_lb(data) + " " + mass_output)
            if mass_input == mass_input_list[0] and mass_output == mass_output_list[2]:
                print('Result: ' + g_to_oz(data) + " " + mass_output)
            if mass_input == mass_input_list[0] and mass_output == mass_output_list[3]:
                print('Result: ' + g_to_ct(data) + " " + mass_output)

            # Kilogram
            if mass_input == mass_input_list[1] and mass_output == mass_output_list[0]:
                print('Result: ' + kg_to_g(data) + " " + mass_output)
            if mass_input == mass_input_list[1] and mass_output == mass_output_list[1]:
                print('Result: ' + kg_to_lb(data) + " " + mass_output)
            if mass_input == mass_input_list[1] and mass_output == mass_output_list[2]:
                print('Result: ' + kg_to_oz(data) + " " + mass_output)
            if mass_input == mass_input_list[1] and mass_output == mass_output_list[3]:
                print('Result: ' + kg_to_ct(data) + " " + mass_output)

            # Pound
            if mass_input == mass_input_list[2] and mass_output == mass_output_list[0]:
                print('Result: ' + lb_to_g(data) + " " + mass_output)
            if mass_input == mass_input_list[2] and mass_output == mass_output_list[1]:
                print('Result: ' + lb_to_kg(data) + " " + mass_output)
            if mass_input == mass_input_list[2] and mass_output == mass_output_list[2]:
                print('Result: ' + lb_to_oz(data) + " " + mass_output)
            if mass_input == mass_input_list[2] and mass_output == mass_output_list[3]:
                print('Result: ' + lb_to_ct(data) + " " + mass_output)

            # Ounce
            if mass_input == mass_input_list[3] and mass_output == mass_output_list[0]:
                print('Result: ' + oz_to_g(data) + " " + mass_output)
            if mass_input == mass_input_list[3] and mass_output == mass_output_list[1]:
                print('Result: ' + oz_to_kg(data) + " " + mass_output)
            if mass_input == mass_input_list[3] and mass_output == mass_output_list[2]:
                print('Result: ' + oz_to_lb(data) + " " + mass_output)
            if mass_input == mass_input_list[3] and mass_output == mass_output_list[3]:
                print('Result: ' + oz_to_ct(data) + " " + mass_output)

            # Carat
            if mass_input == mass_input_list[4] and mass_output == mass_output_list[0]:
                print('Result: ' + ct_to_g(data) + " " + mass_output)
            if mass_input == mass_input_list[4] and mass_output == mass_output_list[1]:
                print('Result: ' + ct_to_kg(data) + " " + mass_output)
            if mass_input == mass_input_list[4] and mass_output == mass_output_list[2]:
                print('Result: ' + ct_to_lb(data) + " " + mass_output)
            if mass_input == mass_input_list[4] and mass_output == mass_output_list[3]:
                print('Result: ' + ct_to_oz(data) + " " + mass_output)