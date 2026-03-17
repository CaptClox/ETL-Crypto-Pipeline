import requests
import pandas as pd
import os

def extract():
    print("📥 Extrayendo datos...")
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {"vs_currency": "usd", "order": "market_cap_desc", "per_page": 100}
    headers = {"accept": "application/json"}
    
    response = requests.get(url, params=params, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Error API: {response.status_code} - {response.text}")
    
    data = response.json()
    
    if not data:
        raise Exception("La API devolvió datos vacíos. Espera 1 minuto y vuelve a intentar.")
    
    df = pd.DataFrame(data)
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/raw_data.csv", index=False)
    print(f"   ✅ Extraídos {len(df)} registros")
    return df

if __name__ == "__main__":
    extract()