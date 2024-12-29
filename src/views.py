from typing import Annotated
from models import Base, Company, Product, Delivery
from api_models import CompanyBase, ProductBase, DeliveryBase
from connect_db import engine, get_db, init_db
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException



app = FastAPI()
db_dependency = Annotated[Session, Depends(get_db)]


@app.on_event("startup")
def startup_event():
  init_db()
  Base.metadata.create_all(engine)


@app.get("/")
def read_root():
  return {"Hello": "World"}


# ============= Company Table Views ============= #

@app.post("/company/")
def create_company(company: CompanyBase, db: db_dependency):
  db_company = Company(name=company.name, workers_cnt=company.workers_cnt, area=company.area)
  db.add(db_company)
  db.commit()
  db.refresh(db_company)


@app.get("/company/{company_id}")
def get_company_by_id(company_id: int, db:db_dependency):
  company = db.get(Company, company_id)
  if not company:
    raise HTTPException(status_code=404, detail=f"Company with id {company_id} not found")
  return company

@app.get("/company/")
def get_company_by_name(company_name: str, db: db_dependency):
  company = db.query(Company).filter(Company.name == company_name).first()
  if not company:
    raise HTTPException(status_code=404, detail=f"Company {company_name} not found")
  return company


@app.put("/company/{company_id}", response_model=CompanyBase)
def update_company_by_id(company_id: int, company: CompanyBase, db: db_dependency):
  db_company = db.get(Company, company_id)
  if not db_company:
    raise HTTPException(status_code=404, detail=f"Company with id {company_id} not found")
  db_company.name = company.name
  db_company.workers_cnt = company.workers_cnt
  db_company.area = company.area
  db.commit()
  return db_company

# ============= Product Table Views ============= #















# ============= Delivery Table Views ============= #