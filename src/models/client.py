from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .commune import Commune
    from .order import Order

class ClientBase(SQLModel):
    """Schema de base pour les clients."""
    firstname: str = Field(max_length=50)
    lastname: str = Field(max_length=50, index=True)
    email: str | None = Field(default=None, max_length=255, index=True)
    phone: str | None = Field(default=None, max_length=15)
    address_line_1: str = Field(max_length=100)
    address_line_2: str | None = Field(default=None, max_length=100)
    commune_id: int | None = Field(default=None, foreign_key="communes.id")
    newsletter_subscription: bool = Field(default=False)

class Client(ClientBase, table=True):
    """Table des clients de la fromagerie."""
    __tablename__ = "clients"
    
    id: int | None = Field(default=None, primary_key=True)
    
    # Relationships
    commune: "Commune" = Relationship(back_populates="clients")
    orders: list["Order"] = Relationship(back_populates="client")

class ClientCreate(ClientBase):
    pass

class ClientPatch(SQLModel):
    """Schema pour la mise à jour d'un client."""
    firstname: str | None = Field(default=None, max_length=50)
    lastname: str | None = Field(default=None, max_length=50)
    email: str | None = Field(default=None, max_length=255)
    phone: str | None = Field(default=None, max_length=15)
    address_line_1: str | None = Field(default=None, max_length=100)
    address_line_2: str | None = Field(default=None, max_length=100)
    commune_id: int | None = Field(default=None)
    newsletter_subscription: bool | None = Field(default=None)

class ClientPublic(ClientBase):
    id: int