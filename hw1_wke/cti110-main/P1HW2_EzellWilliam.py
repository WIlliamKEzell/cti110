# William Ezell
# 2025-09-20
# Assignment: P1HW2 - Trip Budget Calculator
# A brief description of the project: Prompt user for trip budget, destination, and expenses (gas, accommodation, food). Calculate total expenses and remaining budget and display results.

"""
Pseudocode:
1. Prompt user to enter their budget (float)
2. Prompt user to enter travel destination (string)
3. Prompt user to enter gas expense (float)
4. Prompt user to enter accommodation expense (float)
5. Prompt user to enter food expense (float)
6. Calculate total_expenses = gas + accommodation + food
7. Calculate remaining = budget - total_expenses
8. Print destination, budget, each expense, total expenses, and remaining balance (formatted to 2 decimal places)
"""

# 3. Ask user to enter their budget
budget = float(input("Enter your budget: "))

# 4. Ask user to enter travel destination
destination = input("Enter your travel destination: ")

# 5. Ask user for amount they will spend on gas
gas = float(input("Enter amount you will spend on gas: "))

# 6. Ask user for amount they will spend on accommodation
accommodation = float(input("Enter amount you will spend on accommodation: "))

# 7. Ask user for amount they will spend on food
food = float(input("Enter amount you will spend on food: "))

# 8. Add expenses
total_expenses = gas + accommodation + food

# 9. Subtract expenses from budget
remaining = budget - total_expenses

# 10. Display results
print()
print(f"Destination: {destination}")
print(f"Budget: ${budget:.2f}")
print("Expenses:")
print(f"  Gas: ${gas:.2f}")
print(f"  Accommodation: ${accommodation:.2f}")
print(f"  Food: ${food:.2f}")
print(f"Total expenses: ${total_expenses:.2f}")
print(f"Remaining balance: ${remaining:.2f}")
