from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/weather")
def weather():
    lat = request.args.get("lat", "40.71")   # default: New York
    lon = request.args.get("lon", "-74.01")
    try:
        resp = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={"latitude": lat, "longitude": lon, "current_weather": True},
            timeout=5,  # never wait forever on an external service
        )
        resp.raise_for_status()  # raise on 4xx/5xx responses
        current = resp.json()["current_weather"]
    except (requests.RequestException, KeyError, ValueError):
        # Return a generic message; don't leak internal error details to users
        return "Weather service unavailable", 502
    return (
        f"Temperature: {current['temperature']} °C, "
        f"wind: {current['windspeed']} km/h"
    )

if __name__ == "__main__":
    app.run(debug=True)  # local only; never ship debug=True