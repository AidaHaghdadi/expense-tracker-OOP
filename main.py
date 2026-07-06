
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
            return None
        
        print("\nExpenses list:")
        for index, expense in enumerate(self.expenses): # `expense` is an instance of `Expense`.
            print(f"{index + 1}- Title: {expense.title} | Amount: {expense.amount} | Date: {expense.date}")

    # Search expense function
    def search_expense(self, search_title):
        results = []
        for expense in self.expenses:
            if search_title == expense.title:
                results.append(expense)
        return results

    # Calculate total function
    def calculate_total(self):
        total_amount = 0
        for expense in self.expenses :
            total_amount += expense.amount
        return total_amount

    # Calculate average function
    def calculate_average(self):
        if not self.expenses :
            return None

        total_amount = self.calculate_total()
        average_amount = total_amount / len(self.expenses)
        return average_amount
