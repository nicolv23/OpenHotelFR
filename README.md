# OpenHotelFR
OpenHotelFR est une application web développée en Python avec le framework Flask, permettant de gérer les réservations, les chambres et les clients d’un hôtel. Le projet propose une interface web moderne et intuitive, ainsi qu’un backend structuré et extensible. Il sert de base à un véritable système de gestion hôtelière open‑source. 

--- 
## Fonctionnalités prévues 

- Gestion des chambres (création, modification, disponibilité) 
- Gestion des clients - Système de réservation complet 
- Interface web simple et intuitive 
- Architecture modulaire prête pour évoluer : 
    - authentification 
    - tableau de bord 
    - statistiques 
    - intégration d’une base de données SQL 

--- 

## Technologies utilisées 

- **Python 3** 
- **Flask** 
- HTML / CSS 
- *(À venir)* SQLAlchemy 
- *(À venir)* Bootstrap --- 

## Structure du projet

OpenHotelFR/
│
├── app/                    
# Code principal de l'application Flask
│   ├── __init__.py          
# Fonction create_app() et configuration de l'app
│   ├── bd.py                
# (À venir) Initialisation de la base de données
│   │
│   ├── routes/              
# Dossiers contenant les Blueprints (routes)
│   │   └── main.py          
# Routes principales (page d'accueil)
│   │
│   ├── templates/           
# Templates HTML (Jinja2)
│   │   ├── layout.html      
# Template de base (héritage)
│   │   └── index.html       
# Page d'accueil
│   │
│   └── static/             
# Fichiers statiques (CSS, JS, images)
│
├── config.py                
# Configuration globale de l'application
├── run.py                   
# Point d'entrée pour lancer Flask
├── requirements.txt         
# Dépendances Python
└── README.md                
# Documentation du projet


## Description des éléments du projet 

### **app/** 
Contient tout le code principal de l’application Flask. C’est le cœur du projet. 

### **app/__init__.py** 
Met en place la fonction `create_app()`, configure l’application et enregistre les Blueprints. 

### **app/bd.py** 
Fichier réservé à l’initialisation de la base de données (SQLAlchemy, migrations, etc.). 

### **app/routes/** 
Contient les Blueprints, permettant une organisation modulaire des routes. 

### **app/routes/main.py** 
Gère les routes principales, notamment la page d’accueil. 

### **app/templates/** 
Contient les templates HTML rendus par Flask via Jinja2. 

- **layout.html** : template de base utilisé pour l’héritage 
- **index.html** : page d’accueil 

### **app/static/** 
Fichiers statiques : CSS, JavaScript, images, logos, etc. 

### **config.py** 
Centralise la configuration de l’application (clé secrète, base de données, options futures). 

### **run.py** 
Point d’entrée pour lancer l’application Flask en local. 

### **requirements.txt** 
Liste des dépendances Python nécessaires au projet. ### **README.md** Documentation du projet, instructions d’installation et informations générales.

---

## Installation

### 1. Cloner le projet

```bash
git clone https://github.com/ton-utilisateur/OpenHotelFR.git
cd OpenHotelFR
```

### 2. Créer un environnement virtuel (Git Bash)

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Lancer l'application 

```bash
python run.py
```

Puis ouvrir dans votre navigateur:

`http://127.0.0.1:5000`