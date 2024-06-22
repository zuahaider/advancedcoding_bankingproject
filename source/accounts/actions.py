import sqlite3

class AccountAction: # this is the parent class (or base class) for all account-related actions
    def __init__(self, account_no):
        self.account_no = account_no

    def execute(self):
        # method should be implemented by all subclasses
        raise NotImplementedError("Subclasses should implement this method")

    def get_account(self):
        # to fetch account details from the database
        conn = sqlite3.connect('banking_management.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM accounts WHERE account_no = ?', (self.account_no,))
        account = cursor.fetchone() # retrieve one row
        conn.close()
        return account
 
    
# childclass: ShowAccountDetails inherits from the parent class: AccountAction
class ShowAccountDetails(AccountAction):
    def execute(self):
        # specific implementation for showing account details.
        account = self.get_account()
        if account:
            print(f"Holder Name: {account[3]}, Account No: {account[0]}, Password: {account[1]}, Balance: {account[2]}") # using f string to format the string
        else:
            print("Account not found.")


# child class: Deposit inherits from the parent class: AccountAction
class Deposit(AccountAction):
    def __init__(self, account_no, amount):
        # initializing the parent class with account number
        super().__init__(account_no)
        self.amount = amount

    def execute(self):
        # specific implementations for depositing money
        conn = sqlite3.connect('banking_management.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE accounts SET balance = balance + ? WHERE account_no = ?', (self.amount, self.account_no))
        conn.commit()
        
        # fetch the updated balance from the database
        cursor.execute('SELECT balance FROM accounts WHERE account_no = ?', (self.account_no,))
        updated_balance = cursor.fetchone()[0] 
        
        conn.close()
        print("Deposit successful!")
        print("Your updated account balance is:", updated_balance)  # print the updated balance


# child class: Withdraw inherits from the parent class: AccountAction
class Withdraw(AccountAction):
    def __init__(self, account_no, amount):
        # initializing the parent class with account number
        super().__init__(account_no)
        self.amount = amount

    def execute(self):
        # specific implementations for withdrawing money
        conn = sqlite3.connect('banking_management.db')
        cursor = conn.cursor()
        cursor.execute('SELECT balance FROM accounts WHERE account_no = ?', (self.account_no,))
        balance = cursor.fetchone()[0]
        
        if balance >= self.amount:
            # update the balance in the database
            new_balance = balance - self.amount
            cursor.execute('UPDATE accounts SET balance = ? WHERE account_no = ?', (new_balance, self.account_no))
            conn.commit()
            print("Withdrawal successful!")
            print("Your updated account balance is: ", new_balance)  # Print the updated balance
        else:
            print("Insufficient balance.")
        
        conn.close()

