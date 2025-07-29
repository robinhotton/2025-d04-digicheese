from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .commune import Commune


class DepartementBase(SQLModel):
    """Base schema representing French departments."""
    department_code: str | None = Field(default=None, max_length=2 , nullable=False)
    department_name: str | None = Field(default=None, max_length=50, nullable=False)


class Departement(DepartementBase, table=True):
    """Table représentant les départements français."""
    __tablename__ = "t_departement"
    id: int | None = Field(default=None, primary_key=True)
    communes: list["Commune"] = Relationship(back_populates="departement")
    
    
class DepartementPost(DepartementBase):
    pass


class DepartementPatch(DepartementBase):
    department_code: str | None = Field(default=None, max_length=2 , nullable=True)
    department_name: str | None = Field(default=None, max_length=50, nullable=True)


class DepartementPublic(DepartementBase):
    id: int