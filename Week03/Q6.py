inventory = {
    "Laptop": (999.99, 5),
    "Mouse": (29.99, 15),
    "Keyboard": (79.99, 10),
    "Monitor": (299.99, 8)
}

print("=== Current Inventory ===")
for key, value in inventory.items():
    print(f"{key} - Price: {value[0]}, Quantity: {value[1]}")

electronics = {"Laptop", "Monitor"}
accessories = {'Mouse', 'Keyboard'}

union =  electronics | accessories
print(f"\nAll product categories: {union}\n")

priceList = []
for value in inventory.values():
    priceList.append((value[0]))

print(f"Price list: {priceList}")
priceList.sort(reverse=False)
print(f"Sorted prices: {priceList}")

low = inventory["Laptop"][0]
for value in inventory.values():
    cur = value[0]
    if cur < low:
        low = cur
print(f"Lowest price: ${low}")

high = 0
for value in inventory.values():
    cur = value[0]
    if cur > high:
        high = cur
print(f"Highest price: ${high}")

inventory["Headphones"] = (49.99, 20)
inventory.update({"Mouse": (49.99, 12)})
del inventory["Monitor"]

print("\n=== Final Inventory ===")
for key, value in inventory.items():
    print(f"{key} - Price: {value[0]}, Quantity: {value[1]}")