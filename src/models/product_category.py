from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .product import Product


class ProductCategoryBase(SQLModel):
    """Schema de base pour les catégories de produits."""
    name: str = Field(max_length=100, unique=True)
    description: str | None = Field(default=None, max_length=255)


class ProductCategory(ProductCategoryBase, table=True):
    """Table des catégories de produits."""
    __tablename__ = "product_categories"
    
    id: int | None = Field(default=None, primary_key=True)
    
    # Relationships
    products: list["Product"] = Relationship(back_populates="category")


class ProductCategoryCreate(ProductCategoryBase):
    pass


class ProductCategoryPatch(ProductCategoryBase):
    """Schema pour la mise à jour d'une catégorie."""
    name: str | None = Field(default=None, max_length=100)


class ProductCategoryPublic(ProductCategoryBase):
    id: int