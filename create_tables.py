import sqlite3

# to create tables in the SQLite database
def create_tables():
    # connecting to SQLite database
    conn = sqlite3.connect('banking_management.db')
    cursor = conn.cursor()

    # creating 'accounts' table with columns for account number, password, and balance
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        account_no INTEGER PRIMARY KEY,
        password TEXT NOT NULL,
        balance REAL NOT NULL,
        account_holder_name TEXT NOT NULL
    )
    ''')

    # inserting user's account details
    accounts = [
        (67789876, '2362', 55000.0, 'Sarah Kim'),
        (37292011, '7362', 45670.0, 'Christine William'),
        (55483920, '8456', 3510.0, 'Edward Charles'),
        (38392021, '3282', 2000.0, 'Tom Mayor'),
        (72829022, '2729', 500.0, 'George Brown')
    ]

    cursor.executemany('''
    INSERT INTO accounts (account_no, password, balance, account_holder_name)
    VALUES (?, ?, ?, ?)
    ON CONFLICT(account_no) DO NOTHING
    ''', accounts)

    # to commit changes and close the connection
    conn.commit()
    conn.close()
    print("Tables created successfully and accounts added.")

if __name__ == "__main__":
    create_tables()
