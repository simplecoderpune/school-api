from app.schema.admin import AdminPanelResponse
from typing import List
def get_admin_panel_details():
    return [
        AdminPanelResponse(
            id="1",
            name="Mark",
            grade="A"
        ),
        AdminPanelResponse(
            id="2",
            name="Antony",
            grade="B"
        )
    ]