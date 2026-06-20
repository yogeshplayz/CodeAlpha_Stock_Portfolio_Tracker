def stock_portfolio_tracker():
    """
    A simple stock portfolio tracker that calculates the total investment value.
    """

    # Use a hardcoded dictionary to define stock prices, as per the simplified scope.
    stock_prices = {
        "AAPL": 190.00,
        "TSLA": 230.00,
        "GOOGL": 150.50,
        "MSFT": 275.75,
        "AMZN": 273.25
    }

    portfolio = {} # Dictionary to store user's stocks and quantities

    print("--- Stock Portfolio Tracker ---")
    print("Enter 'done' when you are finished adding stocks.")

    while True:
        stock_ticker = input("\nEnter a stock ticker (e.g., AAPL): ").upper()

        if stock_ticker == 'DONE':
            break

        # Check if the entered stock is in our price list
        if stock_ticker not in stock_prices:
            print(f"Error: Stock ticker '{stock_ticker}' not found. Please choose from: {', '.join(stock_prices.keys())}")
            continue

        # Get the quantity from the user and validate it
        try:
            quantity = int(input(f"Enter quantity for {stock_ticker}: "))
            if quantity <= 0:
                print("Error: Please enter a positive number for quantity.")
                continue
        except ValueError:
            print("Error: Invalid input. Please enter a whole number for quantity.")
            continue

        # Add the stock to the user's portfolio
        portfolio[stock_ticker] = portfolio.get(stock_ticker, 0) + quantity
        print(f"Added {quantity} shares of {stock_ticker} to your portfolio.")

    # --- Calculate and Display Results ---
    if not portfolio:
        print("\nYour portfolio is empty. Goodbye!")
        return

    total_investment = 0.0
    print("\n--- Your Portfolio Summary ---")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        total_investment += value
        print(f"{stock}: {quantity} shares @ ${price:.2f} each = ${value:.2f}")

    print(f"\nTotal Investment Value: ${total_investment:.2f}")

    # --- Optional: Save to file ---
    save_file = input("\nDo you want to save your portfolio to a file? (yes/no): ").lower()
    if save_file == 'yes':
        try:
            with open("portfolio.txt", "w") as file:
                file.write("--- Your Portfolio Summary ---\n")
                for stock, quantity in portfolio.items():
                    price = stock_prices[stock]
                    value = price * quantity
                    file.write(f"{stock}: {quantity} shares @ ${price:.2f} each = ${value:.2f}\n")
                file.write(f"\nTotal Investment Value: ${total_investment:.2f}\n")
            print("Portfolio successfully saved to portfolio.txt")
        except IOError:
            print("Error: Could not save portfolio to file.")

if __name__ == "__main__":
    stock_portfolio_tracker()
