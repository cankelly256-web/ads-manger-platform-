from sqlalchemy import Column, String, DateTime, Float, Integer, ForeignKey, Text
from sqlalchemy.sql import func
from app.database import Base
import uuid


class CampaignAnalytics(Base):
    __tablename__ = "campaign_analytics"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    campaign_id = Column(String, ForeignKey("campaigns.id"), nullable=False, index=True)
    date = Column(DateTime(timezone=True), server_default=func.now())
    platform = Column(String, nullable=False)  # meta or google
    impressions = Column(Integer, default=0)
    clicks = Column(Integer, default=0)
    conversions = Column(Integer, default=0)
    spend = Column(Float, default=0.0)
    ctr = Column(Float, default=0.0)  # Click-through rate
    cpc = Column(Float, default=0.0)  # Cost per click
    cpa = Column(Float, default=0.0)  # Cost per acquisition
    roas = Column(Float, default=0.0)  # Return on ad spend
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<CampaignAnalytics {self.campaign_id} {self.date}>"


class ClientAnalytics(Base):
    __tablename__ = "client_analytics"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    client_id = Column(String, ForeignKey("clients.id"), nullable=False, index=True)
    date = Column(DateTime(timezone=True), server_default=func.now())
    total_spend = Column(Float, default=0.0)
    total_impressions = Column(Integer, default=0)
    total_clicks = Column(Integer, default=0)
    total_conversions = Column(Integer, default=0)
    average_roas = Column(Float, default=0.0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<ClientAnalytics {self.client_id} {self.date}>"