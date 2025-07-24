from sqlmodel import Session, select
from ..models import Client

class ClientRepository:
    def __init__(self, session: Session):
        self.session: Session = session
        
    def get_all(self, limit:int=5):
        statement = select(Client).limit(limit)
        result = self.session.exec(statement).all()
        return [dict(client) for client in result]