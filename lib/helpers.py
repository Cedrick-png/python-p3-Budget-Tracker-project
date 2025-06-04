from models import Category, Transaction, Budget, Session, init_db
from models import session_scope  # Import from models.py
import re

def validate_month(month):
    """Validate month format (YYYY-MM)."""
    if not re.match(r"^\d{4}-\d{2}$", month):
        raise ValueError("Month must be in YYYY-MM format")
    year, month_num = map(int, month.split("-"))
    if not (1 <= month_num <= 12):
        raise ValueError("Month must be between 01 and 12")

def add_category(name):
    """Add a new category to the database."""
    init_db()  # Ensure database is initialized
    with session_scope() as session:
        if session.query(Category).filter_by(name=name).first():
            print(f"Category '{name}' already exists")
            return
        category = Category(name=name)
        session.add(category)
        print(f"Added category: {name}")

def add_transaction(amount, category_name, type_, description):
    """Add a new transaction to the database."""
    if amount <= 0:
        print("Amount must be positive")
        return
    if type_ not in ["income", "expense"]:
        print("Type must be 'income' or 'expense'")
        return
    with session_scope() as session:
        category = session.query(Category).filter_by(name=category_name).first()
        if not category:
            print(f"Category '{category_name}' not found")
            return
        transaction = Transaction(
            amount=amount,
            description=description,
            type=type_,
            category_id=category.id
        )
        session.add(transaction)
        print(f"Added {type_} transaction: {amount} in {category_name}")

def set_budget(category_name, amount, month):
    """Set a monthly budget for a category."""
    if amount <= 0:
        print("Budget amount must be positive")
        return
    try:
        validate_month(month)
    except ValueError as e:
        print(f"Invalid month: {e}")
        return
    with session_scope() as session:
        category = session.query(Category).filter_by(name=category_name).first()
        if not category:
            print(f"Category '{category_name}' not found")
            return
        budget = Budget(category_id=category.id, amount=amount, month=month)
        session.add(budget)
        print(f"Set budget for {category_name} in {month}: {amount}")

def view_summary(month):
    """Display budget summary and recent transactions for a month."""
    try:
        validate_month(month)
    except ValueError as e:
        print(f"Invalid month: {e}")
        return
    with session_scope() as session:
        # Dictionary for summary: {category: (budget, spent)}
        summary = {}
        # List of tuples for transactions: (id, category, amount, type, description)
        transactions = []

        categories = session.query(Category).all()
        for category in categories:
            budget = session.query(Budget).filter_by(category_id=category.id, month=month).first()
            budget_amount = budget.amount if budget else 0.0
            spent = sum(
                t.amount for t in session.query(Transaction)
                .filter_by(category_id=category.id, type="expense")
                .filter(Transaction.date.like(f"{month}%"))
                .all()
            )
            summary[category.name] = (budget_amount, spent)

        trans_query = session.query(Transaction).filter(Transaction.date.like(f"{month}%")).all()
        transactions = [
            (t.id, t.category.name, t.amount, t.type, t.description or "No description")
            for t in trans_query
        ]

        print(f"\nBudget Summary for {month}:")
        for category, (budget, spent) in summary.items():
            status = "Over" if spent > budget else "Under"
            print(f"{category}: Spent {spent:.2f}/{budget:.2f} ({status})")

        print("\nRecent Transactions (Last 5):")
        for trans in transactions[-5:]:
            print(f"ID: {trans[0]} | {trans[3]} | {trans[1]}: {trans[2]:.2f} ({trans[4]})")
        return summary, transactions  # Return for potential export

def exit_program():
    """Exit the program cleanly."""
    print("Goodbye!")
    exit()