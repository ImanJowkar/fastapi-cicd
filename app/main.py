from fastapi import FastAPI
from pymongo import MongoClient
from routes import router as book_router
import os


db_url = os.environ["db_url"]
db_name = os.environ["db_name"]

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(db_url)
    app.database = app.mongodb_client[db_name]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(book_router, tags=["books"], prefix="/book")

