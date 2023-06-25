import requests

class DataManager:
    def __init__(self, sheet_endpoint):
        self.sheet_endpoint = sheet_endpoint

    def extract_price(self):
        response = requests.get(self.sheet_endpoint)
        context = response.json()
        return context['prices']

    def update_sheet(self, row_id, city_code):
        params = {
            "price": {
                "iataCode": city_code
            }
        }
        rep = requests.put(url=f"{self.sheet_endpoint}/{row_id}", json=params)


