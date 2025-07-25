from sqlmodel import Session
from ..repositories import ClientRepository as repository
from ..models import ClientPost, ClientPatch


class ClientService:
    
    @staticmethod
    def __traitement(data: dict):
        data["prenom"] = data["prenom"].capitalize()
        data["nom"] = data["nom"].upper()
        return data
    
    @staticmethod
    def get_all(limit: int, session: Session):
        return repository.get_all(limit=limit, session=session)
    
    @staticmethod
    def get_by_id(id: int, session: Session):
        return repository.get_by_id(id=id, session=session)
    
    @staticmethod
    def create(client_data: ClientPost, session: Session):
        data_traite = ClientService.__traitement(client_data) # model_dump()
        return repository.create(data=data_traite, session=session)
    
    @staticmethod
    def patch(id: int, client_data: ClientPatch, session: Session):
        data_traite = ClientService.__traitement(client_data) # model_dump(+option)
        return repository.patch(id=id, data=data_traite, session=session)
    
    @staticmethod
    def delete(id: int, session: Session):
        return repository.delete(id=id, session=session)