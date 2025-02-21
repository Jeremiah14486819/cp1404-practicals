import random

START_PRICE = 10.00
MAX_PRICE = 1000.00
MIN_PRICE = 0.01

price = START_PRICE
day = 0

while MIN_PRICE < price < MAX_PRICE:
    day += 1
    if random.random() < 0.5:  # 50% chance of increase
        price *= random.uniform(1, 1.1)  # Increase by 0 to 10%
    else:  # 50% chance of decrease
        price *= random.uniform(0.95, 1)  # Decrease by 0 to 5%
    print(f"On day {day}, price is: ${price:,.2f}")

FILENAME = 'stock_price_output.txt'

with open(FILENAME, 'w') as out_file:
    out_file.write(f"Starting price: ${START_PRICE:,.2f}\n")
    day = 0
    while MIN_PRICE < price < MAX_PRICE:
        day += 1
        # Apply random changes to price
        out_file.write(f"On day {day}, price is: ${price:,.2f}\n")
