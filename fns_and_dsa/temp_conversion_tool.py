FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celcius(fahrenheit):
    result = FAHRENHEIT_TO_CELSIUS_FACTOR*(fahrenheit - 32)
    return result

def convert_to_fahrenheit(celcius):
    result = celcius*CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return result
    

temperature =float(input("Enter the temperature to convert: "))

celcius_temp= convert_to_celcius(temperature)
farenheit_temp=convert_to_fahrenheit(temperature)

confirm = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if confirm == "F":
    print(f"{temperature}°F is {celcius_temp}°C")
elif confirm =="C":
    print(f"{temperature}°C is {farenheit_temp}°F")
    # print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
else:
    print("Invalid temperature unit")
