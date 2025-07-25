from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING
from datetime import date

if TYPE_CHECKING:
    from .user_role import UserRole

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
    password_hash: str = Field(max_length=255)  # Mot de passe hashé
    created_at: date = Field(default_factory=date.today)
    last_login: date | None = Field(default=None)
    
    # Relationships
    user_roles: list["UserRole"] = Relationship(back_populates="user")

class UserCreate(UserBase):
    password: str = Field(min_length=6)  # Mot de passe en clair pour la création

class UserPatch(SQLModel):
    """Schema pour la mise à jour d'un utilisateur."""
    email: str | None = Field(default=None, max_length=255)
    firstname: str | None = Field(default=None, max_length=50)
    lastname: str | None = Field(default=None, max_length=50)
    is_active: bool | None = Field(default=None)
    password: str | None = Field(default=None, min_length=6)  # Nouveau mot de passe

class UserPublic(UserBase):
    """Schema public (sans mot de passe)."""
    id: int
    created_at: date
    last_login: date | None

class UserWithRoles(UserPublic):
    """Schema avec les rôles de l'utilisateur."""
    roles: list[str] = []  # Liste des noms de rôles