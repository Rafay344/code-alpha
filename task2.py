stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("===== Stock Portfolio Tracker ===== - task2.py:12")

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available in our price list. - task2.py:21")
        print("Available stocks: - task2.py:22", ", ".join(stock_prices.keys()))
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))

        if quantity <= 0:
            print("Quantity must be greater than 0. - task2.py:29")
            continue

        value = stock_prices[stock] * quantity

        portfolio[stock] = {
            "quantity": quantity,
            "price": stock_prices[stock],
            "value": value
        }

        total_investment += value

        print(f"{stock} added successfully! - task2.py:42")
        print(f"Investment in {stock}: ${value} - task2.py:43")

    except ValueError:
        print("Please enter a valid number. - task2.py:46")

print("\n===== Portfolio Summary ===== - task2.py:48")

for stock, details in portfolio.items():
    print(
        f"{stock}: "
        f"{details['quantity']} shares × "
        f"${details['price']} = "
        f"${details['value']}"
    )

print(f"\nTotal Investment: ${total_investment} - task2.py:58")

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("===== Stock Portfolio =====\n")

    for stock, details in portfolio.items():
        file.write(
            f"{stock}: {details['quantity']} shares × "
            f"${details['price']} = ${details['value']}\n"
        )

    file.write(f"\nTotal Investment: ${total_investment}")

print("\nPortfolio saved to portfolio.txt - task2.py:72")