# M10P2.py
# Prompt the user to repeatedly enter automobile information.
# Use a function to compute the out-the-door price.


def compute_out_the_door_price(msrp, make, model, electric_code):
    make = make.lower()
    model = model.lower()
    electric_code = electric_code.lower()

    if electric_code == "y":
        percent_off = 0.30
    elif make == "honda" and model == "accord":
        percent_off = 0.10
    elif make == "toyota" and model == "rav4":
        percent_off = 0.15
    else:
        percent_off = 0.05

    discount = msrp * percent_off
    new_msrp = msrp - discount
    out_the_door_price = new_msrp * 1.07

    return out_the_door_price


total_msrp = 0.0
total_sales_price = 0.0
response = input("Do you want to enter automobile data? Enter Yes or No: ")

print()
print(f"{'Make':<12}{'Model':<12}{'EV':<6}{'MSRP':>15}{'Out the Door':>18}")
print("-" * 63)

while response.lower() == "yes":
    make = input("Enter automobile make: ")
    model = input("Enter automobile model: ")
    electric_code = input("Is it an electric vehicle? Enter Y or N: ")
    msrp = float(input("Enter MSRP: "))

    out_the_door_price = compute_out_the_door_price(msrp, make, model, electric_code)

    total_msrp = total_msrp + msrp
    total_sales_price = total_sales_price + out_the_door_price

    print(f"{make:<12}{model:<12}{electric_code:<6}{msrp:>15.2f}{out_the_door_price:>18.2f}")

    response = input("Do you want to enter another automobile? Enter Yes or No: ")

print("-" * 63)
print(f"{'Total MSRP:':>30}{total_msrp:>15.2f}")
print(f"{'Total Sales Price:':>30}{total_sales_price:>15.2f}")
