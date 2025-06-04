from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///budget_tracker.db", echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)

from .category import Category
from .transaction import Transaction
from .budget import Budget

def init_db():
    Base.metadata.create_all(engine)