from fastapi import FastAPI
from app.routers.user.api import router as api_router
from app.routers.admin.api import router as admin_router

app = FastAPI(title="Travel Suggestion App")
app.include_router(api_router)
app.include_router(admin_router)