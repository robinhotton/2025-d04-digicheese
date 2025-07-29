from sqlmodel import Session, SQLModel
from abc import ABC, abstractmethod

class AbstractService(ABC):
    
    @staticmethod
    @abstractmethod
    def _traitement(data: SQLModel) -> dict:
        """Process the data before passing it to the repository.

        Args:
            data (SQLModel): The data to process.

        Returns:
            dict: The processed data.
        """
        pass
    
    @staticmethod
    @abstractmethod
    def get_all(limit: int, session: Session):
        """Retrieve all records with an optional limit.
        
        Args:
            limit (int): The maximum number of records to retrieve.
            session (Session): The database session.
        
        Returns:
            List[dict]: A list of records as dictionaries.
        """
        pass
    
    @staticmethod
    @abstractmethod
    def get_by_id(id: int, session: Session):
        """Retrieve a record by its ID.
        
        Args:
            id (int): The ID of the record to retrieve.
            session (Session): The database session.
            
        Returns:
            dict: The record as a dictionary, or None if not found.
        """
        pass
    
    @staticmethod
    @abstractmethod
    def create(data: SQLModel, session: Session):
        """Create a new record with the provided data.
        
        Args:
            data (SQLModel.schema.post): The data for the new record.
            session (Session): The database session.
            
        Returns:
            dict: The created record as a dictionary.
        """
        pass
    
    @staticmethod
    @abstractmethod
    def patch(id: int, data: SQLModel, session: Session):
        """Partially update an existing record by its ID with the provided data.
        
        Args:
            id (int): The ID of the record to update.
            data (SQLModel.schema.patch): The new data for the record.
            session (Session): The database session.
            
        Returns:
            dict: The updated record as a dictionary, or None if not found.
        """
        pass
    
    @staticmethod
    @abstractmethod
    def delete(id: int, session: Session):
        """Delete a record by its ID.
        
        Args:
            id (int): The ID of the record to delete.
            session (Session): The database session.
            
        Returns:
            dict: A message confirming the deletion, or None if not found.
        """
        pass