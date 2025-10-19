import json

def load_rates(path="data/rates.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def convert(crypto, amount, rates):
    crypto = crypto.upper()
    if crypto in rates:
        usd_value = amount * rates[crypto]
        return f"≈ ${usd_value:.2f}"
    return "❌ Unsupported crypto."

def main():
    rates = load_rates()
    print("💱 Crypto Converter Lite\n")

    crypto = input("Enter crypto (BTC/ETH/DOGE/SOL): ").strip()
    try:
        amount = float(input("Enter amount: ").strip())
        print(convert(crypto, amount, rates))
    except ValueError:
        print("⚠️ Invalid amount entered.")

if __name__ == "__main__":
    main()
