def stock_tracker():
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 2800,
        "AMZN": 3400,
        "MSFT": 300
    }

    total_investment = 0
    investments = {}

    print("Welcome to the Stock Tracker!")
    print("Available stocks and their prices:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")

    while True:
        stock_name = input("Enter the stock name (or type 'done' to finish): ").upper()
        if stock_name == 'DONE':
            break

        if stock_name not in stock_prices:
            print("Stock not found. Please enter a valid stock name.")
            continue

        try:
            quantity = int(input(f"Enter the quantity of {stock_name}: "))
            if quantity < 0:
                print("Quantity cannot be negative. Please enter a valid quantity.")
                continue
        except ValueError:
            print("Invalid input. Please enter a numeric value for quantity.")
            continue

        investment = stock_prices[stock_name] * quantity
        total_investment += investment
        investments[stock_name] = investments.get(stock_name, 0) + investment

    print("\nTotal Investment Summary:")
    for stock, investment in investments.items():
        print(f"{stock}: ${investment}")

    print(f"\nTotal Investment Value: ${total_investment}")

    save_to_file = input("Would you like to save the results to a file? (yes/no): ").lower()
    if save_to_file == 'yes':
        filename = input("Enter the filename (without extension): ")
        with open(f"{filename}.txt", "w") as file:
            file.write("Total Investment Summary:\n")
            for stock, investment in investments.items():
                file.write(f"{stock}: ${investment}\n")
            file.write(f"\nTotal Investment Value: ${total_investment}\n")
        print(f"Results saved to {filename}.txt")

if __name__ == "__main__":
    stock_tracker()
