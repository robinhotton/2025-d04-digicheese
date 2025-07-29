from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING
from datetime import date


if TYPE_CHECKING:
    from .user_role import UserRole
    from .role import Role


class UserBase(SQLModel):
    """Schema de base pour les utilisateurs du système."""
    username: str = Field(max_length=50, unique=True, index=True)
    email: str = Field(max_length=255, unique=True, index=True)
    firstname: str = Field(max_length=50)
    lastname: str = Field(max_length=50)
    is_active: bool = Field(default=True)
    
    

class User(UserBase, table=True):
    """Table des utilisateurs du système (staff/admin)."""
    __tablename__ = "users"
    id: int | None = Field(default=None, primary_key=True)
    
    password: str = Field(min_length=6, max_length=255)
    created_at: date = Field(default_factory=date.today)
    last_login: date | None = Field(default=None)
    
    # Relationships
    roles: list["Role"] = Relationship(back_populates="users", link_model=UserRole)


class UserCreate(UserBase):
    """Schema pour la création d'un utilisateur."""
    password: str = Field(min_length=6, max_length=255)


class UserPatch(UserBase):
    """Schema pour la mise à jour d'un utilisateur."""
    username: str | None = Field(default=None, max_length=50)
    email: str | None = Field(default=None, max_length=255)
    firstname: str | None = Field(default=None, max_length=50)
    lastname: str | None = Field(default=None, max_length=50)
    password: str | None = Field(default=None, min_length=6, max_length=255)


class UserPublic(UserBase):
    """Schema public (sans mot de passe)."""
    id: int
    created_at: date
    last_login: date | None