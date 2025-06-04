from models import Category, Transaction, Budget, Session, session_scope
from helpers import validate_month

def list_all_categories():
    """Print all categories in the database."""
    with session_scope() as session:
        categories = session.query(Category).all()
        # List of tuples: (id, name)
        category_list = [(c.id, c.name) for c in categories]
        if not category_list:
            print("No categories found.")
            return
        print("\nAll Categories:")
        for cat in category_list:
            print(f"ID: {cat[0]} | Name: {cat[1]}")

def list_transactions_by_category(category_name):
    """Print all transactions for a given category."""
    with session_scope() as session:
        category = session.query(Category).filter_by(name=category_name).first()
        if not category:
            print(f"Category '{category_name}' not found.")
            return
        # List of tuples: (id, amount, type, description, date)
        transactions = [
            (t.id, t.amount, t.type, t.description or "No description", t.date)
            for t in category.transactions
        ]
        print(f"\nTransactions for Category '{category_name}':")
        if not transactions:
            print("No transactions found.")
            return
        for trans in transactions:
            print(f"ID: {trans[0]} | Amount: {trans[1]:.2f} | Type: {trans[2]} | "
                  f"Description: {trans[3]} | Date: {trans[4]}")

def budget_stats(month):
    """Print statistics for a given month's budget, including total income and expenses."""
    try:
        validate_month(month)
    except ValueError as e:
        print(f"Invalid month: {e}")
        return
    with session_scope() as session:
        # Dictionary to store stats: {total_income, total_expense, categories}
        stats = {
            "total_income": 0.0,
            "total_expense": 0.0,
            "categories": {}  # {category_name: (budget, spent)}
        }
        transactions = session.query(Transaction).filter(Transaction.date.like(f"{month}%")).all()
        for t in transactions:
            if t.type == "income":
                stats["total_income"] += t.amount
            elif t.type == "expense":
                stats["total_expense"] += t.amount

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
            stats["categories"][category.name] = (budget_amount, spent)

        print(f"\nBudget Stats for {month}:")
        print(f"Total Income: {stats['total_income']:.2f}")
        print(f"Total Expense: {stats['total_expense']:.2f}")
        print(f"Net Balance: {(stats['total_income'] - stats['total_expense']):.2f}")
        print("\nCategory Breakdown:")
        for cat, (budget, spent) in stats["categories"].items():
            print(f"{cat}: Budget={budget:.2f}, Spent={spent:.2f}")