from abc import ABC, abstractmethod
from sqlmodel import Session

class AbstractRepository(ABC):

    @staticmethod
    @abstractmethod
    def get_all(session: Session, limit: int = 5):
        """Retrieve all records with an optional limit.
        
        Args:
            session (Session): The database session.
            limit (int): The maximum number of records to retrieve.
            
        Returns:
            List[dict]: A list of records as dictionaries."""
        pass
    
    @staticmethod
    @abstractmethod
    def get_by_id(id: int, session: Session):
        """Retrieve a record by its ID.

        Args:
            id (int): The ID of the record to retrieve.
            session (Session): The database session.

        Returns:
            dict: The record as a dictionary, or None if not found."""
        pass
    
    @staticmethod
    @abstractmethod
    def create(data: dict, session: Session):
        """Create a new record with the provided data.

        Args:
            data (dict): The data for the new record.
            session (Session): The database session.

        Returns:
            dict: The created record as a dictionary."""
        pass
    
    @staticmethod
    @abstractmethod
    def patch(id: int, data: dict, session: Session):
        """Update partially an existing record by its ID with the provided data.

        Args:
            id (int): The ID of the record to update.
            data (dict): The new data for the record.
            session (Session): The database session.

        Returns:
            dict: The updated record as a dictionary, or None if not found."""
        pass
    
    @staticmethod
    @abstractmethod
    def delete(id: int, session: Session):
        """Delete a record by its ID.

        Args:
            id (int): The ID of the record to delete.
            session (Session): The database session.

        Returns:
            dict: A message indicating the result of the deletion."""
        pass