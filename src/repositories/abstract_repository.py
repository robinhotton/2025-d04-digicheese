from abc import ABC, abstractmethod
from sqlmodel import Session
from typing import List, Optional, TypeVar, Generic

# Generic type for the model
T = TypeVar('T')

class AbstractRepository(ABC, Generic[T]):
    """Abstract base class for database repositories."""

    @staticmethod
    @abstractmethod
    def get_all(limit: int, offset: int, session: Session) -> List[T]:
        """Retrieve all records with pagination.
        
        Args:
            limit (int): The maximum number of records to retrieve.
            offset (int): The number of records to skip.
            session (Session): The database session.
            
        Returns:
            List[T]: A list of model instances.
        """
        pass
    
    @staticmethod
    @abstractmethod
    def get_by_id(id: int, session: Session) -> Optional[T]:
        """Retrieve a record by its ID.

        Args:
            id (int): The ID of the record to retrieve.
            session (Session): The database session.

        Returns:
            Optional[T]: The model instance, or None if not found.
        """
        pass
    
    @staticmethod
    @abstractmethod
    def create(data: dict, session: Session) -> T:
        """Create a new record with the provided data.

        Args:
            data (dict): The data for the new record.
            session (Session): The database session.

        Returns:
            T: The created model instance.
            
        Raises:
            RuntimeError: If database operation fails.
            ValueError: If data is invalid.
        """
        pass
    
    @staticmethod
    @abstractmethod
    def patch(id: int, data: dict, session: Session) -> Optional[T]:
        """Update partially an existing record by its ID.

        Args:
            id (int): The ID of the record to update.
            data (dict): The new data for the record.
            session (Session): The database session.

        Returns:
            Optional[T]: The updated model instance, or None if not found.
            
        Raises:
            RuntimeError: If database operation fails.
        """
        pass
    
    @staticmethod
    @abstractmethod
    def delete(id: int, session: Session) -> bool:
        """Delete a record by its ID.

        Args:
            id (int): The ID of the record to delete.
            session (Session): The database session.

        Returns:
            bool: True if deleted successfully, False if not found.
            
        Raises:
            RuntimeError: If database operation fails.
        """
        pass
    
    @staticmethod
    @abstractmethod
    def exists(id: int, session: Session) -> bool:
        """Check if a record exists by its ID.

        Args:
            id (int): The ID of the record to check.
            session (Session): The database session.

        Returns:
            bool: True if the record exists, False otherwise.
        """
        pass
    
    @staticmethod
    @abstractmethod
    def count(session: Session) -> int:
        """Count the total number of records.

        Args:
            session (Session): The database session.

        Returns:
            int: The total number of records.
        """
        pass