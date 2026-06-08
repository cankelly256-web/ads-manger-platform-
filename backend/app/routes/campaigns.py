from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.campaign import CampaignCreate, CampaignResponse
from app.services.campaign import CampaignService

router = APIRouter()
campaign_service = CampaignService()


@router.get("/", response_model=List[CampaignResponse])
async def list_campaigns(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    """Get all campaigns"""
    campaigns = await campaign_service.get_all_campaigns(db, skip, limit)
    return campaigns


@router.post("/", response_model=CampaignResponse)
async def create_campaign(campaign_data: CampaignCreate, db: Session = Depends(get_db)):
    """Create a new campaign"""
    try:
        campaign = await campaign_service.create_campaign(campaign_data, db)
        return campaign
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{campaign_id}", response_model=CampaignResponse)
async def get_campaign(campaign_id: str, db: Session = Depends(get_db)):
    """Get campaign by ID"""
    campaign = await campaign_service.get_campaign(campaign_id, db)
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return campaign


@router.put("/{campaign_id}", response_model=CampaignResponse)
async def update_campaign(
    campaign_id: str, campaign_data: CampaignCreate, db: Session = Depends(get_db)
):
    """Update campaign"""
    try:
        campaign = await campaign_service.update_campaign(campaign_id, campaign_data, db)
        return campaign
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{campaign_id}")
async def delete_campaign(campaign_id: str, db: Session = Depends(get_db)):
    """Delete campaign"""
    try:
        await campaign_service.delete_campaign(campaign_id, db)
        return {"message": "Campaign deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))