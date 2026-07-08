from fastapi import FastAPI
from app.parser import router

app = FastAPI(title="FNOL AI Agent")


# @router.get('/')
# def home():
#     return {
#         "message": "project is working..."
#     }


app.include_router(router)