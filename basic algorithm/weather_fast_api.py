from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests

# Jinja HTML dosyalarını dinamik olarak oluşturmaya olanak tanır.

app = FastAPI()
templates = Jinja2Templates(directory="templates")

url = ""

cities = {}

WEATHER_FORM_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hava Durumu Sorgula</title>
</head>
<body>
    <h1>Hava Durumu Sorgula</h1>
    <form action="/weather" method="get">
        <label for="city">Şehir Adı:</label>
        <input type="text" id="city" name="city" required>
        <button type="submit">Sorgula</button>
    </form>
</body>
</html>
"""

WEATHER_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hava Durumu</title>
</head>
<body>
    <h1>{{ weather.location.name }} Hava Durumu</h1>
    <p>Sıcaklık: {{ weather.current.temperature }}°C</p>
    <p>Hava Durumu: {{ weather.current.weather_descriptions[0] }}</p>
    <p>Nem Oranı: {{ weather.current.humidity }}%</p>
    <p>Rüzgar Hızı: {{ weather.current.wind_speed }} km/s</p>
    <a href="/">Yeni Sorgu Yap</a>
</body>
</html>
"""

ERROR_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hata</title>
</head>
<body>
    <h1>Hata Oluştu</h1>
    <p>{{ error }}</p>
    <a href="/">Geri Dön</a>
</body>
</html>
"""