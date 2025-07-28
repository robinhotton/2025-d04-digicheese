from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .client import Client
    from .departement import Departement


class CommuneBase(SQLModel):
    """Base schema representing French communes."""
    city_name: str | None = Field(default=None, max_length=50, nullable=False)
    postal_code: str | None = Field(default=None, max_length=5, nullable=False)
    departement_id: int | None = Field(default=None, foreign_key="t_departement.id", nullable=True)


class Commune(CommuneBase, table=True):
    """Table représentant les communes associées à un département."""
    __tablename__ = "t_communes"
    id: int | None = Field(default=None, primary_key=True)
    clients: list["Client"] = Relationship(back_populates="commune")
    departement: Optional["Departement"] = Relationship(back_populates="communes")


class CommunePost(CommuneBase):
    pass


class CommunePatch(CommuneBase):
    city_name: str | None = Field(default=None, max_length=50, nullable=True)
    postal_code: str | None = Field(default=None, max_length=5, nullable=True)
    
    
class CommunePublic(CommuneBase):
    id: int