import os
import requests
from datetime import datetime

API_KEY = os.getenv("API_FOOTBALL_KEY")
TG_TOKEN = os.getenv("TELEGRAM_TOKEN")
TG_CHAT = os.getenv("TELEGRAM_CHAT_ID")

# 🔹 Obtener partidos de hoy con cuotas
url = "https://v3.football.api-sports.io/odds"
headers = {"x-apisports-key": API_KEY}
today = datetime.utcnow().strftime("%Y-%m-%d")

params = {"date": today, "bookmaker": 8}  # 8 = Bet365
resp = requests.get(url, headers=headers, params=params)
data = resp.json()

msg = f"📊 Value Bets para {today}\n\n"

for match in data.get("response", []):
    home = match["teams"]["home"]["name"]
    away = match["teams"]["away"]["name"]
    odds = match["bookmakers"][0]["bets"][0]["values"]

    for odd in odds:
        market = odd["value"]
        cuota = float(odd["odd"])
        prob_implicita = 1 / cuota * 100

        # Ejemplo de filtro simple
        if cuota:
            print(f"La cuota existe: {cuota}")
