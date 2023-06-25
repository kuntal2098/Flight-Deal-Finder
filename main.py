#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from flight_data import FlightData
from notification_manager import NotificationManager

SHEETY_ENDPOINT = "https://api.sheety.co/646cb74a60fec4cec86b4b32341b1646/flightDeals/prices"
data_manage = DataManager(SHEETY_ENDPOINT)

sheet_data = data_manage.extract_price()

for data in sheet_data:
    if not data['iataCode']:
        city_code = FlightSearch().get_destination_code(data['city'])
        data_manage.update_sheet(data['id'], city_code)

source = input("Enter the source: ")
source_city_code = FlightSearch().get_destination_code(source)

current_date = datetime.now()
six_moth_future = current_date + timedelta(days=6*30)
start_date = current_date.strftime("%d/%m/%Y")
end_date = six_moth_future.strftime("%d/%m/%Y")

sheet_data = data_manage.extract_price()

l = []
print(f"From {source}({source_city_code})")
for data in sheet_data:
    dic = {}
    price, date = FlightData().get_data(source_city_code, data["iataCode"], start_date, end_date)
    print(date, " -> ", data["iataCode"], ": ₹" + str(price))
    if price < data["lowestPrice"]:
        dic["Date"] = date
        dic["Source"] = source_city_code
        dic["Destination"] = data["iataCode"]
        dic["Current Lowest Price"] = price
        dic["Previous Price"] = data["lowestPrice"]
        l.append(dic)

if l:
    success = NotificationManager().send_mail(l)
    print(success)
else:
    print("No lower prices found")


