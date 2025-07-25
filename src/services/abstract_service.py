from abc import ABC
from sqlmodel import Session
from typing import Type, TypeVar, Any, Optional

# Type générique pour le repository
RepositoryType = TypeVar('RepositoryType')

class AbstractService(ABC):
    # Attributs à redéfinir dans chaque service concret
    repository: Type[RepositoryType]
    SERVICE_NOT_DEFINED_ERROR = "Le repository doit être défini dans la classe concrète"
   
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
        processed_data = cls._process_data_for_create(data)
       
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
        processed_data = cls._process_data_for_update(data)
       
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
   
    # Méthodes de traitement à surcharger dans les services concrets
    @classmethod
    def _process_data_for_create(cls, data: Any) -> Any:
        """
        Process data before creation. Override in concrete services.
        Par défaut, retourne les données sans modification.
        """
        return data
   
    @classmethod
    def _process_data_for_update(cls, data: Any) -> Any:
        """
        Process data before update. Override in concrete services.
        Par défaut, retourne les données sans modification.
        """
        return data