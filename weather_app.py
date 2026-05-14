import requests

print("===== Weather App =====")

city = input("Enter city name: ")

api_key = "29a12dca012845c2d5f29a22ec08842e"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

data = response.json()

if response.status_code == 200:

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]

    print("\nWeather Report")
    print("City:", city.title())
    print("Temperature:", temp, "°C")
    print("Humidity:", humidity, "%")
    print("Condition:", condition)

else:
    print("Error fetching weather details")
    print(data)