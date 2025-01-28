from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
# Jinja HTML dosyalarını dinamik olarak oluşturmaya olanak tanır.

app = FastAPI()
templates = Jinja2Templates(directory="templates")

url = ""

cities = {}