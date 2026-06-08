from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.analytics import CampaignAnalytics, ClientAnalytics
from app.models.campaign import Campaign


class AnalyticsService:
    async def get_campaign_analytics(self, campaign_id: str, db: Session):
        campaign = db.query(Campaign).filter(Campaign.id == campaign_id).first()
        if not campaign:
            raise ValueError("Campaign not found")

        analytics = (
            db.query(CampaignAnalytics)
            .filter(CampaignAnalytics.campaign_id == campaign_id)
            .all()
        )

        if not analytics:
            return {
                "campaign_id": campaign_id,
                "campaign_name": campaign.name,
                "data": [],
            }

        return {
            "campaign_id": campaign_id,
            "campaign_name": campaign.name,
            "data": analytics,
        }

    async def get_client_analytics(self, client_id: str, db: Session):
        analytics = (
            db.query(ClientAnalytics)
            .filter(ClientAnalytics.client_id == client_id)
            .all()
        )
        return {"client_id": client_id, "data": analytics}

    async def get_dashboard_overview(self, db: Session):
        total_spend = db.query(func.sum(CampaignAnalytics.spend)).scalar() or 0
        total_impressions = db.query(func.sum(CampaignAnalytics.impressions)).scalar() or 0
        total_clicks = db.query(func.sum(CampaignAnalytics.clicks)).scalar() or 0
        total_conversions = (
            db.query(func.sum(CampaignAnalytics.conversions)).scalar() or 0
        )

        return {
            "total_spend": total_spend,
            "total_impressions": total_impressions,
            "total_clicks": total_clicks,
            "total_conversions": total_conversions,
            "average_ctr": (
                (total_clicks / total_impressions * 100)
                if total_impressions > 0
                else 0
            ),
        }