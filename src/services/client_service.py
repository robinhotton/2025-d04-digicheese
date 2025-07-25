from typing import Any
from sqlmodel import Session

from .abstract_service import AbstractService
from ..repositories import ClientRepository


class ClientService(AbstractService):
    repository: ClientRepository = ClientRepository  # C'est tout ce qu'il faut définir !
    
    @classmethod
    def _process_data_for_create(cls, data: Any) -> Any:
        """Traitement spécifique pour la création de clients."""
        return cls._traitement_client(data)
    
    @classmethod
    def _process_data_for_update(cls, data: Any) -> Any:
        """Traitement spécifique pour la mise à jour de clients."""
        return cls._traitement_client(data)
    
    @classmethod
    def _traitement_client(cls, data: Any) -> Any:
        """Logique métier spécifique aux clients."""
        # Si c'est un modèle Pydantic, le convertir en dict pour le traitement
        if hasattr(data, 'model_dump'):
            data_dict = data.model_dump(exclude_unset=True)
        else:
            data_dict = data.copy() if isinstance(data, dict) else data
        
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