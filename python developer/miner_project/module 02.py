items = ["veg sandwich", "masala dosa", "chole rice", "paneer roll", "tea"]
price =[60, 80, 90, 100, 20]
print("Smart Canteen")
for i in range(len(items)):
    print(f"{i+1}. {items[i]} - {price[i]}")

total = 0
receipt = []
cost_add = []

while True:
    enter_item_number = int(input("enter item number to be ordered"))
    item_quantity = int(input("enter quantity of item"))
    cost = price[enter_item_number-1] * item_quantity
    item_added = items[enter_item_number-1]
    added = (item_added * item_quantity)
    if enter_item_number >= 1 or enter_item_number <= 5:
        print(f"Added: {added} = {cost}")
        receipt.append(added)
        cost_add.append(cost)
        total += cost
    else:
        print("enter valid order number")
        enter_item_number = int(input("enter item number to be ordered"))
        continue
    add_item = input("Add another item? (y/n)")
    if add_item.lower() == "n":
        print("no more input")
        break


print("_receipt_")

print(f"{receipt} = {cost_add}")
print(total)