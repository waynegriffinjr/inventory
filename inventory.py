# Product inventory system for a small store

inventory = {
    "eggs": {
        "full_name": "doz_duck_eggs",
        "price": 4.99,
        "quantity": 10
         },
    "raspberry": {
        "full_name": "8oz_raspberry",
        "price": 4.99,
        "quantity": 10
        },
    "bread": {
        "full_name": "sourdough",
        "price": 3.99,
        "quantity": 10
        },
    "cherry": {
        "full_name": "8oz_cherry",
        "price": 4.99,
        "quantity": 10}
}

# Calcualte total value of inventory
inv_total = 0

for item_name in inventory:
    item_data = inventory[item_name]
    price = item_data["price"]
    quantity = item_data["quantity"]
    inv_total += price * quantity
    


# Header
print("=" * 42)
print("          -- Inventory List --")
print("=" * 42)

# Print full inventory list and value with formatting 
print(f"Duck Eggs: {inventory['eggs']}")
print(f"Raspberry: {inventory['raspberry']}")
print(f"Sourdough: {inventory['bread']}")
print(f"Cherry   : {inventory['cherry']}")
print(f"       --Total Value: ${inv_total:.2f} ")


# Search inventory
search = input("\nLook up item: ").lower()

inventory_find = inventory.get(search) # .get() returns None if not found

if inventory_find:
    
    print(f"Item: {inventory_find['full_name']}")
    print(f"Price: {inventory_find['price']}")
    print(f"Qty: {inventory_find['quantity']}")

# Update qunatity from sale or restock (negative sale/positive restock)
    update = input("Update Quantity? yes or no ")
    if update == "yes":
        inv_update = int(input("Enter amount to add or subtract (eg. 3 or -3): "))
        inventory_find["quantity"] += inv_update
        # print updated quantity
        print(f"Qty: {inventory_find['quantity']}")
        
# Prevent negative quantity in the FUTURE UPDATE

else:
    print(f"No item found for '{search}'.")

low_stock = set()

for item_name, item_data in inventory.items():
    if item_data["quantity"] < 5:
        low_stock.add(item_name)
        print("\nLow Stock Items:")
        for item in low_stock:
            print(item)
            
