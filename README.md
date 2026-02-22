# 🚂 Predictive Maintenance Dashboard ML V1.0
![Python](https://img.shields.io/badge/Python-3.12-blue) ![Scikit-Learn](https://img.shields.io/badge/Scikit_Learn-Machine_Learning-orange) ![Power BI](https://img.shields.io/badge/Power_BI-Industrial_Dashboard-yellow)

**Version:** 1.0.0 Stable | **Date:** Février 2026  
**Auteur:** KAMENI TCHOUATCHEU GAETAN BRUNEL  

---

## 🎯 VUE D'ENSEMBLE DU PROJET

Ce projet démontre la mise en œuvre d'une architecture orientée Data Science pour la **Maintenance Prédictive** du matériel ferroviaire (Locomotives de fret pour Camrail / Bolloré Logistics).

✅ **Machine Learning :** Entraînement d'un Random Forest adapté aux classes déséquilibrées (pannes rares).
✅ **Feature Engineering :** Création métier de variables temporelles (pression d'huile, vibration d'essieux).
✅ **Data Visualization :** Modèle de Dashboard Power BI décisionnel pour la salle de contrôle.

---

## 🏗️ ARCHITECTURE TECHNIQUE

1. **Génération (Ingestion Systèmes)** : `data_generator.py` simule la télémétrie de dizaines de locomotives.
2. **Traitement (Feature Engineering)** : `data_processing.py` nettoie et agrège les indicateurs pour l'IA.
3. **Apprentissage (Data Science)** : `model_training.py` s'entraîne, calcule les risques d'avarie imminente et sauvegarde son intelligence dans un fichier `rf_failure_predict.joblib`.

---

## 🚀 DÉMARRAGE RAPIDE

```bash
# 1. Naviguer dans le dossier du projet
cd Predictive-Maintenance-Dashboard

# 2. Créer l'environnement
python -m venv env
.\env\Scripts\activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Lancer les modules séquentiellement
python src/data_generator.py
python src/data_processing.py
python src/model_training.py
```

Le fichier `models/rf_failure_predict.joblib` sera généré, prêt à être déployé pour l'interface de visualisation.

---

## 📖 GUIDE D'UTILISATION & POWER BI

Des spécifications visuelles précises ont été rédigées dans `POWER_BI_SPECS.md` pour permettre la création d'un tableau de bord efficace orienté vers le "Chef de Gare" pour limiter l'immobilisation des rames logistiques.

© 2026 Kameni Tchouatcheu Gaetan Brunel - Tous droits réservés
