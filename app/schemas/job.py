import uuid
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class JobStatus(str, Enum):
    APPLIED = "applied"
    INTERVIEW = "interview"
    OFFER = "offer"
    REJECTED = "rejected"
class Job(BaseModel):
    id: uuid.UUID
    title: str
    url: str
    date_posted: datetime
    date_applied: datetime
    status: JobStatus
