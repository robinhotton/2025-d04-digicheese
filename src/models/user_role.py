from sqlmodel import SQLModel, Field, Relationship, UniqueConstraint
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User
    from .role import Role

class UserRoleBase(SQLModel):
    """Schema de base pour la relation utilisateur-rôle."""
    user_id: int = Field(foreign_key="users.id")
    role_id: int = Field(foreign_key="roles.id")

class UserRole(UserRoleBase, table=True):
    """Table d'association entre utilisateurs et rôles."""
    __tablename__ = "user_roles"
    
    id: int | None = Field(default=None, primary_key=True)
    
    # Relationships
    user: "User" = Relationship(back_populates="user_roles")
    role: "Role" = Relationship(back_populates="user_roles")
    
    # Contrainte d'unicité correcte
    __table_args__ = (UniqueConstraint('user_id', 'role_id', name='unique_user_role'),)

class UserRoleCreate(UserRoleBase):
    pass

# Pas besoin de UserRolePatch car c'est une relation simple (on supprime/recrée)

class UserRolePublic(UserRoleBase):
    id: int