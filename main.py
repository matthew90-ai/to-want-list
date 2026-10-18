#this should be the main code for running the software.
# I want it to communicate with the steam api.
import requests

app_id = 620 #portal 2 app id

url = "https://store.steampowered.com/api/appdetails"
params = {"appids": app_id, "cc": "us", "filters": "price_overview"}
response = requests.get(url, params=params)
data = response.json()


price_info = data[str(app_id)]["data"]["price_overview"]

print("Price: ", price_info["final_formatted"])
print("Discount: ", price_info["discount_percent"], "%")

target_price = 5.00 #price u want in dollars
current_price = price_info["final"]/100

if current_price <= target_price:
    print("Deal!")
else:
    print("Wait for a better deal!")




