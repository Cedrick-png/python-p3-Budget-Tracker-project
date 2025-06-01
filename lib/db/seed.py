from models import Category, Transaction, Budget, Session, init_db
from datetime import datetime

def seed_database():
    """Seed the database with sample data."""
    init_db()  # Ensure database is initialized
    with session_scope() as session:
        # Clear existing data
        session.query(Transaction).delete()
        session.query(Budget).delete()
        session.query(Category).delete()

        # Sample data using lists and dictionaries
        categories = [
            {"name": "Food"},
            {"name": "Salary"},
            {"name": "Utilities"}
        ]
        budgets = {
            "Food": {"amount": 500.0, "month": "2025-06"},
            "Utilities": {"amount": 200.0, "month": "2025-06"}
        }
        transactions = [
            {"amount": 50.0, "category": "Food", "type": "expense", "description": "Groceries", "date": datetime(2025, 6, 1)},
            {"amount": 2000.0, "category": "Salary", "type": "income", "description": "Monthly salary", "date": datetime(2025, 6, 1)},
            {"amount": 100.0, "category": "Utilities", "type": "expense", "description": "Electricity bill", "date": datetime(2025, 6, 2)}
        ]

        # Add categories
        for cat in categories:  # Using list
            category = Category(name=cat["name"])
            session.add(category)
        session.commit()

        # Add budgets
        for cat_name, budget_data in budgets.items():  # Using dictionary
            category = session.query(Category).filter_by(name=cat_name).first()
            if category:
                budget = Budget(category_id=category.id, amount=budget_data["amount"], month=budget_data["month"])
                session.add(budget)
        session.commit()

        # Add transactions
        for trans in transactions:  # Using list of dictionaries
            category = session.query(Category).filter_by(name=trans["category"]).first()
            if category:
                transaction = Transaction(
                    amount=trans["amount"],
                    description=trans["description"],
                    type=trans["type"],
                    category_id=category.id,
                    date=trans["date"]
                )
                session.add(transaction)
        session.commit()

        # Verify seeded data using tuple
        category_count = session.query(Category).count()
        transaction_count = session.query(Transaction).count()
        budget_count = session.query(Budget).count()
        print(f"Seeded database with {category_count} categories, {transaction_count} transactions, and {budget_count} budgets.")

# Context manager from helpers.py (included for completeness)
from contextlib import contextmanager

@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

if __name__ == "__main__":
    seed_database()