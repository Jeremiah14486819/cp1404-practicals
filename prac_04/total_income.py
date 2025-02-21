def print_income_report(incomes):
    total = 0
    for month, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {month} - Income: ${income:10.2f} Total: ${total:10.2f}")
