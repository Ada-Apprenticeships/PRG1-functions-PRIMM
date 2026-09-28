TAX_RATE = 0.20


def calculate_gross_pay(hours_worked, hourly_rate):
    return hours_worked * hourly_rate


def calculate_tax(gross_pay):
    return gross_pay * TAX_RATE


def calculate_take_home(hours_worked, hourly_rate):
    gross_pay = calculate_gross_pay(hours_worked, hourly_rate)
    tax = calculate_tax(gross_pay)
    return gross_pay - tax


print(calculate_gross_pay(38, 12.50))
print(calculate_tax(475.00))
print(calculate_take_home(38, 12.50))
