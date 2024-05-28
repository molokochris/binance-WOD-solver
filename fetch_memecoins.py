import requests
import csv

# Define the URL for the API endpoint to fetch all coins
url_list = "https://api.coingecko.com/api/v3/coins/list"
url_coin_details = "https://api.coingecko.com/api/v3/coins/"


# Fetch the list of all coins
response_list = requests.get(url_list)
response_list = response_list.json()
        
seven_letter_cryptos = []
for crypto in response_list:
    if len(crypto['name']) == 7:
        seven_letter_cryptos.append(crypto)

file_name_all = "cryptocurrencies.csv"
file_name_7_letters = "cryptocurrencies_7_letters.csv"
file_name_filtered = "cryptocurrencies_filtered.csv"

# Define the header for the CSV files
header = ["Name", "Symbol", "Market Cap", "Current Price", "Total Volume"]

# Define the header for the CSV files
with open(file_name_all, mode="w", newline="", encoding="utf-8") as file_all, \
     open(file_name_7_letters, mode="w", newline="", encoding="utf-8") as file_7_letters,\
     open(file_name_filtered, mode="w", newline="", encoding="utf-8") as file_filtered:

    write_all = csv.writer(file_all)
    write_7_letters = csv.writer(file_7_letters)
    write_filtered = csv.writer(file_filtered)

    # Write the header
    write_all.writerow(header)
    write_7_letters.writerow(header)
    write_filtered.writerow(header)

    for coin in response_list:
        write_all.writerow([coin['name'], coin['symbol']])
        
        if len(coin['name']) == 7:
            write_7_letters.writerow([coin['name'], coin['symbol']])

            if (coin['name'][0] == "C" or coin['name'][0] == "c"):
                write_filtered.writerow([coin['name'], coin['symbol']])
            
print(f"Data saved to {file_name_all}")
print(f"7-letter cryptocurrencies saved to {file_name_7_letters}")
print(f"filtered cryptocurrencies saved to {file_name_filtered}")