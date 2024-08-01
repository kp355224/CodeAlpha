import yfinance as yf
import json
import os

# File to store portfolio data
portfolio_file = 'portfolio.json'

def load_portfolio():
    if os.path.exists(portfolio_file):
        with open(portfolio_file, 'r') as file:
            return json.load(file)
    return {}

def save_portfolio(portfolio):
    with open(portfolio_file, 'w') as file:
        json.dump(portfolio, file, indent=4)

def add_stock(ticker, shares):
    portfolio = load_portfolio()
    if ticker in portfolio:
        portfolio[ticker] += shares
    else:
        portfolio[ticker] = shares
    save_portfolio(portfolio)
    print(f'Added {shares} shares of {ticker} to your portfolio.')

def remove_stock(ticker, shares):
    portfolio = load_portfolio()
    if ticker in portfolio:
        if portfolio[ticker] > shares:
            portfolio[ticker] -= shares
            print(f'Removed {shares} shares of {ticker} from your portfolio.')
        elif portfolio[ticker] == shares:
            del portfolio[ticker]
            print(f'Removed all shares of {ticker} from your portfolio.')
        else:
            print(f'You do not have enough shares of {ticker} to remove.')
        save_portfolio(portfolio)
    else:
        print(f'{ticker} is not in your portfolio.')

def get_portfolio_value():
    portfolio = load_portfolio()
    total_value = 0.0
    for ticker, shares in portfolio.items():
        stock = yf.Ticker(ticker)
        price = stock.history(period='1d')['Close'][0]
        total_value += price * shares
        print(f'{ticker}: {shares} shares @ ${price:.2f} each')
    print(f'Total portfolio value: ${total_value:.2f}')

# Example usage
while True:
    print("\nStock Portfolio Tracker")
    print("1. Add stock")
    print("2. Remove stock")
    print("3. View portfolio value")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        ticker = input("Enter stock ticker: ").upper()
        shares = int(input("Enter number of shares: "))
        add_stock(ticker, shares)
    elif choice == '2':
        ticker = input("Enter stock ticker: ").upper()
        shares = int(input("Enter number of shares: "))
        remove_stock(ticker, shares)
    elif choice == '3':
        get_portfolio_value()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")