from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.client import ClientCreate, ClientResponse
from app.services.client import ClientService

router = APIRouter()
client_service = ClientService()


@router.get("/", response_model=List[ClientResponse])
async def list_clients(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    """Get all clients"""
    clients = await client_service.get_all_clients(db, skip, limit)
    return clients


@router.post("/", response_model=ClientResponse)
async def create_client(client_data: ClientCreate, db: Session = Depends(get_db)):
    """Create a new client"""
    try:
        client = await client_service.create_client(client_data, db)
        return client
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{client_id}", response_model=ClientResponse)
async def get_client(client_id: str, db: Session = Depends(get_db)):
    """Get client by ID"""
    client = await client_service.get_client(client_id, db)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client


@router.put("/{client_id}", response_model=ClientResponse)
async def update_client(
    client_id: str, client_data: ClientCreate, db: Session = Depends(get_db)
):
    """Update client"""
    try:
        client = await client_service.update_client(client_id, client_data, db)
        return client
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{client_id}")
async def delete_client(client_id: str, db: Session = Depends(get_db)):
    """Delete client"""
    try:
        await client_service.delete_client(client_id, db)
        return {"message": "Client deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))