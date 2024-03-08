from api.schemas import EmployeeCreate, DepartmentCreate, JobCreate
from database.models import Employee, Department, Job
from sqlalchemy.orm import Session


def create_employee(db: Session, employee: EmployeeCreate):
    db_employee = Employee(**employee.model_dump())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def create_department(db: Session, department: DepartmentCreate):
    db_department = Department(**department.model_dump())
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department


def create_job(db: Session, job: JobCreate):
    db_job = Job(**job.model_dump())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job
