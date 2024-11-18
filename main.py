from dotenv import load_dotenv
import os
from fastapi import FastAPI, Query
from databases import Database
from fastapi.middleware.cors import CORSMiddleware

from typing import List

from models import GroupingData

from data_test import tenant_data, agent_data, state_data

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

DATABASE_URL = f"mysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
database = Database(DATABASE_URL)

@app.get("/data", response_model=List[GroupingData.GroupingData])
async def get_data(grouping_type: str = Query(..., enum=["tenant", "agent", "state"], description="Tipo de agrupación")):
    if grouping_type == "tenant":
        return tenant_data
    elif grouping_type == "agent":
        return agent_data
    elif grouping_type == "state":
        return state_data
    else:
        return []
