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
        return {"message": f"Client 'id={id}' retrieved successfully"}
    
    @staticmethod
    def create(data: dict, session: Session):
        new_client = Client(**data)
        session.add(new_client)
        session.commit()
        session.refresh(new_client)
        return new_client
    
    @staticmethod
    def patch(id: int, data: dict, session: Session):
        return {"message": f"Client 'id={id}' updated successfully", "data": data}
    
    @staticmethod
    def delete(id: int, session: Session):
        return {"message": f"Client 'id={id}' deleted successfully"}