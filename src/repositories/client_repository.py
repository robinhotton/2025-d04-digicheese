from sqlmodel import Session, select
from .abstract_repository import AbstractRepository
from ..models import Client

class ClientRepository(AbstractRepository):
    """Repository for managing Client entities in the database."""

    @staticmethod
    def get_all(limit: int, session: Session):
        statement = select(Client).limit(limit)
        clients = session.exec(statement).all()
        return clients
    
    @staticmethod
    def get_by_id(id: int, session: Session):
        statement = select(Client).where(Client.client_id == id)
        client = session.exec(statement).first()
        if not client:
            return None
        return client
    
    @staticmethod
    def create(data: dict, session: Session):
        new_client = Client(**data)
        session.add(new_client)
        session.commit()
        session.refresh(new_client)
        return new_client
    
    @staticmethod
    def patch(id: int, data: dict, session: Session):
        statement = select(Client).where(Client.client_id == id)
        client = session.exec(statement).first()
        if not client:
            return None
        
        # Update the client with the provided data
        client = client.sqlmodel_update(data)
        
        # Commit the changes to the database
        session.add(client)
        session.commit()
        session.refresh(client)
        return client
    
    @staticmethod
    def delete(id: int, session: Session) -> bool:
        statement = select(Client).where(Client.client_id == id)
        client = session.exec(statement).first()
        if not client:
            return False
        session.delete(client)
        session.commit()
        return True