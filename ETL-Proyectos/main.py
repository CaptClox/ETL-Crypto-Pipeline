import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from extract.fetch_data import extract
from Transform.clean_data import transform
from load.load_to_db import load

def run_pipeline():
    print(" Iniciando pipeline ETL...")
    raw = extract()
    cleaned = transform(raw)
    load(cleaned)
    print("Pipeline completado")

if __name__ == "__main__":
    run_pipeline()
