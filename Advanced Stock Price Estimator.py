def calculate_stock_price(dividends, growth_rate, required_rate):
    stock_price = dividends / (required_rate - growth_rate)
    return stock_price

def calculate_dividends(stock_price, growth_rate, required_rate):
    dividends = stock_price * (required_rate - growth_rate)
    return dividends

def calculate_growth_rate(stock_price, dividends, required_rate):
    growth_rate = required_rate - (dividends / stock_price)
    return growth_rate

def calculate_required_rate(stock_price, dividends, growth_rate):
    required_rate = (dividends / stock_price) + growth_rate
    return required_rate

def main():
    while True:
        print("\nStock Price Estimator")
        print("1. Calculate Stock Price")
        print("2. Calculate Dividends")
        print("3. Calculate Growth Rate")
        print("4. Calculate Required Rate")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            dividends = float(input("Enter annual dividends: "))
            growth_rate = float(input("Enter expected growth rate (%): ")) / 100
            required_rate = float(input("Enter required rate of return (%): ")) / 100
            stock_price = calculate_stock_price(dividends, growth_rate, required_rate)
            print(f"Estimated Stock Price: ${stock_price:.2f}")
        elif choice == "2":
            stock_price = float(input("Enter current stock price: "))
            growth_rate = float(input("Enter expected growth rate (%): ")) / 100
            required_rate = float(input("Enter required rate of return (%): ")) / 100
            dividends = calculate_dividends(stock_price, growth_rate, required_rate)
            print(f"Estimated Dividends: ${dividends:.2f}")
        elif choice == "3":
            stock_price = float(input("Enter current stock price: "))
            dividends = float(input("Enter annual dividends: "))
            required_rate = float(input("Enter required rate of return (%): ")) / 100
            growth_rate = calculate_growth_rate(stock_price, dividends, required_rate)
            print(f"Estimated Growth Rate: {growth_rate * 100:.2f}%")
        elif choice == "4":
            stock_price = float(input("Enter current stock price: "))
            dividends = float(input("Enter annual dividends: "))
            growth_rate = float(input("Enter expected growth rate (%): ")) / 100
            required_rate = calculate_required_rate(stock_price, dividends, growth_rate)
            print(f"Required Rate of Return: {required_rate * 100:.2f}%")
        elif choice == "5":
            print("Exiting Stock Price Estimator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
