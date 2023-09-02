import requests
import sys


def main():
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    # Get the bitcoin amount from command-line argument
    bitcoin = get_bitcoin()
    # Print the value of bitcoin in USD
    print(exchange_bticoin(bitcoin))


def get_bitcoin():
    try:
        return float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")


def exchange_bticoin(bitcoin):
    try:
        # Make the API request to obtain the current USD rate
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        # Parse the JSON response and extract the USD rate
        obj = response.json()
        usd_rate = float(obj["bpi"]["USD"]["rate"].replace(",", ""))

        # Calculate the exchange result and format it as a string
        result = bitcoin * usd_rate
        return f"${result:,.4f}"
    except requests.RequestException:
        sys.exit("Failed to retrieve the exchange rate from the API")


if __name__ == "__main__":
    main()
