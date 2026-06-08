from sqlalchemy.orm import Session
from app.models.client import Client
from app.schemas.client import ClientCreate


class ClientService:
    async def get_all_clients(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(Client).offset(skip).limit(limit).all()

    async def create_client(self, client_data: ClientCreate, db: Session) -> Client:
        client = Client(**client_data.dict())
        db.add(client)
        db.commit()
        db.refresh(client)
        return client

    async def get_client(self, client_id: str, db: Session) -> Client:
        return db.query(Client).filter(Client.id == client_id).first()

    async def update_client(
        self, client_id: str, client_data: ClientCreate, db: Session
    ) -> Client:
        client = db.query(Client).filter(Client.id == client_id).first()
        if not client:
            raise ValueError("Client not found")
        for key, value in client_data.dict(exclude_unset=True).items():
            setattr(client, key, value)
        db.commit()
        db.refresh(client)
        return client

    async def delete_client(self, client_id: str, db: Session):
        client = db.query(Client).filter(Client.id == client_id).first()
        if not client:
            raise ValueError("Client not found")
        db.delete(client)
        db.commit()