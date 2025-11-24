import requests
'''
try:
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?units=imperial&lat=36.173999304&lon=-87.339831974&appid=81a720e0a77aa6e0983c34fa6b60cb7d")

except Exception as e:
    print("Something went wrong")

response_json = response.json()

#print from "main" dictionary from json
temp = response_json["main"]["temp"]
temp_min = response_json["main"]["temp_min"]
temp_max = response_json["main"]["temp_max"]

print(f"In Charlotte it is currently {temp}° F")
print(f"Today's High is {temp_min}° F")
print(f"Today's Low is {temp_max}° F")
'''

class City:
    def __init__(self, name, lat, lon, units="imperial"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()
    
    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=81a720e0a77aa6e0983c34fa6b60cb7d")

        except Exception as e:
            print("Something went wrong")

        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]

    def temp_print(self):
        units_symbol = "F"
        if self.units == "metric":
            units_symbol = "C"
        print(f"In {self.name} it is currently {self.temp}° {units_symbol}")
        print(f"Today's High is {self.temp_min}° {units_symbol}")
        print(f"Today's Low is {self.temp_max}° {units_symbol}")

my_city = City("Charlotte", 36.173999304, -87.339831974)
my_city.temp_print()

vacation_city = City("Saddlebrooke", 32.59427, -110.90413, units="metric")
vacation_city.temp_print()
