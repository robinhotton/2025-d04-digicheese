from sqlmodel import SQLModel, Field

class UserRole(SQLModel, table=True):
    """Table d'association entre utilisateurs et rôles."""
    __tablename__ = "user_roles"

    role_id: int | None = Field(default=None, foreign_key="roles.id", primary_key=True)
    user_id: int | None = Field(default=None, foreign_key="users.id", primary_key=True)
