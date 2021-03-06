from fastapi import FastAPI
from app.core import config
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from app.catalog import router as catalog_router
from app.user import router as user_router
from app.booking import router as booking_router
from app.auth import router as auth_router

app = FastAPI(title = "Airline-Booking", version = "0.0.1")
@app.get("/", response_class=RedirectResponse, status_code=302)
async def redirect_to_docs():
    return "/docs"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(catalog_router.api_router)
app.include_router(user_router.api_router)
app.include_router(booking_router.api_router)
app.include_router(auth_router.api_router)