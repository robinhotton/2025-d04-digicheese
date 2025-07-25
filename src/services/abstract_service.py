from abc import ABC
from sqlmodel import Session
from typing import Type, TypeVar, Any

# Type générique pour le repository
RepositoryType = TypeVar('RepositoryType')

class AbstractService(ABC):
    """Classe abstraite pour les services, définissant les méthodes génériques."""
    
    #########################
    # Attributs à redéfinir #
    #########################
    
    repository: Type[RepositoryType]
    SERVICE_NOT_DEFINED_ERROR = "Le repository doit être défini dans la classe concrète"
    
    #########################################
    # Méthodes génériques pour les services #
    #########################################
    
    @classmethod
    def get_all(cls, session: Session, limit: int = 5) -> list[dict]:
        """Retrieve all records with an optional limit."""
        if cls.repository is None:
            raise NotImplementedError(cls.SERVICE_NOT_DEFINED_ERROR)
       
        return cls.repository.get_all(session=session, limit=limit)
   
    @classmethod
    def get_by_id(cls, id: int, session: Session) -> dict | None:
        """Retrieve a record by its ID."""
        if cls.repository is None:
            raise NotImplementedError(cls.SERVICE_NOT_DEFINED_ERROR)
       
        return cls.repository.get_by_id(id=id, session=session)
   
    @classmethod
    def create(cls, data: Any, session: Session) -> dict:
        """Create a new record with business logic processing."""
        if cls.repository is None:
            raise NotImplementedError(cls.SERVICE_NOT_DEFINED_ERROR)
       
        # Traitement des données métier
        processed_data = cls._process_data(data)
       
        # Conversion en dict si nécessaire
        if hasattr(processed_data, 'model_dump'):
            processed_data = processed_data.model_dump(exclude_unset=True)
       
        return cls.repository.create(data=processed_data, session=session)
   
    @classmethod
    def patch(cls, id: int, data: Any, session: Session) -> dict | None:
        """Update a record with business logic processing."""
        if cls.repository is None:
            raise NotImplementedError(cls.SERVICE_NOT_DEFINED_ERROR)
       
        # Traitement des données métier
        processed_data = cls._process_data(data)
       
        # Conversion en dict si nécessaire
        if hasattr(processed_data, 'model_dump'):
            processed_data = processed_data.model_dump(exclude_unset=True)
       
        return cls.repository.patch(id=id, data=processed_data, session=session)
   
    @classmethod
    def delete(cls, id: int, session: Session) -> dict:
        """Delete a record by its ID."""
        if cls.repository is None:
            raise NotImplementedError(cls.SERVICE_NOT_DEFINED_ERROR)
       
        return cls.repository.delete(id=id, session=session)
    
    ##############################################
    # Permet de décomposer les données du schéma #  
    ##############################################
    
    @classmethod
    def _unpack_schema(cls, data: Any) -> dict:
        """
        Unpack the schema if it's a Pydantic model.
        Override in concrete services to implement specific logic.
        Par défaut, retourne les données sans modification.
        """
        if hasattr(data, 'model_dump'):
            return data.model_dump(exclude_unset=True)
        return data.copy() if isinstance(data, dict) else data
    
    ##############################################################
    # Méthodes abstraites à redéfinir dans les services concrets #
    ##############################################################
    
    @classmethod
    def _process_data(cls, data: Any) -> dict:
        """
        Process data before creation or update.
        Override in concrete services to implement specific logic.
        Par défaut, retourne les données sans modification.
        """
        return cls._unpack_schema(data)
    