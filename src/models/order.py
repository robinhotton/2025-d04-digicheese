from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING
from datetime import date, datetime
from decimal import Decimal
from enum import Enum

if TYPE_CHECKING:
    from .client import Client
    from .order_item import OrderItem

class OrderStatus(str, Enum):
    """Statuts des commandes."""
    PENDING = "pending"
    CONFIRMED = "confirmed"
    PREPARING = "preparing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class OrderBase(SQLModel):
    """Schema de base pour les commandes."""
    order_date: date = Field(default_factory=date.today)
    client_id: int = Field(foreign_key="clients.id", index=True)
    status: OrderStatus = Field(default=OrderStatus.PENDING)
    total_amount: Decimal = Field(default=Decimal("0.00"), decimal_places=2, ge=0)
    shipping_cost: Decimal = Field(default=Decimal("0.00"), decimal_places=2, ge=0)
    notes: str | None = Field(default=None, max_length=500)

class Order(OrderBase, table=True):
    """Table des commandes."""
    __tablename__ = "orders"
    
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)
    shipped_at: datetime | None = Field(default=None)
    delivered_at: datetime | None = Field(default=None)
    
    # Relationships
    client: "Client" = Relationship(back_populates="orders")
    items: list["OrderItem"] = Relationship(back_populates="order")

class OrderCreate(OrderBase):
    pass

class OrderPatch(SQLModel):
    """Schema pour la mise à jour d'une commande."""
    status: OrderStatus | None = Field(default=None)
    total_amount: Decimal | None = Field(default=None, decimal_places=2, ge=0)
    shipping_cost: Decimal | None = Field(default=None, decimal_places=2, ge=0)
    notes: str | None = Field(default=None, max_length=500)
    shipped_at: datetime | None = Field(default=None)
    delivered_at: datetime | None = Field(default=None)

class OrderPublic(OrderBase):
    id: int
    created_at: datetime
    shipped_at: datetime | None
    delivered_at: datetime | None

class OrderWithItems(OrderPublic):
    """Schema avec les détails de la commande."""
    items: list["OrderItemPublic"] = []