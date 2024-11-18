import os
from typing import List

from databases import Database
from dotenv import load_dotenv
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from models import GroupingData
from services.querys import get_tenant_data, get_agent_data, get_state_data

load_dotenv()
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

app = FastAPI(title="FastAPI Taurus",
              description="Esta es una API para la prueba tecnica de taurus con FastAPI",
              version="1.0.0",
              openapi_url="/openapi.json",
              docs_url="/",
              redoc_url="/docs"
              )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = f"mysql+aiomysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
database = Database(DATABASE_URL)

engine = create_async_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, autocommit=False, autoflush=False)


@app.get("/data", response_model=List[GroupingData.GroupingData])
async def get_data(
        grouping_type: str = Query(..., enum=["tenant", "agent", "state"], description="Tipo de agrupación")):
    async with SessionLocal() as session:
        if grouping_type == "tenant":
            return await get_tenant_data(session)
        elif grouping_type == "agent":
            return await get_agent_data(session)
        elif grouping_type == "state":
            return await get_state_data(session)
        else:
            return []
