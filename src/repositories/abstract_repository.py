from abc import ABC
from sqlmodel import Session, select
from typing import Type, TypeVar, Generic

#################################
# Type générique pour le modèle #
#################################

ModelType = TypeVar('ModelType')

class AbstractRepository(ABC, Generic[ModelType]):
    
    ########################
    # Attribut à redéfinir #
    ########################
    
    model: Type[ModelType]
    MODEL_NOT_DEFINED_ERROR = "Le modèle doit être défini dans la classe concrète"
   
    ############################
    # Méthodes de base du repo #
    ############################
   
    @classmethod
    def get_all(cls, session: Session, limit: int = 5) -> list[dict]:
        """Retrieve all records with an optional limit."""
        if cls.model is None:
            raise NotImplementedError(cls.MODEL_NOT_DEFINED_ERROR)
       
        statement = select(cls.model).limit(limit)
        records = session.exec(statement).all()
        return [dict(record) for record in records]
   
    @classmethod
    def get_by_id(cls, id: int, session: Session) -> dict | None:
        """Retrieve a record by its ID."""
        if cls.model is None:
            raise NotImplementedError(cls.MODEL_NOT_DEFINED_ERROR)
       
        record = session.get(cls.model, id)
        return dict(record) if record else None
   
    @classmethod
    def create(cls, data: dict, session: Session) -> dict:
        """Create a new record with the provided data."""
        if cls.model is None:
            raise NotImplementedError(cls.MODEL_NOT_DEFINED_ERROR)
       
        record = cls.model(**data)
        session.add(record)
        session.commit()
        session.refresh(record)
        return dict(record)
   
    @classmethod
    def patch(cls, id: int, data: dict, session: Session) -> dict | None:
        """Update partially an existing record by its ID."""
        if cls.model is None:
            raise NotImplementedError(cls.MODEL_NOT_DEFINED_ERROR)
       
        record = session.get(cls.model, id)
        if not record:
            return None
       
        # Utilisation de la méthode SQLModel pour l'update
        record.sqlmodel_update(data)
        session.add(record)
        session.commit()
        session.refresh(record)
        return dict(record)
   
    @classmethod
    def delete(cls, id: int, session: Session) -> dict:
        """Delete a record by its ID."""
        if cls.model is None:
            raise NotImplementedError(cls.MODEL_NOT_DEFINED_ERROR)
       
        record = session.get(cls.model, id)
        if not record:
            return {"message": f"Record with id={id} not found"}
       
        session.delete(record)
        session.commit()
        return {"message": f"Record with id={id} deleted successfully"}