import requests

response = requests.get("https://api.openweathermap.org")

print(response.status_code)