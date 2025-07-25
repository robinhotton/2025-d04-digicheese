from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .product import Product

class ProductCategoryBase(SQLModel):
    """Schema de base pour les catégories de produits."""
    name: str = Field(max_length=100, unique=True)
    description: str | None = Field(default=None, max_length=255)
    display_order: int = Field(default=0)

class ProductCategory(ProductCategoryBase, table=True):
    """Table des catégories de produits."""
    __tablename__ = "product_categories"
    
    id: int | None = Field(default=None, primary_key=True)
    
    # Relationships
    products: list["Product"] = Relationship(back_populates="category")

class ProductCategoryCreate(ProductCategoryBase):
    pass

class ProductCategoryPatch(SQLModel):
    """Schema pour la mise à jour d'une catégorie."""
    name: str | None = Field(default=None, max_length=100)
    description: str | None = Field(default=None, max_length=255)
    display_order: int | None = Field(default=None)

class ProductCategoryPublic(ProductCategoryBase):
    id: int