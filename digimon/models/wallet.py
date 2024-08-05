from pydantic import BaseModel, ConfigDict
from typing import Optional
from sqlmodel import Field, SQLModel, create_engine, Session, select, Relationship

class BaseWallet(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    balance: float = 0.0


class CreatedWallet(BaseWallet):
    pass


class UpdatedWallet(BaseWallet):
    pass

class Wallet(BaseWallet):
    id: int

class DBWallet(Wallet, SQLModel, table=True):
    __tablename__ = "wallets"
    id: Optional[int] = Field(default=None, primary_key=True)
    # items: list["DBItem"] = Relationship(back_populates="merchant")


class WalletList(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    wallet: list[Wallet]
    page: int
    page_size: int
    size_per_page: int    