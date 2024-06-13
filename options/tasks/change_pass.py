from options.tasks.account_action import AccountAction
from options.tasks.password import PasswordManager

# ChangePassword is a child class that inherits from the parent class AccountAction.
class ChangePassword(AccountAction):
    def __init__(self, account_no, new_password):
        # Initializing the parent class with account number.
        super().__init__(account_no)
        self.new_password = new_password

    def execute(self):
        # Using PasswordManager to change the password.
        PasswordManager(self.account_no).change_password(self.new_password)
