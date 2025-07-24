from sqlmodel import SQLModel, Field


class ClientBase(SQLModel):
    """Schema de base représentant les clients de la fidélisation de la fromagerie."""
    
    genrecli: str | None = Field(default=None, max_length=8, nullable=True)
    nomcli: str = Field(default=None, max_length=40, index=True)
    prenomcli: str = Field(default=None, max_length=30)
    adresse1cli: str | None = Field(default=None, max_length=50, nullable=True)
    adresse2cli: str | None = Field(default=None, max_length=50, nullable=True)
    adresse3cli: str | None = Field(default=None, max_length=50, nullable=True)
    villecli_id: int | None = Field(default=None, foreign_key="t_communes.id", nullable=True)
    telcli: str | None = Field(default=None, max_length=10, nullable=True)
    emailcli: str | None = Field(default=None, max_length=255, nullable=True)
    portcli: str | None = Field(default=None, max_length=10, nullable=True)
    newsletter: int | None = Field(default=None, nullable=True)


class Client(ClientBase, table=True):
    """Table représentant les clients de la fidélisation de la fromagerie."""
    
    __tablename__ = "t_client"
    
    codcli: int | None = Field(default=None, primary_key=True)
    
class ClientPost(ClientBase):
    pass

class ClientPatch(ClientBase):
    nomcli: str | None = Field(default=None, max_length=40, index=True, nullable=True)
    prenomcli: str | None = Field(default=None, max_length=30, nullable=True)