# Temperature Conversion Program

unit = input("Enter the unit of temperature (C for Celsius, F for Fahrenheit): ")
temp = float(input("Enter the temperature: "))
if unit == "c":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}°F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp}°C")  
else:
    print(f"Invalid Unit: {unit}. Please enter 'C' for Celsius or 'F' for Fahrenheit")
