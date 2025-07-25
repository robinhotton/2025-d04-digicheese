from typing import Any
from sqlmodel import Session

from .abstract_service import AbstractService
from ..repositories import ClientRepository
from ..models import ClientCreate, ClientPatch


class ClientService(AbstractService):
    repository: ClientRepository = ClientRepository
    
    @classmethod
    def _process_data(cls, data: ClientCreate | ClientPatch) -> Any:
        """Logique métier spécifique aux clients."""
        data_dict = cls._unpack_data(data)
        
        # Traitement des noms
        if "firstname" in data_dict and data_dict["firstname"]:
            data_dict["firstname"] = data_dict["firstname"].capitalize()
        if "lastname" in data_dict and data_dict["lastname"]:
            data_dict["lastname"] = data_dict["lastname"].upper()
        
        return data_dict
    
    # Méthodes métier spécifiques (optionnelles)
    @classmethod
    def get_by_email(cls, email: str, session: Session):
        """Méthode métier spécifique aux clients."""
        return cls.repository.get_by_email(email=email, session=session)
    
    @classmethod
    def get_active_clients(cls, session: Session):
        """Récupère les clients actifs."""
        return cls.repository.get_active_clients(session=session)