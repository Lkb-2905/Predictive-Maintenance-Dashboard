🔰 DOSSIER DE SÉCURITÉ ET CONTINUITÉ (PCR/PRA)
⚡ PM-D : Predictive Maintenance Dashboard
Gestion de Crise • Continuité Logistique Ferroviaire • Résilience IA

Classification: Confidentiel (Interne Camrail / Bolloré Logistics) | Version: 1.0.0
Responsable: KAMENI TCHOUATCHEU GAETAN BRUNEL

---

## 🚨 CONTEXTE ET ENJEUX CRITIQUES
Ce plan définit la stratégie de résilience opérationnelle du **Dashboard de Maintenance Prédictive (PM-D)**.
Dans le contexte critique d'une Gare de Fret (Camrail / Douala), l'incapacité à anticiper la panne d'une locomotive de marchandise bloque les voies et stoppe le trafic (Coût d'arrêt majeur).

**Objectifs du PCR :**
* Garantir l'accès aux indicateurs Power BI basiques, même si l'IA est hors ligne.
* Anticiper la perte du modèle.

---

## 🔍 ANALYSE D'IMPACT MÉTIER (BIA)
| Menace Identifiée | Probabilité | Impact | Sévérité |
| :--- | :--- | :--- | :--- |
| **Panne des Capteurs IoT** | Élevée (3/5) | Réception de données `NaN`. | 🟠 Majeur |
| **Échec Entraînement IA** | Moyenne (2/5) | Modèle désuet pour des nouvelles locomotives. | 🟠 Majeur |
| **Perte Fichier Modèle** | Faible (1/5) | Incapacité prédictive totale. | 🔴 Critique |

---

## 🛡️ STRATÉGIES DE CONTINUITÉ (PCA)

### Protocole de Dégradation Gracieuse (Graceful Degradation)
Dans `model_training.py`, les pipelines prévoient un algorithme de secours ou envoient les `features` pures vers l'API si le modèle échoue. 

---

## 🔄 PROCÉDURES DE REPRISE (PRA)

### Reprise Machine Learning "Cold Start"
Si le dossier `models/` est purgé accidentellement :
```powershell
cd "C:\chemin\vers\Predictive-Maintenance-Dashboard"
.\env\Scripts\activate
python src/model_training.py
Write-Host "✅ Modèle RandomForest reconstruit et prêt pour l'inférence."
```

---

## 🔧 ANNEXE TECHNIQUE
### Contacts d'Astreinte
* **Responsable Technique :** Kameni Tchouatcheu
* **Support DevOps :** support-it@camrail.net

*Ce document est la propriété de la Direction Logistique Ferroviaire (Data Department). Dernière mise à jour : Février 2026 par G.B.K.T.*
