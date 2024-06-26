from source.password_managing.password_actions import PasswordManager, ChangePassword
from source.accounts.actions import ShowAccountDetails, Deposit, Withdraw
import time

def authenticate(account_no, password_input):
    # Using PasswordManager to validate the password
    password_manager_instance = PasswordManager(account_no)
    return password_manager_instance.validate_password(password_input)

def main():
    while True:
        action = input("Enter desired action (C) change password, (D) deposit, (W) withdraw, (S) show acc details, (Q) quit: ").lower()
        if action not in ['c', 'd', 'w', 's', 'q']:
            print("Invalid action.")
            continue
        
        if action == 'q':
            print("Exiting the system. Goodbye!")
            break
        
        account_no = int(input("Enter account number: "))
        password_input = input("Enter password: ")
        
        if not authenticate(account_no, password_input):
            print("Invalid account or password.")
            continue
        
        if action == 'c':
            new_password = input("Enter new password: ")
            ChangePassword(account_no, new_password).execute()
        elif action == 'd':
            amount = float(input("Enter the amount you wish to deposit: "))
            Deposit(account_no, amount).execute()
        elif action == 'w':
            amount = float(input("Enter the amount you wish to withdraw: "))
            Withdraw(account_no, amount).execute()
        elif action == 's':
            # Creating an instance of ShowAccountDetails and calling its execute method
            ShowAccountDetails(account_no).execute()
        

# after entering 'Q' the program closes after 7 seconds
if __name__ == "__main__":
    main()
    time.sleep(7)