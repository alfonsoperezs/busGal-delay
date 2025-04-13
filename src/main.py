from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from datetime import datetime

from database import get_session, create_db
from models import Delay, Message
from crud import *
from sqlmodel import Session

tags_metadata = [
    {
        "name": "delay",
        "description": "CRUD operations with delay."
    }
]

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db()
    yield

app = FastAPI(lifespan=lifespan, openapi_tags=tags_metadata)

# Enable CORS
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/delay", tags=["delay"], status_code=201, responses={201: {"model": Delay}, 409: {"model": Message}})
def add_delay(delay: Delay, session: Session = Depends(get_session)):
    delay.real_time = datetime.strptime(delay.real_time, '%Y-%m-%dT%H:%M:%S')
    delay.passing_time = datetime.strptime(delay.passing_time, '%Y-%m-%dT%H:%M:%S')
    inserted_delay = insert_delay(session, delay)
    if inserted_delay is not None:
        return inserted_delay
    else:
        raise HTTPException(status_code=409, detail="Delay already registered")
    
@app.get("/delay", tags=["delay"], responses={200: {"model": list[Delay]}})
def get_all_delays(session: Session = Depends(get_session)):
    return find_delays(session)