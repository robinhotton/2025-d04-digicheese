from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING
from decimal import Decimal

if TYPE_CHECKING:
    from .product_category import ProductCategory
    from .order import Order

class ProductBase(SQLModel):
    """Schema de base pour les produits."""
    name: str = Field(max_length=100)
    description: str | None = Field(default=None, max_length=500)
    unit_price: Decimal = Field(default=0, decimal_places=2, ge=0)
    weight_grams: Decimal = Field(default=0, decimal_places=2, ge=0)
    category_id: int | None = Field(default=None, foreign_key="product_categories.id")
    stock_quantity: int | None = Field(default=0, ge=0)
    stock_alert_threshold: int | None = Field(default=5, ge=0)
    is_active: bool = Field(default=True)


class Product(ProductBase, table=True):
    """Table des produits de la fromagerie."""
    __tablename__ = "products"
    
    id: int | None = Field(default=None, primary_key=True)
    
    # Relationships
    category: "ProductCategory" = Relationship(back_populates="products")
    orders: list["Order"] = Relationship(back_populates="product")


class ProductCreate(ProductBase):
    pass


class ProductPatch(ProductBase):
    """Schema pour la mise à jour d'un produit."""
    name: str | None = Field(default=None, max_length=100)
    

class ProductPublic(ProductBase):
    id: int
    