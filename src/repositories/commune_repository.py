from sqlmodel import Session, select
from .abstract_repository import AbstractRepository
from ..models import Commune

class CommuneRepository(AbstractRepository[Commune]):
    """Repository for Commune model, extending the AbstractRepository."""
    
    # Model Concret
    model = Commune
    
    ########################
    # Méthodes spécifiques #
    ########################
    
    @classmethod
    def get_by_postal_code(cls, postal_code: str, session: Session) -> list[dict]:
        """Récupère toutes les communes avec un code postal donné."""
        statement = select(cls.model).where(cls.model.postal_code == postal_code)
        communes = session.exec(statement).all()
        return [dict(commune) for commune in communes]
    
    @classmethod
    def get_by_department_code(cls, department_code: str, session: Session) -> list[dict]:
        """Récupère toutes les communes d'un département."""
        statement = select(cls.model).where(cls.model.department_code == department_code)
        communes = session.exec(statement).all()
        return [dict(commune) for commune in communes]
    
    @classmethod
    def search_by_name(cls, name_pattern: str, session: Session) -> list[dict]:
        """Recherche des communes par nom (recherche partielle)."""
        statement = select(cls.model).where(cls.model.name.ilike(f"%{name_pattern}%"))
        communes = session.exec(statement).all()
        return [dict(commune) for commune in communes]