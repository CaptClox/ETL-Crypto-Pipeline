# ETL Crypto Pipeline 🚀

Pipeline ETL end-to-end que extrae datos de criptomonedas en tiempo real, los transforma y los visualiza en un dashboard interactivo.

## Stack tecnológico

| Etapa | Tecnología |
|---|---|
| Extracción | Python + Requests (CoinGecko API) |
| Transformación | Pandas |
| Carga | DuckDB |
| Visualización | Streamlit |

## Estructura del proyecto

```
etl-crypto-pipeline/
├── extract/
│   └── fetch_data.py       # Extracción desde CoinGecko API
├── Transform/
│   └── clean_data.py       # Limpieza y modelado de datos
├── load/
│   └── load_to_db.py       # Carga a DuckDB
├── dashboard/
│   └── app.py              # Dashboard interactivo
└── main.py                 # Orquestador del pipeline
```

## Cómo correrlo

**1. Instala las dependencias**
```bash
pip install pandas requests duckdb streamlit
```

**2. Corre el pipeline**
```bash
python main.py
```

**3. Abre el dashboard**
```bash
python -m streamlit run dashboard/app.py
```

## Qué hace el pipeline

1. **Extract** — Consume la API de CoinGecko y obtiene datos de las 100 criptomonedas con mayor market cap
2. **Transform** — Limpia nulos, convierte tipos de datos y clasifica por categoría (Large, Mid, Small Cap)
3. **Load** — Persiste los datos en una base de datos analítica DuckDB
4. **Dashboard** — Visualiza métricas, gráficos y tabla filtrable en tiempo real
