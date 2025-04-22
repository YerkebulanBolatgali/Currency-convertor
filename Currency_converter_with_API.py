import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate.host/latest?base={base_currency}&symbols={target_currency}"
    response = requests.get(url)
    data = response.json()
    if "rates" in data and target_currency in data["rates"]:
        return data["rates"][target_currency]
    else:
        return None

def convert_currency(amount, base_currency, target_currency):
    rate = get_exchange_rate(base_currency, target_currency)
    if rate:
        converted = amount * rate
        return converted
    else:
        return None

def main():
    print("=== Currency Converter ===")
    base_currency = input("Enter base currency (e.g., USD): ").upper()
    target_currency = input("Enter target currency (e.g., EUR): ").upper()
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount!")
        return

    result = convert_currency(amount, base_currency, target_currency)
    if result is not None:
        print(f"{amount:.2f} {base_currency} = {result:.2f} {target_currency}")
    else:
        print("Conversion failed. Please check the currency codes.")

if __name__ == "__main__":
    main()
