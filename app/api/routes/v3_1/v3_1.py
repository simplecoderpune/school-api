import logging
from fastapi import FastAPI
from app.version import __version__
from app.api.routes.v3_1 import admin

logger = logging.getLogger(__name__)

api_description = "This API is Standalone Self Service API(s) fro School Project"

v3_1_app = FastAPI(
    title="School Project API",
    description=api_description,
    version=__version__,
    contact={"email":"ashvinsrvstv@gmail.com"}
)

v3_1_app.include_router(admin.router, tags=["admin"],prefix="")
