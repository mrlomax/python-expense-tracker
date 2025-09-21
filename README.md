# Python Expense Tracker CLI

This is a simple command-line interface (CLI) application I wrote in Python to track expenses. It allows a user to add, list, total, and filter expenses through an interactive menu. The project was an exercise to explore and implement lambda functions for data manipulation.



## What I Learned

This project gave me hands-on experience with core Python data structures and functional programming concepts:

- **Data Structures:** Using a **list** as a container to hold all the expenses, where each individual expense is represented as a **dictionary** with clear key-value pairs (`'amount'`, `'category'`).
- **Lambda Functions:** Exploring the power of lambdas for efficient, streamlined operations on that data, specifically:
  - Using `map()` with `lambda` to extract specific data from each dictionary for summation.
  - Using `filter()` with `lambda` to create a new, filtered collection based on a specific category.

## Features

- Add new expenses with an amount and category.
- List all recorded expenses in a formatted way.
- Calculate and display the total of all expenses.
- Filter expenses by a specific category.
- Robust input handling to prevent crashes from non-numeric input.
- Interactive and user-friendly command-line menu.

## Requirements

This script uses only Python's standard library, so no external packages are needed. All you need is **Python 3.x** installed.

## Usage

To run the script, save the code as `expense_tracker.py` and execute it from your terminal:

```sh
python expense_tracker.py
```

This will launch the interactive menu where you can manage your expenses.

**Example Session:**
```
Expense Tracker
1. Add an expense
2. List all expenses
3. Show total expenses
4. Filter expenses by category
5. Exit
Enter your choice: 1
Enter amount: 12.50
Enter category: Food

Expense Tracker
...
Enter your choice: 2

All Expenses:
Amount: £12.50, Category: Food
```

## Code Overview

- **`add_expense`, `print_expenses`, `total_expenses`, `filter_expenses_by_category`**: A set of functions that handle the core expense operations (adding, displaying, summing, and filtering).
- **`main`**: The main application loop that displays the menu, gathers user input, and calls the appropriate functions.

## Technologies Used

- **Language:** Python 3
- **Key Concepts:** Lambda Functions, Higher-Order Functions (`map`, `filter`), Lists, Dictionaries
