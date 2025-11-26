# Python weight convertor program

weight = float(input("Enter your weight: "))
unit = input("Enter the unit of conversion (Kg/Lb): ")

if unit == "kg":
    weight = weight * 2.20462
    print(f"Your weight in pounds is: {weight:.2f} lbs")

elif unit == "lb":
    weight = weight / 2.20462

    print(f"Your weight in kilograms is: {weight:.2f} kg")

else:
    print("Invalid unit. Please enter 'kg' for kilograms or 'lb' for pounds.")
