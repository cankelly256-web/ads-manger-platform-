from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey, Float, Text, Enum
from sqlalchemy.sql import func
from app.database import Base
import uuid
import enum


class CampaignStatus(str, enum.Enum):
    DRAFT = "draft"
    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETED = "completed"
    ARCHIVED = "archived"


class CampaignPlatform(str, enum.Enum):
    META = "meta"
    GOOGLE = "google"
    BOTH = "both"


class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    client_id = Column(String, ForeignKey("clients.id"), nullable=False, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    platform = Column(Enum(CampaignPlatform), nullable=False)  # meta, google, both
    status = Column(Enum(CampaignStatus), default=CampaignStatus.DRAFT)
    budget = Column(Float, nullable=False)
    daily_budget = Column(Float, nullable=True)
    start_date = Column(DateTime(timezone=True), nullable=False)
    end_date = Column(DateTime(timezone=True), nullable=True)
    meta_campaign_id = Column(String, nullable=True, unique=True)
    google_campaign_id = Column(String, nullable=True, unique=True)
    objective = Column(String, nullable=True)  # awareness, traffic, conversions, etc.
    audience_targeting = Column(Text, nullable=True)  # JSON string
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<Campaign {self.name}>"