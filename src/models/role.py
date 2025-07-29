from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user_role import UserRole
    from .user import User

class RoleBase(SQLModel):
    """Schema de base pour les rôles utilisateur."""
    name: str = Field(max_length=50, unique=True)
    description: str | None = Field(default=None, max_length=255)

class Role(RoleBase, table=True):
    """Table des rôles utilisateur."""
    __tablename__ = "roles"
    
    id: int | None = Field(default=None, primary_key=True)
    
    # Relationships
    users: list["User"] = Relationship(back_populates="roles", link_model=UserRole)

class RoleCreate(RoleBase):
    """Schema pour la création d'un rôle."""
    pass

class RolePatch(SQLModel):
    """Schema pour la mise à jour d'un rôle."""
    name: str | None = Field(default=None, max_length=50)
    description: str | None = Field(default=None, max_length=255)

class RolePublic(RoleBase):
    """Schema public pour les rôles utilisateur."""
    id: int