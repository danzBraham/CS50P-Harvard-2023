import json
import requests
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoin = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        bitcoin_in_USD = bitcoin * response.json()["bpi"]["USD"]["rate_float"]
        print(f"${bitcoin_in_USD:,.4f}")
    except requests.RequestException:
        pass


if __name__ == "__main__":
    main()
