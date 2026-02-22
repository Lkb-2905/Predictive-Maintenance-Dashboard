🌍 DOSSIER DE CONFIGURATION D'EXPLOITATION (DCE)
⚡ PM-D PCR : Dossier de Sécurité et Continuité (PRA)
Gestion Crise Logistique IA Résilience License

Version: 1.0.0 Stable | Date: Février 2026
Auteur: KAMENI TCHOUATCHEU GAETAN BRUNEL
Contact: gaetanbrunel.kamenitchouatcheu@et.esiea.fr

🚀 Démarrage Rapide • 📚 Documentation • 🎯 Fonctionnalités • 🔧 Installation

📋 TABLE DES MATIÈRES
Vue d'ensemble du projet
Architecture Technique
Contexte et Enjeux Critiques
Analyse d'Impact Métier (BIA)
Stratégies de Continuité (PCA)
Procédures de Reprise (PRA)
Annexe Technique

🎯 VUE D'ENSEMBLE DU PROJET
Contexte et Objectifs (PCR)
Ce document définit la stratégie de résilience opérationnelle du Dashboard de Maintenance Prédictive (PM-D). Il décrit comment l'application garantit sa continuité logistique ferroviaire. L'incapacité à anticiper la panne d'une locomotive bloque les voies (coût d'arrêt majeur).

Pourquoi ce document ?
Garantir l'accès aux indicateurs basiques si l'IA est hors ligne, et anticiper la perte du modèle.

🏗️ ARCHITECTURE TECHNIQUE
Analyse d'Impact Métier (BIA)
Menace Identifiée | Probabilité | Impact | Sévérité
--- | --- | --- | ---
Panne des Capteurs IoT | Élevée (3/5) | Réception de données `NaN`. | 🟠 Majeur
Échec Entraînement IA | Moyenne (2/5) | Modèle désuet pour des nouvelles locomotives. | 🟠 Majeur
Perte Fichier Modèle | Faible (1/5) | Incapacité prédictive totale. | 🔴 Critique

🛠️ STACK TECHNOLOGIQUE
Stratégies de Continuité (PCA)
Protocole de Dégradation Gracieuse (Graceful Degradation) : Dans le processus `model_training.py`, les pipelines prévoient un algorithme de secours ou envoient les features pures vers l'API si l'évaluation IA échoue.

🎯 FONCTIONNALITÉS CLÉS
Procédures de Reprise (PRA)
Reprise Machine Learning "Cold Start".
Si le dossier `models/` est purgé accidentellement :

🚀 DÉMARRAGE RAPIDE
```powershell
# 1. Restaurer le modèle
cd "C:\chemin\vers\Predictive-Maintenance-Dashboard"
.\env\Scripts\activate

# 2. Entraîner le ML
python src/model_training.py
Write-Host "✅ Modèle RandomForest reconstruit et prêt pour l'inférence."
```

📖 GUIDE D'UTILISATION
Annexe Technique
Contacts d'Astreinte :
Responsable Technique : Kameni Tchouatcheu
Support DevOps : support-it@camrail.net

✨ QUALITÉ & BEST PRACTICES
Maintenance
Ce document est la propriété de la Direction Logistique Ferroviaire. Sécuriser les accès.

🗺️ ROADMAP & ÉVOLUTIONS
Intégration poussée des alertes de continuité à l'aide d'outils modernes, à prévoir dans la V2.0.0.

🤝 CONTRIBUTION
Révisions annuelles recommandées.

📄 LICENCE
Ce document est confidentiel (Interne Camrail / Bolloré Logistics).

👨💻 AUTEUR
KAMENI TCHOUATCHEU GAETAN BRUNEL
Ingénieur Logiciel & Data | Étudiant ESIEA

📧 Email : gaetanbrunel.kamenitchouatcheu@et.esiea.fr
🐙 GitHub : @Lkb-2905

© 2026 Kameni Tchouatcheu Gaetan Brunel - Tous droits réservés
