import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta
from loguru import logger

def generate_data(output_path, num_records=5000):
    logger.info("🚀 Début : Génération de données synthétiques pour les pompes logistiques...")
    np.random.seed(42)
    
    # 10 pompes de dépôt logistique
    pump_ids = [f"PUMP_{i:03d}" for i in range(1, 11)]
    start_date = datetime.now() - timedelta(days=30)
    
    timestamps = [start_date + timedelta(hours=i) for i in range(num_records)]
    
    data = []
    for ts in timestamps:
        pump = np.random.choice(pump_ids)
        
        # Base métriques normales
        flow_rate = np.random.normal(500, 50)     # Débit L/min
        pressure = np.random.normal(5, 0.5)       # Pression en Bar
        vibration = np.random.normal(2, 0.2)      # Vibration mm/s
        temperature = np.random.normal(45, 5)     # Température Celsius
        
        failure = 0
        # Simulation d'une anomalie/panne imminente (5% du temps)
        if np.random.rand() > 0.95: 
            vibration += np.random.normal(3, 1)   # Hausse anormale de vibration
            pressure -= np.random.normal(2, 0.5)  # Chute de pression
            temperature += np.random.normal(15, 5) # Surchauffe
            
            # 70% de ces anomalies mènent à une panne constatée
            if np.random.rand() > 0.3:
                failure = 1 
                
        data.append([ts, pump, flow_rate, pressure, vibration, temperature, failure])
        
    df = pd.DataFrame(data, columns=['timestamp', 'pump_id', 'flow_rate', 'pressure', 'vibration', 'temperature', 'failure'])
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    logger.success(f"✅ Données générées avec succès : {output_path} ({len(df)} lignes enregistrées)")

if __name__ == "__main__":
    # Définition du chemin relatif pour exécution depuis divers dossiers
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_file = os.path.join(base_dir, "data", "raw_telemetry.csv")
    generate_data(output_file)
