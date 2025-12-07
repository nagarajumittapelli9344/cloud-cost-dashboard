import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def load_cost_data():
    path = BASE_DIR / "data" / "cloud_costs.csv"
    return pd.read_csv(path)

def load_metric_data():
    path = BASE_DIR / "data" / "cloud_metrics.csv"
    return pd.read_csv(path)
