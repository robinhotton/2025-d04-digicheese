from sqlmodel import Session, select
from ..models import Client

class ClientRepository:

    @staticmethod
    def get_all(session: Session, limit: int = 5):
        statement = select(Client).limit(limit)
        clients = session.exec(statement).all()
        return [dict(client) for client in clients]
    
    @staticmethod
    def get_by_id(id: int, session: Session):
        pass
    
    @staticmethod
    def create(client_data: dict, session: Session):
        pass
    
    @staticmethod
    def patch(id: int, client_data: dict, session: Session):
        pass
    
    @staticmethod
    def delete(id: int, session: Session):
        # DO SOMETHING
        return {"message": f"Client 'id={id}' deleted successfully"}