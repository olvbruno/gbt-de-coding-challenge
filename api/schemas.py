from pydantic import BaseModel
from typing import Optional


class EmployeeBase(BaseModel):
    id: int
    name: Optional[str] = None
    datetime: Optional[str] = None
    department_id: Optional[int] = None
    job_id: Optional[int] = None


class EmployeeCreate(EmployeeBase):
    ...


class DepartmentBase(BaseModel):
    id: int
    department: str


class DepartmentCreate(DepartmentBase):
    ...


class JobBase(BaseModel):
    id: int
    job: str


class JobCreate(JobBase):
    ...
