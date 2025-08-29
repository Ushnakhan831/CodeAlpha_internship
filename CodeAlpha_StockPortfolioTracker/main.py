
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "AMZN": 100,
    "MSFT": 200
}
portfolio = {}

print("Welcome to the Stock Portfolio Tracker!")
print("Available stocks: ", ", ".join(stock_prices.keys()))
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not in list. Please choose from available stocks.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity < 0:
            print("Quantity cannot be negative.")
            continue
   
        if stock in portfolio:
            portfolio[stock] += quantity
        else:
            portfolio[stock] = quantity
    except ValueError:
        print("Please enter a valid integer quantity.")
total_investment = 0
print("\nYour Portfolio:")
for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_investment += value
    print(f"{stock}: {quantity} shares x ${stock_prices[stock]} = ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

save = input("Do you want to save your portfolio to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio:\n")
        for stock, quantity in portfolio.items():
            value = stock_prices[stock] * quantity
            file.write(f"{stock}: {quantity} shares x ${stock_prices[stock]} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}\n")
    print("Portfolio saved to portfolio.txt")
////
