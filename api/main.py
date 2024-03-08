from fastapi import FastAPI
from routers import upload, metrics


app = FastAPI()


@app.get("/", tags=["Root"])
async def welcome():
    return {"message": "Welcome to Globant's Data Engineering Coding Challenge!"}


app.include_router(upload.router)
app.include_router(metrics.router)
