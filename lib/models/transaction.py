from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from . import Base
from datetime import datetime

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    description = Column(String)
    type = Column(String, nullable=False)  # 'income' or 'expense'
    category_id = Column(Integer, ForeignKey("categories.id"))
    date = Column(DateTime, default=datetime.utcnow)
    category = relationship("Category", back_populates="transactions")