# 1. run this code using a configuration
# 2. debug this code
# 3. add some try except wrappers
# 4. run flake8
# 5. run black

import csv


def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
    #    headers = next(rows)

        for row in rows:
            stock = {
                "name": row[1] # suspicious?
                 ,"shares": int(row[1]),  "price": float(row[2]),
            }
            portfolio.append(stock)

    return portfolio


def read_prices(filename):

    output = {}
    with open(filename) as f:
        rows = csv.reader(f  )
        for row in rows:
                parsed_price = float(row[1]   )
                output[row[0]] = parsed_price


    return output


if __name__ == "__main__":

    portfolio = read_portfolio("./Data/portfolio.csv")
    prices = read_prices("./Data/prices.csv")  # try prices2



    # Calculate the total cost of the portfolio
    total_cost = 0.0


    for s in portfolio:
        total_cost += s["share"] * s["price"]

    print("Total cost", total_cost)

    # Compute the current value of the portfolio

    total_value =    0.0
    for s in portfolio:

        total_value += s[  "share"] * prices[s["name"]]

    print("Current value", total_value  )
    print("Gain", total_value -  total_cost)
