from sqlmodel import Session
from ..repositories import ClientRepository as repository
from ..models import ClientPost, ClientPatch


class ClientService:
    
    @staticmethod
    def _traitement(data: ClientPost | ClientPatch, patch: bool = True) -> dict:
        # Drop unset fields if patching
        if patch:
            data = data.model_dump(exclude_unset=True)
        else:
            data = data.model_dump()
        
        # Example processing: Capitalize first name and uppercase last name
        if "firstname" in data and isinstance(data["firstname"], str):
            data["firstname"] = data["firstname"].capitalize()
        if "lastname" in data and isinstance(data["lastname"], str):
            data["lastname"] = data["lastname"].upper()
            
        # Return the processed data
        return data
    
    @staticmethod
    def get_all(limit: int, session: Session):
        return repository.get_all(limit=limit, session=session)
    
    @staticmethod
    def get_by_id(id: int, session: Session):
        return repository.get_by_id(id=id, session=session)
    
    @staticmethod
    def create(data: ClientPost, session: Session):
        data_traite = ClientService._traitement(data)
        return repository.create(data=data_traite, session=session)
    
    @staticmethod
    def patch(id: int, client_data: ClientPatch, session: Session):
        data_traite = ClientService._traitement(client_data)
        return repository.patch(id=id, data=data_traite, session=session)
    
    @staticmethod
    def delete(id: int, session: Session):
        return repository.delete(id=id, session=session)