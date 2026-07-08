from fastapi import FastAPI
from app.parser import router

app = FastAPI(title="FNOL AI Agent")

app.include_router(router)