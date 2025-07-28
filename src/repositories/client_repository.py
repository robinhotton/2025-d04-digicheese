from sqlmodel import Session, select
from .abstract_repository import AbstractRepository
from ..models import Client

class ClientRepository(AbstractRepository):

    @staticmethod
    def get_all(session: Session, limit: int = 5):
        statement = select(Client).limit(limit)
        clients = session.exec(statement).all()
        return [dict(client) for client in clients]
    
    @staticmethod
    def get_by_id(id: int, session: Session):
        statement = select(Client).where(Client.client_id == id)
        client = session.exec(statement).first()
        if not client:
            return None
        return dict(client)
    
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
        
        for key, value in data.items():
            setattr(client, key, value)
        
        session.add(client)
        session.commit()
        session.refresh(client)
        return client
    
    @staticmethod
    def delete(id: int, session: Session):
        statement = select(Client).where(Client.client_id == id)
        client = session.exec(statement).first()
        if not client:
            return None
        session.delete(client)
        session.commit()
        return {"message": f"Client 'id={id}' deleted successfully"}