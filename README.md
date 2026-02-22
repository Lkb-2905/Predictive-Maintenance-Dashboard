🌍 DOSSIER DE CONFIGURATION D'EXPLOITATION (DCE)
⚡ PM-D : Predictive Maintenance Dashboard
Python Scikit-Learn PowerBI Data Science License

Version: 1.0.0 Stable | Date: Février 2026
Auteur: KAMENI TCHOUATCHEU GAETAN BRUNEL
Contact: gaetanbrunel.kamenitchouatcheu@et.esiea.fr

🚀 Démarrage Rapide • 📚 Documentation • 🎯 Fonctionnalités • 🔧 Installation

📋 TABLE DES MATIÈRES
Vue d'ensemble du projet
Architecture Technique
Stack Technologique
Fonctionnalités Clés
Démarrage Rapide
Guide d'Utilisation
Qualité & Best Practices
Roadmap & Évolutions

🎯 VUE D'ENSEMBLE DU PROJET
Contexte & Objectifs
Ce projet démontre la mise en œuvre d'une architecture orientée Data Science pour la Maintenance Prédictive du matériel ferroviaire (Locomotives de fret pour Camrail / Bolloré Logistics). Il répond aux exigences de disponibilité du matériel en combinant télémétrie et anticipation par l'IA.

✅ Machine Learning : Entraînement d'un Random Forest adapté aux classes déséquilibrées.
✅ Feature Engineering : Création métier de variables temporelles (pression d'huile, vibration d'essieux).
✅ Data Visualization : Modèle de Dashboard Power BI décisionnel pour la salle de contrôle.
✅ Clean Code : Respect des standards (PEP8, Modularité).

Pourquoi ce projet ?
Aspect | Démonstration
--- | ---
Scalabilité | Ingestion de flux de données continus.
Maintenabilité | Code modulaire séparant la génération, le traitement et l'entraînement.
Innovation | Modèle ML de détection d'avaries rares sur des équipements lourds.
Business Value | Limite l'immobilisation des rames logistiques ("Chef de Gare").

🏗️ ARCHITECTURE TECHNIQUE
Diagramme de Flux
Flux de Données Détaillé
1. Génération : Le générateur simule la télémétrie des locomotives en activité.
2. Traitement : Les données brutes sont nettoyées et les features calculées.
3. Apprentissage : Le modèle Random Forest s'entraîne et se sauvegarde (`rf_failure_predict.joblib`).
4. Restitution : Les données sont visualisées dans Power BI.

🛠️ STACK TECHNOLOGIQUE
Technologies Core
Composant | Technologie | Version | Justification Technique
--- | --- | --- | ---
Langage | Python | 3.12+ | Standard mondial de la Data Science.
Machine Learning | Scikit-Learn | Latest | Algorithmes d'arbres robustes et explicables.
Visualisation | Power BI | - | Création de tableaux de bord décisionnels.
Outils | Joblib / Pandas | Latest | Sérialisation et manipulation rapide.

🎯 FONCTIONNALITÉS CLÉS
🚀 Fonctionnalités Principales
Supervision Télémétrique
Suivi des indicateurs de dizaines de locomotives.
Intelligence Artificielle Prédictive
Détecter une avarie avant qu'elle ne bloque une voie.

🛡️ Sécurité & Robustesse
Validation : Traitement des données aberrantes.

🚀 DÉMARRAGE RAPIDE
Prérequis
Python (v3.12+)

Installation Rapide
```bash
# 1. Naviguer dans le dossier du projet
cd Predictive-Maintenance-Dashboard

# 2. Créer l'environnement
python -m venv env
.\env\Scripts\activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Lancer les modules
python src/data_generator.py
python src/data_processing.py
python src/model_training.py
```

📖 GUIDE D'UTILISATION
Scénario de Pilotage
Alimenter Power BI pour identifier immédiatement les rames à risques. Des spécifications sont dans `POWER_BI_SPECS.md`.

📸 Aperçu de l'Exécution
![Exécution du Pipeline ML](execution_screenshot.png)

✨ QUALITÉ & BEST PRACTICES
Standards de Code
Modularité : Séparation en trois phases claires.

🗺️ ROADMAP & ÉVOLUTIONS
Version Actuelle : 1.0.0 ✅
Environnement fonctionnel pour l'entraînement du Random Forest.

🤝 CONTRIBUTION
Les contributions sont les bienvenues.

📄 LICENCE
Ce projet est développé dans un cadre académique et professionnel. Droits réservés.

👨💻 AUTEUR
KAMENI TCHOUATCHEU GAETAN BRUNEL
Ingénieur Logiciel & Data | Étudiant ESIEA

📧 Email : gaetanbrunel.kamenitchouatcheu@et.esiea.fr
🐙 GitHub : @Lkb-2905

© 2026 Kameni Tchouatcheu Gaetan Brunel - Tous droits réservés
