from sqlmodel import Field, SQLModel
from datetime import datetime

class Delay(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    expedition_id: int = Field(default=None, nullable=False)
    line_name: str = Field(default=None, nullable=False)
    real_time: datetime = Field(nullable=False)
    passing_time: datetime = Field(default=None, nullable=False)

