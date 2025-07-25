from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user_role import UserRole

class RoleBase(SQLModel):
    """Schema de base pour les rôles utilisateur."""
    name: str = Field(max_length=50, unique=True)
    description: str | None = Field(default=None, max_length=255)

class Role(RoleBase, table=True):
    """Table des rôles utilisateur."""
    __tablename__ = "roles"
    
    id: int | None = Field(default=None, primary_key=True)
    
    # Relationships
    user_roles: list["UserRole"] = Relationship(back_populates="role")

class RoleCreate(RoleBase):
    pass

class RolePatch(SQLModel):
    """Schema pour la mise à jour d'un rôle."""
    name: str | None = Field(default=None, max_length=50)
    description: str | None = Field(default=None, max_length=255)

class RolePublic(RoleBase):
    id: int