import requests, sys, time

def main():
    try:
        if len(sys.argv) != 2:
            sys.exit("Missing command-line argument")

        try:
            amount = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")

        price_float = None

        while True:
            try:
                resp = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
                
                data = resp.json()
                price_float = data["bpi"]["USD"]["rate_float"]

                print(f"${price_float * amount:,.4f}")

            except requests.RequestException as e:
                print(f"Error fetching data: {e}")

            time.sleep(18)

    except KeyboardInterrupt:
        if price_float is not None:
            print(f"Price at time of interruption: ${price_float * amount:,.4f}")
        else:
            print("The program terminated before any data was fetched.")
    except Exception as e:
        print(f"An unexpected error has occurred: {e}")

if __name__ == "__main__":
    main()
