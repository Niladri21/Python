# Python code to check weather conditions

temp = float(input("Enter the temperature in Celsius: "))

is_sunny = input("Is it sunny? (yes/no): ").strip().lower() 

def check_temp(x):
    if x <= 0:
        return 'freezing'
    elif x > 0 and x <= 28:
        return 'cold'
    else:
        return 'hot'

def check_sunny(x):
    if x == 'yes':
        return 'sunny'
    else:
        return 'cloudy'

temp_final = check_temp(temp)
sunny_final = check_sunny(is_sunny)

print(f"It's {temp_final} and {sunny_final} outside!")

