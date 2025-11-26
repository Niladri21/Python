# Exercise 2: Shopping cart Program

item = input("What do you want to buy?: ")
price = float(input("What is the price of the Item?: "))
quantity = int(input("How many do you want to buy?: "))
total = price * quantity

print(f"You have bought {quantity} {item}s for {price} rupees.")
print(f"The total price is Rs{total}")
