from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .commune import Commune


class DepartementBase(SQLModel):
    """Base schema representing French departments."""
    department_code: str = Field(max_length=2, index=True)
    department_name: str = Field(max_length=50)


class Departement(DepartementBase, table=True):
    """Table représentant les départements français."""
    __tablename__ = "t_departement"
    id: int | None = Field(default=None, primary_key=True)
    
    # Relationships
    communes: list["Commune"] = Relationship(back_populates="departement")
    
    
class DepartementPost(DepartementBase):
    pass


class DepartementPatch(DepartementBase):
    department_code: str | None = Field(default=None, max_length=2)
    department_name: str | None = Field(default=None, max_length=50)


class DepartementPublic(DepartementBase):
    id: int