from options.tasks.account_action import AccountAction
import sqlite3

# ShowAccountDetails is a child class that inherits from the parent class AccountAction.
class ShowAccountDetails(AccountAction):
    def execute(self):
        # Specific implementation for showing account details.
        account = self.get_account()
        if account:
            print(f"Holder Name: {account[3]}, Account No: {account[0]}, Password: {account[1]}, Balance: {account[2]}")
        else:
            print("Account not found.")
