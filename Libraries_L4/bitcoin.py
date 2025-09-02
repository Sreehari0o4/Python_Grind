"""
This script fetches the current price of Bitcoin in USD from the CoinCap API and calculates the total value for a user-specified amount of Bitcoin. The amount is provided as a command-line argument. The script handles missing or invalid arguments and network errors gracefully, displaying appropriate error messages. The result is printed with four decimal places and comma separators for readability.
"""

import requests
import sys

try:
    try:
        n = float(sys.argv[1])
    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")

    url = "https://api.coincap.io/v3/assets/bitcoin?apiKey=f369d5e3b7b909e6d5b74a19b8c4f2ff6117f1de6c75997dae130e9efdeb63ed"
    
    response = requests.get(url)
    a = response.json()
    res = a["data"]
    price = float(res["priceUsd"])
    print(price)
    total_amt = n * price
    print(f"${total_amt:,.4f}")
    
except requests.RequestException:
    ...