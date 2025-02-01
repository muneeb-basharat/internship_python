import json
import os
from datetime import datetime

class ExpenseTracker:
    def __init__(self):  # Change here
        self.expenses = []
        self.load_expenses()

    def add_expense(self, amount, category, description):
        """Add a new expense to the tracker."""
        expense = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "amount": amount,
            "category": category,
            "description": description
        }
        self.expenses.append(expense)
        print("Expense added successfully!")
        self.save_expenses()

    def view_expenses(self):
        """Display all expenses."""
        if not self.expenses:
            print("No expenses found.")
            return
        print("\nExpense History:")
        for expense in self.expenses:
            print(f"Date: {expense['date']}, Amount: ${expense['amount']:.2f}, "
                  f"Category: {expense['category']}, Description: {expense['description']}")

    def total_expenses(self):
        """Calculate and display the total amount of expenses."""
        total = sum(expense['amount'] for expense in self.expenses)
        print(f"\nTotal Expenses: ${total:.2f}")

    def save_expenses(self):
        """Save expenses to a file."""
        with open("expenses.json", "w") as file:
            json.dump(self.expenses, file, indent=4)

    def load_expenses(self):
        """Load expenses from a file."""
        if os.path.exists("expenses.json"):
            with open("expenses.json", "r") as file:
                self.expenses = json.load(file)

def display_menu():
    """Display the main menu."""
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

def main():
    tracker = ExpenseTracker()
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                amount = float(input("Enter the amount: "))
                category = input("Enter the category: ")
                description = input("Enter a description: ")
                tracker.add_expense(amount, category, description)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.total_expenses()
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
