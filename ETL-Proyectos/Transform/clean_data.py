import pandas as pd

def transform(df: pd.DataFrame) -> pd.DataFrame:

    df= df[["id","name","current_price","market_cap",
            "price_change_percentage_24h","last_updated"]]
    
    #limpiar nulos
    df = df.dropna()

    #convertir tipos
    df["last_updated"] = pd.to_datetime(df["last_updated"])
    df["price_change_percentage_24h"] = df["price_change_percentage_24h"].round(2)
    
    #agregar columna de categoría
    df["cap_category"] = df["market_cap"].apply(
        lambda x: "Large" if x > 1e10 else "Mid" if x > 1e9 else "Small"
    )

    print(f"Transformados {len(df)} registros")
    return df