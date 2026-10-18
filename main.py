import time
import requests

url = "https://store.steampowered.com/api/appdetails"

games = {620: "Portal 2", 105600: "Terraria", 730: "Counter-Strike 2"}

for app_id, name in games.items():
    params = {"appids": app_id, "cc": "us", "filters": "price_overview"}
    data = requests.get(url, params=params).json()

    game = data[str(app_id)]
    if game["success"] and game["data"]:
        price_info = game["data"]["price_overview"]
        print(name, "-", price_info["final_formatted"], f"({price_info['discount_percent']}% off)")
    else:
        print(name, "- no price (free?)")

    time.sleep(1)  # to slow down reqs so Steam doesn't block us