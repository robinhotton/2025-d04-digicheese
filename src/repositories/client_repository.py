from sqlmodel import Session, select
from .abstract_repository import AbstractRepository
from ..models import Client

class ClientRepository(AbstractRepository[Client]):  # ✅ Ajout du type générique
    """Repository for Client model, extending the AbstractRepository."""
   
    # Définition du modèle spécifique pour ce repository
    model = Client
   
    # Optionnel : surcharger ou ajouter des méthodes spécifiques si besoin
    @classmethod
    def get_by_email(cls, email: str, session: Session):
        """Récupère un client par son email."""
        statement = select(cls.model).where(cls.model.email == email)
        client = session.exec(statement).first()
        return dict(client) if client else None
    
    @classmethod
    def get_active_clients(cls, session: Session):
        """Récupère tous les clients qui ont souscrit à la newsletter."""
        statement = select(cls.model).where(cls.model.newsletter_subscription == True)
        clients = session.exec(statement).all()
        return [dict(client) for client in clients]