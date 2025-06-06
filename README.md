<<<<<<< HEAD
# python-p3-Budget-Tracker-project
Budget Tracker
Overview
Budget Tracker is a simple Python application designed to help users manage their personal finances by tracking income, expenses, and overall budget. It provides a command-line interface to add transactions, view summaries, and generate basic reports.
Features

Add Transactions: Record income and expenses with categories and dates.
View Balance: Check the current balance based on all transactions.
Category Summaries: View spending and income by category.
Transaction History: Display a log of all recorded transactions.
Data Persistence: Save transactions to a JSON file for persistent storage.
Simple CLI: User-friendly command-line interface for easy interaction.

Requirements

Python 3.6 or higher
No external libraries required (uses standard Python libraries like json and datetime)

Installation

Clone the Repository:git clone https://github.com/yourusername/budget-tracker.git
cd budget-tracker


Ensure Python 3.6+ is installed:python --version


Run the application:python budget_tracker.py



Usage

Launch the program by running:python budget_tracker.py


Follow the on-screen menu to:
Add income or expense transactions.
View the current balance.
Display transaction history or category summaries.
Save and exit the program.


Example commands:
Add income: Enter amount: 1000, Category: Salary, Date: 2025-06-01
Add expense: Enter amount: -200, Category: Groceries, Date: 2025-06-02
View balance: Select the "Show Balance" option from the menu.



Project Structure

budget_tracker.py: Main script containing the application logic.
transactions.json: File where transaction data is stored (created automatically).
README.md: This file, providing project documentation.

Example
=== Budget Tracker ===
1. Add Income/Expense
2. Show Balance
3. Show Transaction History
4. Show Category Summary
5. Exit
Enter choice: 1
Amount: 500
Category: Freelance
Date (YYYY-MM-DD): 2025-06-06
Transaction added!

Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit (git commit -m 'Add new feature').
Push to the branch (git push origin feature-branch).
Open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Contact
For questions or feedback, please contact your.email@example.com or open an issue on the GitHub repository.
