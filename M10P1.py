# M10P1.py
# Prompt the user to repeatedly enter last name, month, and sales.
# Use a function to compute next month's sales forecast.


def compute_forecast(month, sales):
    month = month.lower()

    if month == "jan" or month == "feb" or month == "mar":
        forecast_percent = 0.10
    elif month == "apr" or month == "may" or month == "jun":
        forecast_percent = 0.15
    elif month == "jul" or month == "aug" or month == "sep":
        forecast_percent = 0.20
    elif month == "oct" or month == "nov" or month == "dec":
        forecast_percent = 0.25
    else:
        forecast_percent = 0.00

    next_month_sales = sales * (1 + forecast_percent)
    return next_month_sales


response = input("Do you want to enter sales data? Enter Yes or No: ")

print()
print(f"{'Last Name':<15}{'Month':<10}{'Sales':>15}{'Forecast':>15}")
print("-" * 55)

while response.lower() == "yes":
    last_name = input("Enter last name: ")
    month = input("Enter month using three letters, such as Jan: ")
    sales = float(input("Enter sales: "))

    forecast = compute_forecast(month, sales)

    print(f"{last_name:<15}{month:<10}{sales:>15.2f}{forecast:>15.2f}")

    response = input("Do you want to enter another sales record? Enter Yes or No: ")
