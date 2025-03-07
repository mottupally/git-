foods = []  
prices = []  
total = 0  
while True:  
    food = input("Enter a food to buy (or press 'Q' to quit): ")  
    if food.lower() == 'q':  
        break  
    else:  
        foods.append(food)  
        price = float(input(f"Enter the price of {food}: "))  
        prices.append(price)  
print("\nYour shopping cart:")  
for food in foods:  
    print(food)  
for price in prices:  
    total += price  
print(f"\nYour total is: ${total:.2f}")  