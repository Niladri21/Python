# To enter the rows and columns using Nested Loops


rows = int(input("Enter the Number of rows: "))
columns = int(input("Enter the Number of Columns: "))
symbol = input("Enter a symbol to use: ")
for x in range(rows):
    for x in range(columns):
        print(symbol, end=" ")
    print()
