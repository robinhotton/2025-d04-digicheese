from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .order import Order
    from .product import Product


class OrderItemBase(SQLModel):
    """Schema de base pour les lignes de commande."""
    quantity: int = Field(ge=1)


class OrderItem(OrderItemBase, table=True):
    """Table des lignes de commande."""
    __tablename__ = "order_items"
    
    order_id: int = Field(foreign_key="orders.id", index=True, primary_key=True)
    product_id: int = Field(foreign_key="products.id", index=True, primary_key=True)
    
    # Relationships
    order_id: "Order" = Relationship(back_populates="items")
    product_id: "Product" = Relationship(back_populates="order_items")


class OrderItemPatch(OrderItemBase):
    """Schema pour la mise à jour d'une ligne de commande."""
    quantity: int | None = Field(default=None, ge=1)


class OrderItemPublic(OrderItemBase):
    """Schema pour exposer les lignes de commande."""
    order_id: int
    product_id: int