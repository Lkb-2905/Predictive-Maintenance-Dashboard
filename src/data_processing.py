import pandas as pd
from loguru import logger
import os

def clean_data(input_path, output_path):
    logger.info(f"🔄 Chargement des données brutes : {input_path}")
    df = pd.read_csv(input_path)
    
    logger.info("⚙️  Nettoyage et Feature Engineering (Création de variables métier)...")
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Feature Engineering : Moyennes glissantes pour détecter les tendances (Crucial en prévision)
    df = df.sort_values(by=['pump_id', 'timestamp'])
    df['vibration_rolling_mean'] = df.groupby('pump_id')['vibration'].transform(lambda x: x.rolling(window=3, min_periods=1).mean())
    df['pressure_rolling_mean'] = df.groupby('pump_id')['pressure'].transform(lambda x: x.rolling(window=3, min_periods=1).mean())
    
    # Arrondir pour la propreté analytique
    df = df.round(2)
    
    # Traitement des valeurs nulles éventuelles
    df = df.dropna()
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    logger.success(f"🎯 Données traitées et prêtes pour l'analyse : {output_path}")
    return df

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_file = os.path.join(base_dir, "data", "raw_telemetry.csv")
    output_file = os.path.join(base_dir, "data", "processed_telemetry.csv")
    clean_data(input_file, output_file)
