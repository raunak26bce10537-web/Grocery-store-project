# Simple Grocery Store System
# Features: add item, remove item, calculate bill, apply discount, display bill

# Items available in the store (name: price per unit)
store_items = {
    "milk": 60,
    "bread": 40,
    "rice": 90,
    "eggs": 70,
    "sugar": 45,
    "apple": 120,
}

# Cart stores item name and quantity
cart = {}


def show_store_items():
    print("\n--- Store Items ---")
    for name, price in store_items.items():
        print(name.capitalize(), "- Rs", price)


def add_item():
    show_store_items()
    name = input("\nEnter item name to add: ").lower()

    if name not in store_items:
        print("Sorry, item not available.")
        return

    try:
        qty = int(input("Enter quantity: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if qty <= 0:
        print("Quantity must be more than 0.")
        return

    if name in cart:
        cart[name] = cart[name] + qty
    else:
        cart[name] = qty
    print(qty, name, "added to cart.")


def remove_item():
    if len(cart) == 0:
        print("Cart is empty.")
        return

    name = input("Enter item name to remove: ").lower()

    if name not in cart:
        print("Item is not in the cart.")
        return

    try:
        qty = int(input("Enter quantity to remove: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if qty >= cart[name]:
        del cart[name]
        print(name, "removed from cart.")
    elif qty > 0:
        cart[name] = cart[name] - qty
        print(qty, name, "removed from cart.")
    else:
        print("Invalid quantity.")


def calculate_total():
    total = 0
    for name, qty in cart.items():
        total = total + store_items[name] * qty
    return total


def get_discount(total):
    # Simple discount rules
    if total >= 1000:
        return 10   # 10 percent
    elif total >= 500:
        return 5    # 5 percent
    else:
        return 0


def display_bill():
    if len(cart) == 0:
        print("Cart is empty. Nothing to bill.")
        return

    print("\n========== BILL ==========")
    print("Item       Qty   Price   Amount")
    print("--------------------------")
    for name, qty in cart.items():
        price = store_items[name]
        print(name.capitalize().ljust(10), str(qty).ljust(5),
              str(price).ljust(7), price * qty)

    total = calculate_total()
    discount_percent = get_discount(total)
    discount_amount = total * discount_percent / 100
    final_amount = total - discount_amount

    print("--------------------------")
    print("Total           : Rs", total)
    print("Discount (" + str(discount_percent) + "%) : Rs", discount_amount)
    print("Final Amount    : Rs", final_amount)
    print("==========================")


def main():
    while True:
        print("\n===== GROCERY STORE =====")
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. Display bill")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            display_bill()
        elif choice == "4":
            print("Thank you for shopping!")
            break
        else:
            print("Invalid choice. Try again.")


main()