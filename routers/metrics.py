from fastapi import APIRouter
from database.database import SessionLocal
from sqlalchemy import text


router = APIRouter()


@router.get("/metrics/quarterly_hiring/", response_model=list)
async def get_quarterly_hiring():
    db = SessionLocal()
    try:
        query = text(open("sql/quarterly_hiring.sql").read())
        result = db.execute(query)
        quarterly_hiring = [dict(zip(result.keys(), row)) for row in result.fetchall()]
        
        return quarterly_hiring
    
    finally:
        db.close()


@router.get("/metrics/top_departments/", response_model=list)
async def get_top_departments():
    db = SessionLocal()
    try:
        query = text(open("sql/top_departments.sql").read())
        result = db.execute(query)
        top_departments = [dict(zip(result.keys(), row)) for row in result.fetchall()]

        return top_departments
    
    finally:
        db.close()
