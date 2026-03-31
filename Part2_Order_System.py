Theme: Restaurant Menu & Order Management System

====================================================
Print Full Menu  Grouped by Category

menu = {
    "PANEER Tikka":   {"category": "Starters",  "price": 180.00, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.00, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.00, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.00, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.00, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.00, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.00, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.00, "available": True},
    "Rasgula":       {"category": "Desserts",  "price":  80.00, "available": True},
    "Ice -Cream":      {"category": "Desserts",  "price": 110.00, "available": False},
}

# -------------------------------
# Task 1: Explore the Menu
# -------------------------------

print("\n===== MENU BY CATEGORY =====\n")

# Step 1: Get unique categories
categories = set(item["category"] for item in menu.values())

# Step 2: Loop through categories
for category in categories:
    print(f"===== {category} =====")

    for item_name, details in menu.items():
        if details["category"] == category:
            price = details["price"]
            status = "Available" if details["available"] else "Unavailable"

            print(f"{item_name:<20} ₹{price:>6.2f}   [{status}]")

    print()  # blank line

===============================================================================================================================================================
Task 2 : Cart Operation

Task 2 : Cart Operation



cart = [] # Initialize cart as an empty list



def add_to_cart(item_name, quantity):

  if item_name not in menu:

    print(f"❌ {item_name} not found in menu.")

    return



  if not menu[item_name]["available"]:

    print(f"❌ {item_name} is currentlly unavailable.")

    return



  # Check if already in cart

  for item in cart:

    if item["item"] == item_name:

      item["quantity"] += quantity

      print(f"✅ Updated {item_name} quantity to {item['quantity']}")

      return



  # Add new item

  cart.append({

    "item": item_name,

    "quantity": quantity,

    "price": menu[item_name]["price"]

  })

  print(f"✅ Added {item_name} x{quantity} to cart")



# -------------------------------

# Function to remove item

# -------------------------------

def remove_from_cart(item_name):

  for item in cart:

    if item["item"] == item_name:

      cart.remove(item)

      print(f"🗑 Removed {item_name} from cart")

      return



  print(f"❌ {item_name} not found in cart.")



# -------------------------------

# Function to update quantity

# -------------------------------

def update_quantity(item_name, quantity):

  for item in cart:

    if item["item"] == item_name:

      item["quantity"] = quantity

      print(f"🔄 updated {item_name} to quantity {quantity}")

      return



  print(f"❌ {item_name} not found in cart.")



# -------------------------------

# Function to print cart

# -------------------------------

def print_cart():

  print("\n--- Current Cart ---")

  if not cart:

    print("Cart is empty.")

    return



  for item in cart:

    print(f"{item['item']} x{item['quantity']} (₹{item['price']})")



# -------------------------------

# SIMULATION STEPS

# -------------------------------



add_to_cart("PANEER Tikka", 2) # Changed to "PANEER Tikka" to match menu key

print_cart()



add_to_cart("Gulab Jamun", 1)

print_cart()



add_to_cart("PANEER Tikka", 1) # should update to 3

print_cart()



add_to_cart("Mystery Burger", 1) # not in menu

print_cart()



add_to_cart("Chicken Wings", 1) # unavailable

print_cart()



remove_from_cart("Gulab Jamun")

print_cart()



# -------------------------------

# FINAL ORDER SUMMARY

# -------------------------------



print("\n========== Order Summary ==========")



subtotal = 0



for item in cart:

  total_price = item["quantity"] * item["price"]

  subtotal += total_price

  print(f"{item['item']:<20} x{item['quantity']}  ₹{total_price:.2f}")



print("------------------------------------")



gst = subtotal * 0.05

total = subtotal + gst



print(f"Subtotal:        ₹{subtotal:.2f}")

print(f"GST (5%):        ₹{gst:.2f}")

print(f"Total Payable:     ₹{total:.2f}")

print("==================================")



================================================================================================

