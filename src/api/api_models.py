from datetime import date
from pydantic import BaseModel
from models import *
from typing import Dict, Any

class CompanyBase(BaseModel):
  name:         str
  workers_cnt:  int
  area:         str


class ProductBase(BaseModel):
  name: str
  expr_date: date
  cost: float
  unit: ProductUnit
  description: Dict[str, Any]

class DeliveryBase(BaseModel):
  price: float
  date: date
  volume: float
  company_id: int
  product_id: int