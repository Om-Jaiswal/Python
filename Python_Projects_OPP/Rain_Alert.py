import requests
import os
from twillo.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWN_API_KEY")
account_sid = "AC7c357bb2c70d78979800071781270f39"
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": 46.947975,
    "lon": 7.447447,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'http': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client-proxy_client)
    message = client.messages \
        .create(
        body= "It's going to rain today. Remeber to bring an ☂️",
        from_= "+12057362627",
        to= "Your verified number",
    )

    print(message.status)