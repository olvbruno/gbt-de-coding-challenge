from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    department = Column(String, index=True)


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    job = Column(String, index=True)


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    datetime = Column(String, nullable=True)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=True)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=True)

    department = relationship("Department", back_populates="employees")
    job = relationship("Job", back_populates="employees")
    

Department.employees = relationship("Employee", back_populates="department")
Job.employees = relationship("Employee", back_populates="job")
