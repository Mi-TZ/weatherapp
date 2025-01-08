import requests

def get_weather_data(city):
    api_key = "f5b8b5c525e5a50b0924d16cf3224625"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "APPID" : api_key,
        "units" : "metric"
    }

    response = requests.get(url, params=params)
    if(response.status_code == 200):
        return response.json()
    else:
        return None