from fastapi import APIRouter
from src.controllers import item_controller

router = APIRouter()
router.include_router(item_controller.router)