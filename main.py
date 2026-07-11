from datetime import datetime
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
            print("No expenses found!")
            return 
        
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
        if not self.expenses:
            return None

        total_amount = 0
        for expense in self.expenses :
            total_amount += expense.amount
        return total_amount

    # Calculate average function
    def calculate_average(self):
        total_amount = self.calculate_total()
        
        if total_amount is None:
            return None

        average_amount = total_amount / len(self.expenses)
        return average_amount
    

def show_menu():
    print("\n1- Add Expense")
    print("2- Show Expenses")
    print("3- Search Expense")
    print("4- Calculate Total ")
    print("5- Calculate Average")
    print("6- Delete Expense")
    print("7- Exit")

def create_expense():
    expense_title = input("Enter the title of expense :").capitalize()
    # Value validation
    while True:
        try:
            expense_amount = float(input("Enter the amount of expense:"))
            break
        except ValueError:
            print("Invalid input!")
    # Date validation
    while True:
        try:
            expense_date = input("Enter date of expense [YYYY-MM-DD]:")
            datetime.strptime(expense_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date! Example: 2026-07-01")
            
    expense = Expense(expense_title,expense_amount,expense_date)
    return expense


tracker = ExpenseTracker()

user_selection = None
while user_selection != 7:
    show_menu()
    try:
        user_selection = int(input("Enter your selection :"))
    except ValueError:
        print("Invalid input!")
        continue

    if user_selection == 1:
        expense = create_expense()
        tracker.add_expense(expense)
        print("Expense added.")

    elif user_selection == 2:
        tracker.show_expenses()

    elif user_selection == 3:
        search_title = input("Enter the title of expense :").capitalize()
        result = tracker.search_expense(search_title)
        if not result:
            print("No expense found!")
        else:
            count = len(result)
            for index, expense_info in enumerate(result):
                print(f"{index + 1}- Title: {expense_info.title} | Amount: {expense_info.amount} | Date: {expense_info.date}")
            print(f"{count} expense(s) found.")

    elif user_selection == 4:
        total = tracker.calculate_total()
        if total is None:
            print("No expense found!")
        else :
            print(f"Total is {total}")
    
    elif user_selection == 5:
        average = tracker.calculate_average()
        if average is None:
            print("No expense found!")
        else :
            print(f"Average is : {average}")
        

    # elif user_selection == 6 :
        

    elif user_selection == 7 :
        print("Exit from program.")

    else :
        print("Invalid choice!")