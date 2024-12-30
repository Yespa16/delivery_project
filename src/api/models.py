from sqlalchemy import Column, Date, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
import enum
# from psql import Base, db, session


Base = declarative_base()

class ProductUnit(enum.Enum):
  meter = "meter"
  kg = "kg"
  liter = "liter"


class Company(Base):
  __tablename__ = "company"
  id            = Column(Integer, primary_key=True, autoincrement=True)
  name          = Column(String(75), nullable=False, unique=True)
  workers_cnt   = Column(Integer)
  area          = Column(String(30))


class Product(Base):
  __tablename__ = "product"
  id            = Column(Integer, primary_key=True, autoincrement=True)
  name          = Column(String(50), nullable=False)
  expr_date     = Column(Date)
  cost          = Column(Float)
  unit          = Column(Enum(ProductUnit))


class Delivery(Base):
  __tablename__ = "delivery"
  id            = Column(Integer, primary_key=True, autoincrement=True)
  price         = Column(Float)
  date          = Column(Date)
  volume        = Column(Float)
  company_id    = Column(Integer, ForeignKey('company.id', onupdate='CASCADE', ondelete='CASCADE'))
  company       = relationship("Company", backref="company")
  product_id    = Column(Integer, ForeignKey('product.id', onupdate='CASCADE', ondelete='CASCADE'))
  product       = relationship("Product", backref="product")

