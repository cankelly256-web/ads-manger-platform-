from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional
from enum import Enum


class CampaignStatus(str, Enum):
    DRAFT = "draft"
    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETED = "completed"
    ARCHIVED = "archived"


class CampaignPlatform(str, Enum):
    META = "meta"
    GOOGLE = "google"
    BOTH = "both"


class CampaignCreate(BaseModel):
    name: str
    description: Optional[str] = None
    platform: CampaignPlatform
    budget: float
    daily_budget: Optional[float] = None
    start_date: datetime
    end_date: Optional[datetime] = None
    objective: Optional[str] = None
    audience_targeting: Optional[str] = None


class CampaignResponse(BaseModel):
    id: str
    client_id: str
    name: str
    description: Optional[str]
    platform: CampaignPlatform
    status: CampaignStatus
    budget: float
    daily_budget: Optional[float]
    start_date: datetime
    end_date: Optional[datetime]
    objective: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True