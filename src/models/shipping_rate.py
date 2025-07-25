from sqlmodel import SQLModel, Field
from decimal import Decimal

class ShippingRateBase(SQLModel):
    """Schema de base pour les tarifs d'expédition."""
    weight_min_grams: Decimal = Field(decimal_places=2, ge=0)
    weight_max_grams: Decimal | None = Field(default=None, decimal_places=2, ge=0)  # None = illimité
    cost: Decimal = Field(decimal_places=2, ge=0)
    description: str | None = Field(default=None, max_length=100)

class ShippingRate(ShippingRateBase, table=True):
    """Table des tarifs d'expédition selon le poids."""
    __tablename__ = "shipping_rates"
    
    id: int | None = Field(default=None, primary_key=True)

class ShippingRateCreate(ShippingRateBase):
    pass

class ShippingRatePatch(SQLModel):
    """Schema pour la mise à jour d'un tarif d'expédition."""
    weight_min_grams: Decimal | None = Field(default=None, decimal_places=2, ge=0)
    weight_max_grams: Decimal | None = Field(default=None, decimal_places=2, ge=0)
    cost: Decimal | None = Field(default=None, decimal_places=2, ge=0)
    description: str | None = Field(default=None, max_length=100)

class ShippingRatePublic(ShippingRateBase):
    id: int