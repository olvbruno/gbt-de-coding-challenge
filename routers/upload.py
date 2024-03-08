from api.schemas import  EmployeeCreate, DepartmentCreate, JobCreate
from database.database import SessionLocal
from database.models import Employee, Job, Department
from fastapi import APIRouter, File, UploadFile, HTTPException
import math


router = APIRouter()


@router.post("/upload/form/")
async def upload_file_form(file: UploadFile = File(...), batch_size: int = 1000):
    if batch_size < 1 or batch_size > 1000:
        raise HTTPException(status_code=400, detail="Batch size must be between 1 and 1000")

    db = SessionLocal()

    try:
        if file.filename == "hired_employees.csv":
            num_batches = await process_csv(db, file, EmployeeCreate, Employee, batch_size)

        elif file.filename == "jobs.csv":
            num_batches = await process_csv(db, file, JobCreate, Job, batch_size)

        elif file.filename == "departments.csv":
            num_batches = await process_csv(db, file, DepartmentCreate, Department, batch_size)

        else:
            raise HTTPException(status_code=400, detail="Invalid CSV file name")
        
    finally:
        db.close()

    return {
        "message": f"File uploaded and data migrated successfully. Number of batches used: {num_batches}"
    }


async def process_csv(db, file: UploadFile, schema_class, model_class, batch_size: int) -> int:
    data = await file.read()
    data = data.decode("utf-8").splitlines()
    data_objects = []

    field_names = [field for field in schema_class.__fields__]

    for line in data:
        values = line.split(',')
        data_dict = {field_name: value if value else None for field_name, value in zip(field_names, values)}
        data_object = schema_class(**data_dict)
        data_objects.append(data_object)

    num_batches = math.ceil(len(data_objects) / batch_size)

    try:
        for i in range(0, len(data_objects), batch_size):

            batch = data_objects[i:i+batch_size]
            for data_object in batch:
                model_instance = model_class(**data_object.dict())
                db.add(model_instance)
            db.commit()

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    
    return num_batches
