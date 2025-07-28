from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .commune import Commune


class ClientBase(SQLModel):
    """Schema de base représentant les clients de la fidélisation de la fromagerie."""
    firstname: str | None = Field(default=None, max_length=30, nullable=False)
    lastname: str | None = Field(default=None, max_length=40, index=True, nullable=False)
    gender: str | None = Field(default=None, max_length=8, nullable=True)
    commune_id: int | None = Field(default=None, foreign_key="t_communes.id", nullable=True)
    address_line_1: str | None = Field(default=None, max_length=50, nullable=False)
    address_line_2: str | None = Field(default=None, max_length=50, nullable=True)
    address_line_3: str | None = Field(default=None, max_length=50, nullable=True)
    email: str | None = Field(default=None, max_length=255, nullable=True)
    phone: str | None = Field(default=None, max_length=10, nullable=True)
    mobile_phone: str | None = Field(default=None, max_length=10, nullable=True)
    newsletter: int | None = Field(default=None, nullable=True)


class Client(ClientBase, table=True):
    """Table représentant les clients de la fidélisation de la fromagerie."""
    __tablename__ = "t_client"
    client_id: int | None = Field(default=None, primary_key=True)
    commune: Optional["Commune"] = Relationship(back_populates="clients")
    
    
class ClientPost(ClientBase):
    pass


class ClientPatch(ClientBase):
    lastname: str | None = Field(default=None, max_length=40, index=True, nullable=True)
    firstname: str | None = Field(default=None, max_length=30, nullable=True)
    address_line_1: str | None = Field(default=None, max_length=50, nullable=True)
    
    
class ClientPublic(ClientBase):
    client_id: int