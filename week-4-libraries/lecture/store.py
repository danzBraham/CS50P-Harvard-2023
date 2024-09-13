import json
import requests


def main():
    response = requests.get("https://fakestoreapi.com/products?limit=5")
    print(json.dumps(response.json(), indent=2))


if __name__ == "__main__":
    main()
