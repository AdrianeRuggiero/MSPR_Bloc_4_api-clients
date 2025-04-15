from fastapi import APIRouter
from app.models.client import Client

router = APIRouter(prefix="/clients", tags=["Clients"])

clients = []

@router.get("", response_model=list[Client])
def get_clients():
    return clients

@router.post("", response_model=Client)
def add_client(client: Client):
    clients.append(client)
    return client

@router.put("/{id}", response_model=Client)
def update_client(id: int, updated_client: Client):
    for i, c in enumerate(clients):
        if c.id == id:
            clients[i] = updated_client
            return updated_client
    return {"detail": "Client non trouvé"}

@router.delete("/{id}")
def delete_client(id: int):
    for i, c in enumerate(clients):
        if c.id == id:
            del clients[i]
            return {"message": f"Client {id} supprimé"}
    return {"detail": "Client non trouvé"}
