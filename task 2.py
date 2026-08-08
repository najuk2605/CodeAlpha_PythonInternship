# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 185
}

portfolio = {}
total_investment = 0

print("================================")
print("     STOCK PORTFOLIO TRACKER")
print("================================")

print("\nAvailable stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

print("\nEnter your stock holdings.")
print("Type 'done' when finished.\n")

while True:
    stock = input("Enter stock symbol: ").upper().strip()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available. Please choose from the listed stocks.\n")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.\n")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

        print(f"Added {quantity} shares of {stock}.\n")

    except ValueError:
        print("Please enter a valid whole number.\n")


# Calculate total investment
print("\n================================")
print("       PORTFOLIO SUMMARY")
print("================================")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    print(
        f"{stock}: {quantity} shares × "
        f"${price} = ${investment}"
    )

print("--------------------------------")
print(f"Total Investment: ${total_investment}")
print("================================")


# Save result to a text file
with open("portfolio_result.txt", "w") as file:
    file.write("STOCK PORTFOLIO SUMMARY\n")
    file.write("=======================\n\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity

        file.write(
            f"{stock}: {quantity} shares × "
            f"${price} = ${investment}\n"
        )

    file.write(f"\nTotal Investment: ${total_investment}")

print("\nPortfolio result saved to portfolio_result.txt")