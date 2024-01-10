import requests
import pandas as pd

# URL API
url = "https://api.apilayer.com/exchangerates_data/latest?base=BRL&apikey=3plTCLRkOn3b3kA5WboEeaPN7qIrx9zW"

# Makes a GET request to the URL and parses the JSON response into a Python data structure
request_data = requests.get(url).json()

# Extract exchange rate data from JSON response
rates_data = request_data.get("rates", {})

# Create a DataFrame Pandas with columns Currency and Rates
data = pd.DataFrame(list(rates_data.items()), columns=["Currency", "Rates"])

# Create Coin column and Rates column and treat decimal values ​​in the column in the Rates column
data["Coin"] = "BRL"
data["Rates"] = data["Rates"].round(2)

# Define the "Currency" column as the DataFrame index
data.set_index("Currency", inplace=False)

print(data.head(5))
