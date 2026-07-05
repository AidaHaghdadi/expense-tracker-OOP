
class Expense: # Responsible for maintaining information about an expense.
    def __init__ (self, title, amount, date):
        self.title = title
        self.amount = amount
        self.date = date

class ExpenseTracker: # Responsible for managing collections of expenses.
    def __init__ (self):
        self.expenses = []

    # Add expense function
    def add_expense(self, expense):
        self.expenses.append(expense)

    # Show expenses function
    def show_expenses(self):
        if not self.expenses:
            print("No expense found!")
        else :
            print("\nExpenses list:")
            for index, expense in enumerate(self.expenses): # `expense` is an instance of `Expense`.
                print(f"{index + 1}- Title: {expense.title} | Amount: {expense.amount} | Date: {expense.date}")