import sqlite3
from source.accounts.actions import AccountAction

class PasswordManager:
    def __init__(self, account_no): # initialize with the given account number 
        self.account_no = account_no

    def validate_password(self, password):
        conn = sqlite3.connect('banking_management.db')
        cursor = conn.cursor()
        cursor.execute('SELECT password FROM accounts WHERE account_no = ?', (self.account_no,))
        stored_password = cursor.fetchone()
        conn.close()
        if stored_password and stored_password[0] == password:
            return True
        return False

    def change_password(self, new_password):
        conn = sqlite3.connect('banking_management.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE accounts SET password = ? WHERE account_no = ?', (new_password, self.account_no))
        conn.commit()
        conn.close()
        print("Password changed successfully.")


# child class: ChangePassword inherits from the parent class: AccountAction
class ChangePassword(AccountAction):
    def __init__(self, account_no, new_password):
        # initializing the parent class with account number
        super().__init__(account_no)
        self.new_password = new_password

    def execute(self):
        # using PasswordManager to change the password
        PasswordManager(self.account_no).change_password(self.new_password)
