import requests
from pprint import pprint

FLIGHT_DATA_ENDPOINT = "https://tequila-api.kiwi.com/v2/search?"
FLIGHT_DATA_API_KEY = "<Tequila API Key>>"

class FlightData:
    def get_data(self, source_code, destination_code, start_date, end_date):
        query = {
            "fly_from": source_code,
            "fly_to": destination_code,
            "date_from": start_date,
            "date_to": end_date,
            "curr": "INR"
        }

        headers = {
            "apikey": FLIGHT_DATA_API_KEY
        }

        response = requests.get(url=FLIGHT_DATA_ENDPOINT, headers=headers, params=query)
        price = response.json()['data'][0]['price']
        date = response.json()['data'][0]['route'][0]['utc_departure'].split("T")[0]
        return price, date

# f = FlightData().get_data("LAX", "PAR", "22/06/2022", "22/10/2022")
# pprint(f)
