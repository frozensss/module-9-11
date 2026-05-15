# M11P1.py
# Enter quantity, price, and discount rate.
# Use a function to return both the discount amount and discounted price.


def compute_discount(quantity, price, discount_rate):
    extended_price = quantity * price
    discount_amount = extended_price * discount_rate
    discounted_price = extended_price - discount_amount

    return discount_amount, discounted_price


response = input("Do you want to enter discount data? Enter Yes or No: ")

print()
print(f"{'Quantity':>10}{'Price':>12}{'Discount Amount':>20}{'Discounted Price':>20}")
print("-" * 62)

while response.lower() == "yes":
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    discount_rate = float(input("Enter discount rate as a decimal, such as 0.10 for 10%: "))

    discount_amount, discounted_price = compute_discount(quantity, price, discount_rate)

    print(f"{quantity:>10}{price:>12.2f}{discount_amount:>20.2f}{discounted_price:>20.2f}")

    response = input("Do you want to enter another discount record? Enter Yes or No: ")
