import os
from sqlmodel import create_engine, Session

# Configuration de la base de données
DB_CONFIG = {
    "connector": "mysql+pymysql",
    "username": os.environ.get("DB_USERNAME", "root"),
    "password": os.environ.get("DB_PASSWORD", "root"),
    "host":     os.environ.get("DB_HOST",     "localhost"),
    "port":     os.environ.get("DB_PORT",     "3306"),
    "database": os.environ.get("DB_NAME",     "digicheese")
}

# URL de connexion à la base de données
CONNEXION_STRING = "{connector}://{username}:{password}@{host}:{port}/{database}"
DATABASE_URL = CONNEXION_STRING.format(**DB_CONFIG)

# Moteur de base de données
engine = create_engine(DATABASE_URL, echo=False)

# déclaration d'une base qui permet après de créer un modèle et de mapper avec SqlModel
def get_db():
    """
    Fonction génératrice pour fournir une session de base de données.
    Laisse ouverte la session pour les opérations de base de données et la ferme après utilisation.
    """
    db = Session(engine, autoflush=False, autocommit=False)
    try:
        yield db
    finally:
        db.close()
        
# Il est possible de créer des fonctions utilitaires pour supprimer et recréer la base de données
# Attention à ne pas essayer de se connecter à la base de données pendant cette opération (DATABASE_URL)