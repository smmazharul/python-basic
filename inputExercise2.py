#Exercise 2 shopping cart program

item = input("Enter the item you want to buy: ")
quantity = int(input("Enter the quantity: "))
price_per_item = float(input("Enter the price per item: "))
total_price = quantity * price_per_item

print(f"The total price for {quantity} X {item}(s) is: ${total_price:.2f}")