from options.show_info.show_acc_details import ShowAccountDetails
from options.tasks import change_pass, deposit, withdraw, password
import time

def authenticate(account_no, password_input):
    # Using PasswordManager to validate the password
    password_manager = password.PasswordManager(account_no)
    return password_manager.validate_password(password_input)

def main():
    while True:
        action = input("Enter desired action (C) change password, (D) deposit, (W) withdraw, (S) show acc details, (Q) quit: ").lower()
        if action == 'q':
            break
        
        account_no = int(input("Enter account number: "))
        password_input = input("Enter password: ")
        
        if not authenticate(account_no, password_input):
            print("Invalid account or password.")
            continue
        
        if action == 'c':
            new_password = input("Enter new password: ")
            change_pass.ChangePassword(account_no, new_password).execute()
        elif action == 'd':
            amount = float(input("Enter the amount you wish to deposit: "))
            deposit.Deposit(account_no, amount).execute()
        elif action == 'w':
            amount = float(input("Enter the amount you wish to withdraw: "))
            withdraw.Withdraw(account_no, amount).execute()
        elif action == 's':
            # Creating an instance of ShowAccountDetails and calling its execute method
            ShowAccountDetails(account_no).execute()
        else:
            print("Invalid action.")

if __name__ == "__main__":
    main()
    time.sleep(7)