from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class ClientCreate(BaseModel):
    name: str
    email: EmailStr
    company_name: Optional[str] = None
    phone: Optional[str] = None
    description: Optional[str] = None


class ClientResponse(BaseModel):
    id: str
    name: str
    email: str
    company_name: Optional[str]
    phone: Optional[str]
    description: Optional[str]
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True