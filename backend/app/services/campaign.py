from sqlalchemy.orm import Session
from app.models.campaign import Campaign
from app.schemas.campaign import CampaignCreate


class CampaignService:
    async def get_all_campaigns(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(Campaign).offset(skip).limit(limit).all()

    async def create_campaign(self, campaign_data: CampaignCreate, db: Session) -> Campaign:
        campaign = Campaign(**campaign_data.dict())
        db.add(campaign)
        db.commit()
        db.refresh(campaign)
        return campaign

    async def get_campaign(self, campaign_id: str, db: Session) -> Campaign:
        return db.query(Campaign).filter(Campaign.id == campaign_id).first()

    async def update_campaign(
        self, campaign_id: str, campaign_data: CampaignCreate, db: Session
    ) -> Campaign:
        campaign = db.query(Campaign).filter(Campaign.id == campaign_id).first()
        if not campaign:
            raise ValueError("Campaign not found")
        for key, value in campaign_data.dict(exclude_unset=True).items():
            setattr(campaign, key, value)
        db.commit()
        db.refresh(campaign)
        return campaign

    async def delete_campaign(self, campaign_id: str, db: Session):
        campaign = db.query(Campaign).filter(Campaign.id == campaign_id).first()
        if not campaign:
            raise ValueError("Campaign not found")
        db.delete(campaign)
        db.commit()