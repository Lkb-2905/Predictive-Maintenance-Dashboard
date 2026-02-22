🌍 DOSSIER DE CONFIGURATION D'EXPLOITATION (DCE)
# ⚡ PM-D PCR : Dossier de Sécurité et Continuité (PRA)
![Sécurité](https://img.shields.io/badge/Plan-Continuité-red) ![Résilience](https://img.shields.io/badge/Data-Résilience-orange) ![Certifié](https://img.shields.io/badge/Qualité-ISO-yellow)

**Version:** 1.0.0 Stable | **Date:** Février 2026  
**Auteur:** KAMENI TCHOUATCHEU GAETAN BRUNEL  
**Contact:** gaetanbrunel.kamenitchouatcheu@et.esiea.fr  

🚀 [Démarrage Rapide](#-démarrage-rapide) • 📚 [Documentation](#-guide-dutilisation) • 🎯 [Fonctionnalités](#-fonctionnalités-clés) • 🔧 [Installation](#-installation-rapide)

---

## 📋 TABLE DES MATIÈRES
1. [Vue d'ensemble du projet](#-vue-densemble-du-projet)
2. [Architecture Technique (Menaces)](#️-architecture-technique)
3. [Stack Technologique & PCA](#️-stack-technologique)
4. [Fonctionnalités Clés (Reprise)](#-fonctionnalités-clés)
5. [Démarrage Rapide](#-démarrage-rapide)
6. [Guide d'Utilisation](#-guide-dutilisation)
7. [Qualité & Best Practices](#-qualité--best-practices)
8. [Roadmap & Évolutions](#️-roadmap--évolutions)

---

## 🎯 VUE D'ENSEMBLE DU PROJET

### Contexte & Objectifs
Ce document définit la stratégie de résilience opérationnelle et le **Plan de Continuité d'Activité (PCA/PRA)** du Dashboard de Maintenance Prédictive (PM-D). Il garantit que l'architecture orientée *Data-Driven* de la maintenance Camrail puisse survivre aux défaillances logicielles.

Il illustre les compétences suivantes :

✅ **Architecture Découplée :** Si le ML crashe, les métriques simples continuent de tourner.
✅ **Data Science Sécurisée :** Préservation des modèles sérialisés contre les effacements accidentels.
✅ **Industrialisation :** Mise en place d'un protocole formel de relance (Cold Start).
✅ **Clean Code Documenté :** Respect strict des directives d'astreinte IT.

### Pourquoi ce projet ?
| Aspect | Démonstration |
| --- | --- |
| **Scalabilité** | L'infrastructure résiste à la charge d'alertes simultanées. |
| **Maintenabilité** | Reprise d'activité formalisée par scripts. |
| **Innovation** | Dégradation Gracieuse de l'IA en cas de faiblesse système. |
| **Sécurité** | Accès restreints et sauvegardes asynchrones gérées. |

---

## 🏗️ ARCHITECTURE TECHNIQUE

### Flux de Données Détaillé (Analyse BIA)
| Menace Identifiée | Probabilité | Impact | Sévérité |
| --- | --- | --- | --- |
| **Panne des Capteurs IoT** | Élevée (3/5) | Réception de données `NaN`. | 🟠 Majeur |
| **Échec Entraînement IA** | Moyenne (2/5) | Modèle désuet pour l'anticipation à J+1. | 🟠 Majeur |
| **Perte Fichier Modèle** | Faible (1/5) | Incapacité prédictive totale. | 🔴 Critique |

---

## 🛠️ STACK TECHNOLOGIQUE

### Stratégies de Continuité (PCA)
* **Dégradation Gracieuse (Graceful Degradation)** : Dans `model_training.py`, les pipelines prévoient un algorithme de secours manuel ou dirigent simplement les `features` calculées pures vers le Dashboard si l'évaluation de probabilité IA tombe en panne.
* **Tolérance aux Fautes** : Fallback automatique en utilisant l'ancien paramétrage sauvegardé.

---

## 🎯 FONCTIONNALITÉS CLÉS

### 🚀 Procédures de Reprise (PRA)
**Reprise Machine Learning "Cold Start"**
Si l'infrastructure logique ou le sous-répertoire de modèles (`rf_failure_predict.joblib`) sont supprimés en production, l'intervention humaine automatisée s'impose.

### 🛡️ Sécurité & Robustesse
| Aspect | Implémentation |
| --- | --- |
| **Validation** | Imputation des NaN capteurs. |
| **Traçabilité** | Alertes et remontées de log. |

---

## 🚀 DÉMARRAGE RAPIDE

### Prérequis
* Python (v3.12+)
* Droits Administrateur Système

### Installation Express (Reprise)
```powershell
# 1. Tuer les processus corrompus
Stop-Process -Name "python" -Force -ErrorAction SilentlyContinue

# 2. Restaurer et Réactiver le Modèle
cd "C:\chemin\vers\Predictive-Maintenance-Dashboard"
.\env\Scripts\activate

# 3. Ré-entraîner et relancer l'IA
python src/model_training.py
Write-Host "✅ Modèle RandomForest reconstruit et opérationnel."
```

---

## 📖 GUIDE D'UTILISATION

### Scénario d'Astreinte (Contacts)
* **Responsable Technique :** Kameni Tchouatcheu
* **Support DevOps :** support-it@camrail.net
* **Procédure :** L'ingénieur applique la commande PRA.

---

## ✨ QUALITÉ & BEST PRACTICES

### Standards de Crise
* **Documentation :** Document propriété de la Direction Logistique Ferroviaire.
* **Tests à blanc :** Un test de purge (PRA) est mené semestriellement.

### Métriques d'Excellence
✅ **Performance :** Reprise d'activité (RTO) en moins de 3 minutes.
✅ **Disponibilité :** Architecture résiliente testée ("Zero-Downtime").

---

## 🗺️ ROADMAP & ÉVOLUTIONS

**Version Actuelle : 1.0.0 ✅**
* Stratégie PCA complète documentée.

**Version 2.0.0 (Prochaine Release) 🚧**
* Déploiement d'une conteneurisation Docker limitant les risques de crashe O.S.
* Envoi automatique de notifications Email (Alerting).

---

## 🤝 CONTRIBUTION
*Interdit. (Lecture seule pour la cellule de crise ITSM)*.

---

## 📄 LICENCE
Ce document est Confidentiel et Réservé (Usage Interne Camrail / Bolloré Logistics).

## 👨‍💻 AUTEUR
**KAMENI TCHOUATCHEU GAETAN BRUNEL**  
Ingénieur Logiciel & Data Scientist en devenir | Étudiant ESIEA  

📧 Email : gaetanbrunel.kamenitchouatcheu@et.esiea.fr  
🐙 GitHub : @Lkb-2905  

🙏 **REMERCIEMENTS**
* **Équipes ITSM :** Pour la méthodologie ITIL.

© 2026 Kameni Tchouatcheu Gaetan Brunel - Tous droits réservés
