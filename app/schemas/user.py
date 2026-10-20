import uuid
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"

class User(BaseModel):
    id: uuid.UUID
    email: str
    date_joined: datetime
    role: UserRole