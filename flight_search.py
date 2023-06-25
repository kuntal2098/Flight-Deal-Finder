import requests

KIWI_ENDPOINT = "https://tequila-api.kiwi.com/"
KIWI_API_KEY = "<Kiwi API Key>"

class FlightSearch:
    def get_destination_code(self, city_name):
        location_endpoint = f"{KIWI_ENDPOINT}locations/query?"
        headers = {
            "apikey": KIWI_API_KEY
        }
        query = {
            "term": city_name,
            "location_types": "city"
        }

        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code
