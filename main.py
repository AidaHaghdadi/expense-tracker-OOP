
class Expense :
    def __init__ (self, expense_title, expense_amount, expense_date) :
        self.title = expense_title
        self.amount = expense_amount
        self.date = expense_date

class ExpenseTracker :
    def __init__ (self) :
        self.expenses = []
