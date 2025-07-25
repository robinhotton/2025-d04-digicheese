from os import path
from sqlmodel import Session, select
from .abstract_repository import AbstractRepository
from ..models import Client

class ClientRepository(AbstractRepository[Client]):
    """Repository for Client model, extending the AbstractRepository."""
   
    # Model Concret
    model = Client
   
   ########################
   # Méthodes spécifiques #
   ########################

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