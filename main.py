# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "AMZN": 175,
    "MSFT": 215
}

def main():
    print("--- Stock Portfolio Tracker ---")
    
    # User inputs
    stock_name = input("Enter stock name (e.g., AAPL): ").upper()
    
    if stock_name in stock_prices:
        try:
            quantity = int(input(f"How many shares of {stock_name} do you own? "))
            
            # Calculate total investment
            price = stock_prices[stock_name]
            total_value = price * quantity
            
            result = f"Investment in {stock_name}: ${total_value:,.2f}"
            print(f"\n{result}")
            
            # Optional: Save to .txt file
            with open("portfolio.txt", "w") as f:
                f.write(result)
            print("Result saved to portfolio.txt")
            
        except ValueError:
            print("Invalid input. Please enter a number for quantity.")
    else:
        print("Stock not found in our database.")

if __name__ == "__main__":
    main()
