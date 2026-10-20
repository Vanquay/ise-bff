import uuid
from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: uuid.UUID
    email: str