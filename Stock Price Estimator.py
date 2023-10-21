def calculate_stock_price(dividends, growth_rate, required_rate_of_return):
    # Calculate the stock price using the Gordon Growth Model
    stock_price = dividends / (required_rate_of_return - growth_rate)
    return stock_price

def get_user_input():
    dividends = float(input("Enter the annual dividends per share: $"))
    growth_rate = float(input("Enter the expected annual growth rate (%): ")) / 100
    required_rate_of_return = float(input("Enter the required rate of return (%): ")) / 100
    return dividends, growth_rate, required_rate_of_return

def display_stock_price(stock_price):
    print(f"Estimated Stock Price: ${stock_price:.2f}")

def main():
    while True:
        print("\nStock Price Calculator")
        print("1. Calculate Stock Price")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            dividends, growth_rate, required_rate_of_return = get_user_input()
            stock_price = calculate_stock_price(dividends, growth_rate, required_rate_of_return)
            display_stock_price(stock_price)
        elif choice == "2":
            print("Exiting Stock Price Calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
