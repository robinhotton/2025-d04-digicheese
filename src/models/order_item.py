from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING
from decimal import Decimal

if TYPE_CHECKING:
    from .order import Order
    from .product import Product

class OrderItemBase(SQLModel):
    """Schema de base pour les lignes de commande."""
    order_id: int = Field(foreign_key="orders.id", index=True)
    product_id: int = Field(foreign_key="products.id", index=True)
    quantity: int = Field(ge=1)
    unit_price_at_order: Decimal = Field(decimal_places=2, ge=0)  # Prix au moment de la commande
    subtotal: Decimal = Field(decimal_places=2, ge=0)  # quantity * unit_price_at_order

class OrderItem(OrderItemBase, table=True):
    """Table des lignes de commande."""
    __tablename__ = "order_items"
    
    id: int | None = Field(default=None, primary_key=True)
    
    # Relationships
    order: "Order" = Relationship(back_populates="items")
    product: "Product" = Relationship(back_populates="order_items")

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemPatch(SQLModel):
    """Schema pour la mise à jour d'une ligne de commande."""
    quantity: int | None = Field(default=None, ge=1)
    unit_price_at_order: Decimal | None = Field(default=None, decimal_places=2, ge=0)
    subtotal: Decimal | None = Field(default=None, decimal_places=2, ge=0)

class OrderItemPublic(OrderItemBase):
    id: int

class OrderItemWithProduct(OrderItemPublic):
    """Schema avec les détails du produit."""
    product_name: str
    product_description: str | None = None