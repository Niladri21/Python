# Python code to check weather conditions

temp = float(input("Enter the temperature in Celsius: "))

is_sunny = input("Is it sunny? (yes/no): ").strip().lower() == 'yes'

if temp >= 28 and is_sunny:
    print("It's a hot and sunny day!")

elif temp <= 0 and is_sunny:
    print("It's a cold and sunny day!")

elif 28 > temp > 0 and is_sunny:
    print("It's a warm and sunny day!")

elif temp >= 28 and not is_sunny:
    print("It's a hot and cloudy day!")

elif temp <= 0 and not is_sunny:
    print("It's a cold and cloudy day!")
    
elif 28 > temp > 0 and not is_sunny:
    print("It's a warm and cloudy day!")
