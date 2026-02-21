# Spécifications Fonctionnelles : 
# Tableau de Bord Power BI Maintenance Prédictive (TotalEnergies)

## 🎯 Objectif Business
Permettre à un Chef de Dépôt Logistique d'identifier en 5 secondes quelles pompes de carburant risquent de tomber en panne dans les prochaines 48h afin d'envoyer un technicien de maintenance préventive (ROI : Éviter l'interruption des camions de livraison).

## 🗂️ Sources de Données (Intégration Power BI)
1. **Source 1 :** Fichier CSV `Processed_Telemetry.csv` (Historique des capteurs).
2. **Source 2** : Fichier Python `rf_failure_predict.joblib` (Intégration possible avec les scripts Python interactifs dans Power BI pour afficher les scores de probabilités générés par notre modèle Random Forest).

## 🎨 Modèle de Conception (Design)
- **Couleurs Corporate :** Fond gris clair industriel, indicateurs en bleu et rouge (Codes couleurs TotalEnergies).
- **Mode :** Sombre (Dark Mode industriel, apprécié dans les salles de contrôle logistique).

## ⚙️ Construction des Visuels (Maquettes Écrans)

### Écran 1 : La Salle de Contrôle (Overview)
*C'est l'écran par défaut du manager opérationnel*
- **KPI Haut Gauche** : Nombre de pompes monitorées (En Vert).
- **KPI Haut Droite** : "Alerte de Défaillance" - Affiche le nombre d'équipements dont le taux de défaillance prédit (Scikit-Learn) > 85%. En Rouge si > 0.
- **Camembert ou Graphique en Donut** : Répartition de l'état des machines (Fonctionnel / Risque Faible / Risque Critique).
- **Jauge Centrale** : Pression globale moyenne des pompes du site en temps réel.

### Écran 2 : Vision Data Science (Zoom Ingénieur Maintenance)
*C'est l'écran pour l'ingénieur de fiabilité*
- **Line Chart (Courbes Multiples)** : Évolution chronologique des vibrations et pressions par *Pump_ID* lissée sur 3 périodes de temps.
- **Scatter Plot (Nuage de Points)** : Corrélation entre l'Augmentation de la Température (Axe Y) et la Perte de Pression (Axe X). Permet au technicien de voir la "signature" thermique des pannes pétrolières.
- **Tableau Détaillé** : 
    - Colonnes : *Machine_ID | Température | Vibrations Moyennes | **% de Risque (issu de Python)***
    - Formatage Conditionnel : Fond de la cellule en rouge vif dès que le risque dépasse 75%.

## 💡 Astuce pour l'Entretien avec le Recruteur
Lors de votre présentation, précisez : 
> *"Habituellement, l'industrie fait de la maintenance à date fixe (ex: réviser les pompes tous les 6 mois). Mon Dashboard Power BI et mon pipeline Data Science permettent de passer d'une maintenance préventive à une **maintenance prescriptive**, ne ciblant que les équipements à l'agonie. Cela réduit les coûts d'interventions de 30%."*
