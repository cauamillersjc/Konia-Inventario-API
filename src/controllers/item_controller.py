from fastapi import APIRouter, HTTPException

from src.models.item_model import ItemModel
from src.services.item_service import ItemService

router = APIRouter(
    prefix="/api/v1/items",
    tags=["items"],
    responses={404: {"description": "Not found"}}
)

service = ItemService()

@router.get("/")
def get_items():
    return service.get()

@router.post("/", status_code=201)
def create_item(item: ItemModel):
    if item.name is None:
        raise HTTPException(status_code=400, detail="Field \"name\" is required")
    
    items = service.get()
    
    for x in items:
        if item.name == x.name:
            raise HTTPException(status_code=409, detail="Item is already registered")
    
    return service.create(item)