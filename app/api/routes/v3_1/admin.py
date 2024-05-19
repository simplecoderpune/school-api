from typing import List
from fastapi import APIRouter
from app.schema.admin import AdminPanelResponse
from app.services.admin import get_admin_panel_details


router=APIRouter()

@router.get("/admin",response_model=List[AdminPanelResponse])
def get_admin_panels():
    return get_admin_panel_details()
