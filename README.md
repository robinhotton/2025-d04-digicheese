# 🧀 DigiCheese API – Projet TP7

Développement d'une API RESTful pour l'entreprise fictive **DigiCheese**, dans le cadre de la formation Data Engineer 2025-D04.

## 🚀 Fonctionnalités principales

- API développée avec **FastAPI**
- Manipulation des données avec **SQLModel** _(nouvel ORM basé sur SQLAlchemy)_
- Base de données **MySQL / MariaDB**
- Documentation automatique avec **Swagger UI**
- Tests unitaires avec **pytest**
- Typage fort, structure modulaire, normes PEP8

## ✅ Prérequis

- Python 3.10+
- MySQL ou MariaDB (local ou distant)
- `git` (gestion de version)
- (Recommandé) Environnement virtuel Python (`venv`)

## 📁 Structure du projet

```
2025-d04-digicheese/
├── src/
│   ├── main.py             # Point d'entrée FastAPI
│   ├── database.py         # Connexion à la BDD
│   ├── models/             # Modèles & schémas SQLModel
│   ├── repositories/       # Accès aux données
│   ├── services/           # Logique métier
│   └── routers/            # Routes API
│
├── tests/
│   ├── conftest.py         # Configuration des tests
│   └── test_*.py           # Tests unitaires API
│
├── docs/
│   ├── architecture.md     # Architecture logicielle
│   └── serveurs.md         # Configs environnements
│
├── run.py                  # Lancement local
├── .env.template           # Variables d'environnement à copier
├── .gitignore              # Fichiers à ignorer par Git
├── requirements.txt        # Dépendances Python
└── README.md               # Présentation du projet
```

## ⚙️ Installation

1. **Cloner le dépôt**

```bash
git clone https://github.com/robinhotton/2025-d04-digicheese
cd 2025-d04-digicheese
```

2. **Créer l’environnement virtuel**

```bash
python -m venv .venv
.venv\Scripts\activate  # sous unix : `source .venv/bin/activate`
```

3. **Installer les dépendances**

```bash
pip install -r requirements.txt
```

4. **Configurer les variables d’environnement**

```bash
cp .env.template .env
# puis modifier les valeurs (DB_HOST, DB_USER, etc.)
```

## ▶️ Lancer le serveur API

```bash
python run.py
```

* Accès à la documentation : [http://localhost:8000/docs](http://localhost:8000/docs)
* Accès à la documentation ReDoc : [http://localhost:8000/redoc](http://localhost:8000/redoc)

> Si votre application plante, pensez à changer le port dans `run.py` avant de relancer (par défaut 8000).  
> Cela permettra d'éviter les conflits de port.

## 🧪 Lancer les tests

### Exécuter tous les tests

```bash
pytest tests/
```

### Exécuter un test spécifique

```bash
pytest tests/test_ma_fonctionnalite.py
```

## 📬 Contact

* **Référent pédagogique** : [@robinhotton](mailto:rhotton@diginamic-formation.fr)
* **Client** : [@Valentin Momin](mailto:vmomin@diginamic-formation.fr)
