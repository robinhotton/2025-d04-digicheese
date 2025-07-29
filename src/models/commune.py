from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .client import Client
    from .departement import Departement

class CommuneBase(SQLModel):
    """Schema de base pour les communes françaises."""
    name: str = Field(max_length=100)
    postal_code: str = Field(max_length=5, index=True)
    department_code: str = Field(min_length=2, max_length=3)

class Commune(CommuneBase, table=True):
    """Table des communes françaises."""
    __tablename__ = "communes"
    id: int | None = Field(default=None, primary_key=True)
    
    # Relationships
    clients: list["Client"] = Relationship(back_populates="commune")
    departement: Optional["Departement"] = Relationship(back_populates="communes")


class CommuneCreate(CommuneBase):
    pass


class CommunePatch(SQLModel):
    """Schema pour la mise à jour d'une commune."""
    name: str | None = Field(default=None, max_length=100)
    postal_code: str | None = Field(default=None, max_length=5)
    department_code: str | None = Field(default=None, max_length=3)


class CommunePublic(CommuneBase):
    id: int