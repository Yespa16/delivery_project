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

# TODO: Error if company exists
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


@app.delete("/company/{company_id}", response_model=dict)
def delete_item(company_id: int, db: db_dependency):
    item = db.query(Company).filter(Company.id == company_id).first()
    if not item:
        raise HTTPException(status_code=404, detail=f"Company with id {company_id} not found")
    
    db.delete(item)
    db.commit()
    return {"message": "Company deleted successfully"}

# ============= Product Table Views ============= #

@app.post("/product/", response_model=dict)
def create_product(product: ProductBase, db: db_dependency):
  db_product = Product(name=product.name, expr_date=product.expr_date, cost=product.cost, unit=product.unit)
  db.add(db_product)
  db.commit()
  db.refresh(db_product)
  return {"message": "Product created successfully"}


@app.get("/product/{product_id}")
def get_product_by_id(product_id: int, db:db_dependency):
  product = db.get(Product, product_id)
  if not product:
    raise HTTPException(status_code=404, detail=f"Product with id {product_id} not found")
  return product


@app.get("/product/")
def get_products_by_name(product_name: str, db: db_dependency):
  product = db.query(Product).filter(Product.name == product_name).all()
  if not product:
    raise HTTPException(status_code=404, detail=f"Products named {product_name} not found")
  return product


@app.put("/product/{product_id}", response_model=ProductBase)
def update_product_by_id(product_id: int, product: ProductBase, db: db_dependency):
  db_product = db.get(Product, product_id)
  if not db_product:
    raise HTTPException(status_code=404, detail=f"Product with id {product_id} not found")
  db_product.name = product.name
  db_product.expr_date = product.expr_date
  db_product.cost = product.cost
  db_product.unit = product.unit
  db.commit()
  return db_product


@app.delete("/product/{product_id}", response_model=dict)
def delete_product(product_id: int, db: db_dependency):
    item = db.query(Product).filter(Product.id == product_id).first()
    if not item:
        raise HTTPException(status_code=404, detail=f"Product with id {product_id} not found")
    
    db.delete(item)
    db.commit()
    return {"message": "Product deleted successfully"}

# ============= Delivery Table Views ============= #



@app.post("/delivery/", response_model=dict)
def create_delivery(delivery: DeliveryBase, db: db_dependency):
  if not db.get(Company, delivery.company_id):
    raise HTTPException(status_code=404, detail=f"Company with id {delivery.company_id} not found")
  if not db.get(Product, delivery.product_id):
    raise HTTPException(status_code=404, detail=f"Product with id {delivery.product_id} not found")
  
  db_delivery = Delivery(price=delivery.price, date=delivery.date, volume=delivery.volume, company_id=delivery.company_id, product_id=delivery.product_id)
  db.add(db_delivery)
  db.commit()
  db.refresh(db_delivery)
  return {"message": "Delivery created successfully"}


@app.get("/delivery/{delivery_id}")
def get_delivery_by_id(delivery_id: int, db:db_dependency):
  delivery = db.get(Delivery, delivery_id)
  if not delivery:
    raise HTTPException(status_code=404, detail=f"Delivery with id {delivery_id} not found")
  return delivery


@app.get("/delivery/")
def get_deliveries_by_company(company_name: str, db: db_dependency):
  company = db.query(Company).filter(Company.name == company_name).first()
  if not company:
    raise HTTPException(status_code=404, detail=f"Company {company_name} not found")
  company_id = company.id
  deliveries = db.query(Delivery).filter(Delivery.company_id == company_id).all()
  if not deliveries:
    raise HTTPException(status_code=404, detail=f"Deliveries for {company_name} not found")
  return deliveries


