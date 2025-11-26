# Compound Interest Calculator

principle = 0
rate = 0
time = 0
while principle <= 0:
    principle = float(input("Enter the Principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equals to 0.")
while rate <= 0:
    rate = float(input("Enter the Intrest rate amount: "))
    if rate <= 0:
        print("Intrest rate can't be less than or equals to 0.") 
while time <= 0:
    time = float(input("Enter the Time in years: "))
    if time <= 0:
        print("Time can't be less than or equals to 0.")
total = principle * pow((1 + rate / 100), time)
print(f"The balance after {time} year/s is: {total:.2f}. ")