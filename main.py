
class Expense : # Responsible for maintaining information about an expense.
    def __init__ (self, expense_title, expense_amount, expense_date) :
        self.title = expense_title
        self.amount = expense_amount
        self.date = expense_date

class ExpenseTracker : # Responsible for managing collections of expenses.
    def __init__ (self) :
        self.expenses = []

    # Add expense function
    def add_expense(self, expense):
        self.expenses.append(expense)

