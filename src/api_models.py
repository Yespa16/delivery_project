from datetime import date
from pydantic import BaseModel
from models import *

class CompanyBase(BaseModel):
  name:         str
  workers_cnt:  int
  area:         str


class ProductBase(BaseModel):
  name: str
  expr_date: date
  cost: float
  unit: ProductUnit


class DeliveryBase(BaseModel):
  price: float
  date: date
  volume: float
  company_id: int
  product_id: int