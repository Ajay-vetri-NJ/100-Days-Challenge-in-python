def expense_splitter():
    print("Welcome to the Personal Expense Splitter!")
    
    try:
        num_people = int(input("Enter the number of people sharing expenses: "))
        if num_people < 2:
            print("At least two people are needed to split expenses.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    names = []
    for i in range(num_people):
        name = input(f"Enter the name of person {i + 1}: ")
        names.append(name)
    
    expenses = {}
    for name in names:
        try:
            expense = float(input(f"Enter the total amount paid by {name}: "))
            expenses[name] = expense
        except ValueError:
            print("Please enter a valid number for expenses.")
            return
    
    total_expenses = sum(expenses.values())
    per_person_share = total_expenses / num_people
    
    balances = {name: expense - per_person_share for name, expense in expenses.items()}
    
    print("\n--- Expense Summary ---")
    print(f"Total Expenses: {total_expenses:.2f}")
    print(f"Per Person Share: {per_person_share:.2f}")
    
    for name, balance in balances.items():
        if balance > 0:
            print(f"{name} overpaid by {balance:.2f}")
        elif balance < 0:
            print(f"{name} owes {-balance:.2f}")
        else:
            print(f"{name} is settled up.")
    
    print("\n--- Settlement Steps ---")
    debtors = {name: -balance for name, balance in balances.items() if balance < 0}
    creditors = {name: balance for name, balance in balances.items() if balance > 0}

    while debtors and creditors:
        debtor, debtor_amount = next(iter(debtors.items()))
        creditor, creditor_amount = next(iter(creditors.items()))
        
        settlement = min(debtor_amount, creditor_amount)
        print(f"{debtor} pays {creditor} {settlement:.2f}")
        
        debtors[debtor] -= settlement
        creditors[creditor] -= settlement

        if debtors[debtor] == 0:
            del debtors[debtor]
        if creditors[creditor] == 0:
            del creditors[creditor]

expense_splitter()
