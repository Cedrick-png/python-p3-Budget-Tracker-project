from .helpers import (
    add_category,
    add_transaction,
    set_budget,
    view_summary,
    exit_program
)
from .debug import list_all_categories, list_transactions_by_category, budget_stats

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            name = input("Enter category name: ")
            add_category(name)
        elif choice == "2":
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category name: ")
                type_ = input("Enter type (income/expense): ")
                description = input("Enter description (optional): ")
                add_transaction(amount, category, type_, description)
            except ValueError:
                print("Invalid amount: Please enter a number")
        elif choice == "3":
            try:
                category = input("Enter category name: ")
                amount = float(input("Enter budget amount: "))
                month = input("Enter month (YYYY-MM): ")
                set_budget(category, amount, month)
            except ValueError:
                print("Invalid amount: Please enter a number")
        elif choice == "4":
            month = input("Enter month (YYYY-MM): ")
            view_summary(month)
        elif choice == "5":
            debug_menu()
        else:
            print("Invalid choice")

def menu():
    print("\nBudget Tracker CLI")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add a category")
    print("2. Add a transaction")
    print("3. Set a monthly budget")
    print("4. View budget summary")
    print("5. Debug tools")

def debug_menu():
    """Debugging menu for database inspection."""
    while True:
        print("\nDebug Tools")
        print("0. Back to main menu")
        print("1. List all categories")
        print("2. List transactions by category")
        print("3. View budget stats")
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            list_all_categories()
        elif choice == "2":
            category = input("Enter category name: ")
            list_transactions_by_category(category)
        elif choice == "3":
            month = input("Enter month (YYYY-MM): ")
            budget_stats(month)
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()