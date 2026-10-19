from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Header
from fastapi.security import OAuth2PasswordBearer
import logging
from app.routers import bookings

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# verify token
async def verify_token(token: Annotated[str, Depends(oauth2_scheme)], x_token: Annotated[str, Header()]):
    if not token or not x_token:
        raise HTTPException(status_code=401, detail="Invalid token")
    return token

app = FastAPI(title="Okada BFF", description="Backend for Okada application", version="0.0.1")
app.include_router(bookings.bookings_router, dependencies=[Depends(verify_token)])


@app.get("/", tags=["root"], summary="Root endpoint")
async def read_root():
    return {"message": "Welcome to Okada BFF"}

