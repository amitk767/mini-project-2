print("========== Menu card    ==========")

menu = ["Veg Sandwich", "Masala Dosa", "Chole Rice",
        "Paneer Roll", "Tea"]
prices = [60, 80, 90, 100, 20]
for i in range(5):
    print(i + 1, menu[i], "- ₹", prices[i])
selected_items = []
quantities = []
line_costs = []
subtotal = 0
while True:
    item_number = int(input("Choose item number (1-5):"))
    if item_number < 1 or item_number > 5:
        print("Invalid item number!")
        continue
    quantity = int(input("Enter quantity: "))
    if quantity <= 0:
        print("Invalid quantity!")
        continue

    item_name = menu[item_number - 1]
    item_price = prices[item_number - 1]

    line_cost = item_price * quantity

    selected_items.append(item_name)
    quantities.append(quantity)
    line_costs.append(line_cost)

    subtotal = subtotal + line_cost

    print("Added:", item_name, "x", quantity,
          "= ₹", line_cost)

    choice = input("Add another item? (yes/no): ")

    if choice == "no":
        break

print("\n========== RECEIPT ==========")

if subtotal == 0:
    print("No order was placed.")

else:
    for i in range(len(selected_items)):
        print(selected_items[i],"x",quantities[i],":₹",line_costs[i])

    print("Subtotal: ₹", subtotal)

    if subtotal >= 500:
        discount = subtotal * 10 / 100
    elif subtotal >= 250:
        discount = subtotal * 5 / 100
    else:
        discount = 0

    final_total = subtotal - discount

    print("Discount: ₹", format(discount, ".2f"))
    print("Final Total: ₹", format(final_total, ".2f"))

print("Thank you !!!! ")