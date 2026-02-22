🔰 DOSSIER DE SÉCURITÉ ET CONTINUITÉ (PCR/PRA)
⚡ PM-D : Predictive Maintenance Dashboard
Gestion de Crise • Continuité Logistique • Résilience IA

Classification: Confidentiel (Interne Camrail / Bolloré Logistics) | Version: 1.0.0
Responsable: KAMENI TCHOUATCHEU GAETAN BRUNEL

🔍 Analyse BIA • 🛡️ Stratégies PCA • 🔄 Procédures PRA • 📝 Maintenance MCO

---

## 📋 TABLE DES MATIÈRES
1. [Contexte & Enjeux Critiques](#-contexte-et-enjeux-critiques)
2. [Analyse d'Impact Métier (BIA)](#-analyse-dimpact-métier-bia)
3. [Stratégies de Continuité (PCA)](#️-stratégies-de-continuité-pca)
4. [Procédures de Reprise (PRA)](#-procédures-de-reprise-pra)
5. [Maintenance & Tests (MCO)](#-maintenance--tests-mco)
6. [Annexe Technique](#-annexe-technique)

---

## 🚨 CONTEXTE ET ENJEUX CRITIQUES
Ce plan définit la stratégie de résilience opérationnelle du **Dashboard de Maintenance Prédictive (PM-D)**.
Dans le contexte critique d'une Gare de Fret (Camrail / Douala), l'incapacité à anticiper la panne d'une locomotive de marchandise bloque les voies et casse le flux logistique de toute la région (Coût d'arrêt majeur).

**Objectifs du PCR :**
* **Disponibilité Data :** Garantir que les gestionnaires aient accès aux indicateurs Power BI basiques, même si l'IA est hors ligne.
* **Intégrité IA :** Assurer que des données corrompues des capteurs ne faussent pas l'algorithme Random Forest.
* **Réactivité :** Temps de reprise rapide pour ne pas perdre la fenêtre d'intervention de maintenance préventive.

---

## 🔍 ANALYSE D'IMPACT MÉTIER (BIA)

### Cartographie des Risques
| Menace Identifiée | Probabilité | Impact Métier | Sévérité |
| :--- | :--- | :--- | :--- |
| **Panne des Capteurs IoT** | Élevée (3/5) | Réception de données `NaN`, calculs statistiques faussés. | 🟠 Majeur |
| **Échec Entraînement IA** | Moyenne (2/5) | Modèle désuet ne détectant pas les pannes des nouvelles locomotives. | 🟠 Majeur |
| **Corruption Fichier CSV** | Faible (1/5) | Tableau de Bord Power BI indisponible (Écran technique). | 🔴 Critique |
| **Perte Fichier Modèle (`.joblib`)**| Très Faible | Incapacité totale à prédire de la panne sur les flux futurs. | 🔴 Critique |

### Métriques de Performance (SLA)
* **RTO (Recovery Time Objective) : < 30 minutes.**
  Temps maximal alloué pour restaurer la source de données Power BI.
* **RPO (Recovery Point Objective) : < 1 heure.**
  Fréquence des flux de télémétrie maximale que l'on accepte de perdre.

---

## 🛡️ STRATÉGIES DE CONTINUITÉ (PCA)
Le PCA repose sur l'approche de *Dégradation Harmonieuse* (Graceful Degradation) : le système continue de fonctionner même affaibli.

### 1. Gestion de la Défaillance des Capteurs (Fallback)
Lors de l'étape de `data_processing.py`, le pipeline contient un filtre strict.
* ⚡ **Mode Nominal :** Lecture des données IoT en temps réel.
* 🚨 **Incident Détecté :** Capteur défectueux envoyant des valeurs aberrantes (-999 bar de pression).
* 🔄 **Basculement Auto :** Pandas utilise la méthode de remplacement (imputation) s'appuyant sur la moyenne mobile historique pour lisser l'anomalie.

### 2. Résilience du Moteur IA (Scikit-Learn)
* **Problème :** Le script de ré-entraînement échoue à cause d'un Data Drift (changement radical des conditions d'exploitation).
* **Solution :** Le système de production charge systématiquement le dernier modèle `rf_failure_predict.joblib` certifié stable, plutôt que de s'arrêter. Les opérationnels gardent une prédiction conservatrice fonctionnelle.

---

## 🔄 PROCÉDURES DE REPRISE (PRA)
En cas de crash de l'architecture nécessitant un redémarrage manuel d'urgence (Crash Power BI ou VM).

### 4.1. Protocole "FAST REBOOT" (PowerShell)
Si les données ne se rafraîchissent plus, exécuter ce script d'urgence par l'astreinte :

```powershell
# SCRIPT DE RÉCUPÉRATION D'URGENCE (PM-D)

# 1. Kill des processus Python suspendus (Zombies)
Stop-Process -Name "python" -Force -ErrorAction SilentlyContinue 
Write-Host "✅ Processus nettoyés."

# 2. Archiver les données corrompues
Rename-Item "data/processed_telemetry.csv" "data/processed_telemetry_CORRUPTED.csv" -ErrorAction SilentlyContinue
Write-Host "✅ Fichier source isolé."

# 3. Relance Forcée du Pipeline
cd "C:\chemin\vers\Predictive-Maintenance-Dashboard"
.\env\Scripts\activate
python src/data_generator.py
python src/data_processing.py
python src/model_training.py
Write-Host "🚀 Télémétrie et IA régénérées !"
```

### 4.2. Stratégie de Sauvegarde (Backup)
* **Modèle IA :** Sauvegarde hebdomadaire des fichiers `.joblib` sur un serveur NAS du site.
* **Code Source :** Versionné en temps réel sur GitLab.

---

## 📝 MAINTENANCE & TESTS (MCO)
La résilience doit être prouvée.

### Scénarios de Test (Réalisés chaque trimestre)
1. **"Blank Data Test" :**
   * *Action :* Injecter un fichier CSV vide dans le processing.
   * *Attendu :* Script lève un `logger.error` propre, ne remplace pas les données saines existantes, et s'arrête gracieusement.
2. **"Model Deletion" :**
   * *Action :* Supprimer le fichier IA de production.
   * *Attendu :* Le Power BI détecte l'absence et affiche le statut "En maintenance - Suivi basique uniquement" sans crasher.

---

## 🔧 ANNEXE TECHNIQUE
### Contacts d'Astreinte
* **Responsable Technique :** Kameni Tchouatcheu (Ext. 06.XX.XX.XX.XX)
* **Support DevOps :** support-it@camrail.net

### Versions Validées en Production
* **Python :** 3.12.x
* **Numpy / Scikit-Learn :** Versions explicitement ancrées dans `requirements.txt`.

*Ce document est la propriété de la Direction Logistique Ferroviaire (Data Department). Dernière mise à jour : Février 2026 par G.B.K.T.*
