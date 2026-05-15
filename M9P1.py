# M9P1.py
# Allow the user to enter quantities and prices in a loop.
# Use a function to compute extended price and apply a 10% discount
# if the extended price is over $10,000.00.


def compute_extended_price(quantity, unit_price):
    extended_price = quantity * unit_price

    if extended_price > 10000.00:
        extended_price = extended_price * 0.90

    return extended_price


total_extended_price = 0.0
response = input("Do you want to enter an item? Enter Yes or No: ")

print()
print(f"{'Quantity':>10}{'Unit Price':>15}{'Extended Price':>20}")
print("-" * 45)

while response.lower() == "yes":
    quantity = int(input("Enter quantity: "))
    unit_price = float(input("Enter unit price: "))

    extended_price = compute_extended_price(quantity, unit_price)
    total_extended_price = total_extended_price + extended_price

    print(f"{quantity:>10}{unit_price:>15.2f}{extended_price:>20.2f}")

    response = input("Do you want to enter another item? Enter Yes or No: ")

print("-" * 45)
print(f"{'Total Extended Price:':>25}{total_extended_price:>20.2f}")
