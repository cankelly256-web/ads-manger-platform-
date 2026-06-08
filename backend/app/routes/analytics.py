from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.analytics import AnalyticsService

router = APIRouter()
analytics_service = AnalyticsService()


@router.get("/campaigns/{campaign_id}")
async def get_campaign_analytics(campaign_id: str, db: Session = Depends(get_db)):
    """Get analytics for a specific campaign"""
    try:
        analytics = await analytics_service.get_campaign_analytics(campaign_id, db)
        return analytics
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/clients/{client_id}")
async def get_client_analytics(client_id: str, db: Session = Depends(get_db)):
    """Get analytics for a specific client"""
    try:
        analytics = await analytics_service.get_client_analytics(client_id, db)
        return analytics
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/dashboard")
async def get_dashboard_overview(db: Session = Depends(get_db)):
    """Get dashboard overview with aggregated metrics"""
    try:
        overview = await analytics_service.get_dashboard_overview(db)
        return overview
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))