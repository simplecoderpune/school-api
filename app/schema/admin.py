from pydantic import BaseModel

class AdminPanelResponse(BaseModel):
    id:str
    name:str
    grade:str