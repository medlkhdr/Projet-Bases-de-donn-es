# 🏨 Système de Réservation d'Hôtel

Ce projet est une application web de gestion de réservations d’hôtels, développée en **Python** avec **SQLite** pour la base de données et **Streamlit** pour l’interface web. Il permet de :

- Gérer les **clients**
- Gérer les **réservations**
- Consulter les **chambres disponibles**
- Afficher les **prestations offertes par les hôtels**
- Visualiser les **évaluations des clients**

---

## 🗂 Structure du projet

```bash
Projet-Bases-de-donnees/
│
├── app.py                # Application principale Streamlit
├── creation.sql          # Script de création des tables SQL
├── insertion.sqlite      # Script d'insertion de données compatible SQLite
├── requetes.sql          # Requêtes SQL pour afficher les données
├── database.py           # Module de connexion et exécution des requêtes
├── hotel_db.sqlite       # Fichier de base de données SQLite
├── requirements.txt      # Dépendances Python
└── README.md             # Ce fichier
````

---

## ⚙️ Installation et exécution

### 1. Cloner le dépôt

```bash
git clone git@github.com:medlkhdr/Projet-Bases-de-donn-es.git
cd Projet-Bases-de-donnees
```

### 2. Créer un environnement virtuel (optionnel mais recommandé)

```bash
python -m venv myenv
source myenv/bin/activate  # Sur Linux/macOS
myenv\Scripts\activate     # Sur Windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Créer et peupler la base de données (si ce n’est pas encore fait)

```bash
sqlite3 hotel_db.sqlite < creation.sql
sqlite3 hotel_db.sqlite < insertion.sql
```

> ⚠️ Le fichier `insertion.sql` est adapté pour SQLite.

---

## 🚀 Lancer l'application

```bash
streamlit run app.py
```

Cela ouvrira automatiquement une page web sur `http://localhost:8501` où vous pouvez utiliser l’interface.

---

## 📋 Fonctionnalités de l’application

### 🔍 Visualisation

* Liste des clients
* Liste des réservations (avec nom du client et ville de l’hôtel)
* Chambres disponibles entre deux dates

### ➕ Ajout

* Ajouter un nouveau client
* Ajouter une réservation en sélectionnant un client et des dates

---

## 🧱 Base de données

La base `hotel_db.sqlite` contient les tables suivantes :

* `Hotel`
* `Client`
* `Prestation`
* `Type_Chambre`
* `Chambre`
* `Reservation`
* `Evaluation`
* `Offre` (association hôtel ↔ prestation)
* `Concerner` (association réservation ↔ type de chambre)

---

## 🛠 Dépendances principales

* Python 3.x
* [Streamlit](https://streamlit.io/)
* SQLite3
* pandas

---

## 📬 Remarques

* En cas de modification du schéma de base de données, il faudra supprimer le fichier `hotel_db.sqlite` et relancer les scripts `creation.sql` puis `insertion.sqlite`.
* Le projet a été développé dans le cadre du TP2 de base de données.

---

## 👨‍💻 Auteurs

* Étudiant : \[MOHAMED LAKHDAR\]
* Université : \[FSSM   _  UCA ]
* Cours : Projet de Base de Données

