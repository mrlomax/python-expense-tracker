def add_expense(expenses: list[dict], amount: float, category: str) -> None:
    """Adds an expense to a list of expenses"""
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses: list[dict]) -> None:
    """Prints expenses list"""
    for expense in expenses:
        print(f"Amount: £{expense['amount']:.2f}, Category: {expense['category']}")

def total_expenses(expenses: list[dict]) -> float:
    """Sums total of expenses"""
    return sum(map(lambda expense: expense['amount'], expenses))

def filter_expenses_by_category(expenses: list[dict], category: str) -> list[dict]:
    """Filters a list of expenses to a specific category"""
    return list(filter(lambda expense: expense['category'] == category, expenses))

def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            try:
                amount = float(input('Enter amount: '))
                category = input('Enter category: ')
                add_expense(expenses, amount, category)
            except ValueError:
                print('Invalid amount. Please enter a number.')
        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
        elif choice == '3':
            print(f'\nTotal Expenses: £{total_expenses(expenses):.2f}')
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
        elif choice == '5':
            print('Exiting the program.')
            break
        else:
            print('Invalid choice. Please enter a number from 1 to 5.')

if __name__ == '__main__':
    main()