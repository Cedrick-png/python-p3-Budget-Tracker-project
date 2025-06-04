from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    transactions = relationship("Transaction", back_populates="category")
    budgets = relationship("Budget", back_populates="category")