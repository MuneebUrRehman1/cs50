import sys
import requests

if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit()
else:
    try:
        n = float(sys.argv[1])
        try:
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            o = response.json()
            value = float(o["bpi"]["USD"]["rate_float"])
            print(f"{value * n :,.4f}")

        except requests.RequestException:
            print("Something went wrong")
            sys.exit()

    except ValueError:
        print("Command-line argument is not a number")
        sys.exit()
