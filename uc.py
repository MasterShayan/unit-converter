def unit_converter():
    print("Unit Converter")
    print("-------------")

    converters = {
        'w': weight_converter,
        'm': meter_converter,
        't': temperature_converter
    }

    while True:
        user_input = input("Enter 'w' to convert weight, 'm' to convert meter, or 't' to convert temperature: ").lower()

        if user_input in converters:
            converters[user_input]()
        else:
            print("Invalid input. Please try again!")

def convert(value, from_unit, to_unit, conversion_rates):
    if from_unit == to_unit:
        return value
    if from_unit in conversion_rates and to_unit in conversion_rates[from_unit]:
        return value * conversion_rates[from_unit][to_unit]
    else:
        raise ValueError("Invalid unit combination")

def weight_converter():
    print("Weight Converter")
    print("--------------")

    weight_units = {
        "kg": "kilograms",
        "lb": "pounds",
        "oz": "ounces",
        "g": "grams"
    }

    weight_conversion_rates = {
        "kg": {"lb": 2.20462, "oz": 35.274, "g": 1000},
        "lb": {"kg": 1 / 2.20462, "oz": 16, "g": 453.592},
        "oz": {"kg": 1 / 35.274, "lb": 1 / 16, "g": 28.35},
        "g": {"kg": 1 / 1000, "lb": 1 / 453.592, "oz": 1 / 28.35},
    }

    print("Available units:")
    for unit, name in weight_units.items():
        print(f"- {unit} ({name})")

    from_unit = input("Enter the unit to convert from: ")
    to_unit = input("Enter the unit to convert to: ")
    try:
        value = float(input("Enter the value to convert: "))
        result = convert(value, from_unit, to_unit, weight_conversion_rates)
        print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again!")

def meter_converter():
    print("Meter Converter")
    print("--------------")

    meter_units = {
        "m": "meters",
        "km": "kilometers",
        "cm": "centimeters",
        "mm": "millimeters",
        "in": "inches",
        "ft": "feet",
        "yd": "yards"
    }

    meter_conversion_rates = {
        "m": {"km": 0.001, "cm": 100, "mm": 1000, "in": 39.37, "ft": 3.2808, "yd": 1.0936},
        "km": {"m": 1000, "cm": 100000, "mm": 1000000, "in": 39370, "ft": 3280.8, "yd": 1093.6},
        "cm": {"m": 0.01, "km": 0.00001, "mm": 10, "in": 0.3937, "ft": 0.032808, "yd": 0.010936},
        "mm": {"m": 0.001, "km": 0.000001, "cm": 0.1, "in": 0.03937, "ft": 0.0032808, "yd": 0.0010936},
        "in": {"m": 0.0254, "km": 0.0000254, "cm": 2.54, "mm": 25.4, "ft": 1 / 12, "yd": 1 / 36},
        "ft": {"m": 0.3048, "km": 0.0003048, "cm": 30.48, "mm": 304.8, "in": 12, "yd": 1 / 3},
        "yd": {"m": 0.9144, "km": 0.0009144, "cm": 91.44, "mm": 914.4, "in": 36, "ft": 3},
    }

    print("Available units:")
    for unit, name in meter_units.items():
        print(f"- {unit} ({name})")

    from_unit = input("Enter the unit to convert from: ")
    to_unit = input("Enter the unit to convert to: ")
    try:
        value = float(input("Enter the value to convert: "))
        result = convert(value, from_unit, to_unit, meter_conversion_rates)
        print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again!")

def temperature_converter():
    print("Temperature Converter")
    print("-------------------")

    temperature_units = {
        "c": "Celsius",
        "f": "Fahrenheit",
        "k": "Kelvin"
    }

    temperature_conversion_rates = {
        "c": {"f": 9 / 5, "k": 1},
        "f": {"c": 5 / 9, "k": 5 / 9},
        "k": {"c": 1, "f": 9 / 5},
    }

    print("Available units:")
    for unit, name in temperature_units.items():
        print(f"- {unit} ({name})")

    from_unit = input("Enter the unit to convert from: ")
    to_unit = input("Enter the unit to convert to: ")
    try:
        value = float(input("Enter the value to convert: "))
        if from_unit == "c" and to_unit == "f":
          result = value * temperature_conversion_rates["c"]["f"] + 32
        elif from_unit == "c" and to_unit == "k":
          result = value + 273.15
        elif from_unit == "f" and to_unit == "c":
          result = (value - 32) * temperature_conversion_rates["f"]["c"]
        elif from_unit == "f" and to_unit == "k":
          result = (value - 32) * temperature_conversion_rates["f"]["k"] + 273.15
        elif from_unit == "k" and to_unit == "c":
          result = value - 273.15
        elif from_unit == "k" and to_unit == "f":
          result = (value - 273.15) * temperature_conversion_rates["k"]["f"] + 32
        elif from_unit == to_unit:
          result = value
        else:
          raise ValueError ("invalid unit combination")
        print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again!")

unit_converter()
