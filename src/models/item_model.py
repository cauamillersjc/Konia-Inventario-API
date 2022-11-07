from pydantic import BaseModel
from datetime import datetime

class ItemModel(BaseModel):
    id: int = 1
    name: str | None
    created_at: datetime | None