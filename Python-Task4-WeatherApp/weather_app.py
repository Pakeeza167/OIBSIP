import requests

api_key = "d2d125ddfeb42d4b861951b84fd5b255"
city = input("Enter city name: ")
print("you entered:", city)

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": city,
    "appid": api_key,
    "units": "metric"
}
try:
    response = requests.get(url, params=params, timeout=10)

    if response.status_code == 404:
        print("City not found. Please check the city name and try again.")
        exit()
    if response.status_code == 401:
        print("Invalid API key.")
        exit() 

    response.raise_for_status()

    data = response.json()      
     
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    fahrenheit = (temperature * 9/5) + 32

    print("\nWeather in", city)
    print("--------------------------")
    print("Temperature:", temperature, "°C /", fahrenheit, "°F")
    print("Feels like:", feels_like, "°C")
    print("Humidity:", humidity, "%")
    print("Condition:", condition)
    print("Wind Speed:", wind_speed, "m/s")

except requests.exceptions.Timeout:
    print("Request timed out. please check your internet connection.")

except requests.exceptions.HTTPError:
    if response.status_code == 404:
        print("City not found. Please check the city name and try again.")
    elif response.status_code == 401:
        print("Invalid API key.")
    else:
        print("something went wrong. please try again later.")

except requests.exceptions.RequestException as e:
        print("request error occurred:", e)


