import sqlite3


class BankingSystem:

    def __init__(self):
        self.conn = sqlite3.connect("bankingSystem.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS accounts (account_number INTEGER PRIMARY "
                            "KEY, account_holder_name TEXT, address TEXT, balance REAL)")
        self.conn.commit()

        self.chair_man = "Niaz"
        self.password = "this is pass"

    def create_account(self):
        number = int(input("what will be your account number(0, 999).\n->".title()))
        name = input("what is your good name?\n->".title())
        address = input("your address?\n->".title())
        balance = float(input("your initial balance? eg 12.8$ \n->".title()))

        self.cursor.execute("INSERT INTO accounts  (account_number, account_holder_name,"
                            " address, balance) VALUES (?, ?, ?, ?)", (number, name, address,
                                                                       balance))
        self.conn.commit()
        print(f"{name}! your account is created.".title())

    def deposit_money(self):
        num = int(input("enter your account number(0, 999).\n->".title()))
        amount = float(input("enter the amount.\n->".title()))

        self.cursor.execute('SELECT balance FROM accounts WHERE account_number = ?', (num, ))

        current_balance = self.cursor.fetchall()[0][0]
        new_balance = current_balance + amount

        self.cursor.execute('UPDATE accounts SET balance = ? WHERE account_number = ?',
                            (new_balance, num))
        self.conn.commit()
        print(f"Deposited successfully. Your new balance: {new_balance}$")

    def withdraw_money(self):
        num = int(input("enter your account number(0, 999).\n->".title()))
        amount = float(input("enter the amount.\n->".title()))

        self.cursor.execute('SELECT balance FROM accounts WHERE account_number = ?',
                            (num,))

        current_balance = self.cursor.fetchall()[0][0]

        if current_balance >= amount:

            new_balance = current_balance - amount

            self.cursor.execute('UPDATE accounts SET balance = ? WHERE account_number = ?',
                                (new_balance, num))

            self.conn.commit()
            print("withdrawal successful.".title())

        else:
            print(round(current_balance, 3))
            print("insufficient funds.".title())

    def check_balance(self):

        num = int(input("enter your account number(0, 999).\n->".title()))

        self.cursor.execute('SELECT balance FROM accounts WHERE account_number = ?', (num,))
        current_balance = self.cursor.fetchall()[0][0]
        self.conn.commit()

        print(f"your balance is {current_balance}$.".title())

    def show_all_accounts(self):

        name = input("enter your good name.\n->".title())
        password = input("enter your password.\n->".title())

        if name == self.chair_man and password == self.password:

            self.cursor.execute('SELECT * FROM accounts')
            all_acc = self.cursor.fetchall()
            self.conn.commit()

            print("|acc_num|\t\t|name|\t\t|address|\t\t|money|")

            for i in all_acc:
                # print(all_acc[:][i][i])
                print(f"  {i[0]}        {i[1]}\t\t {i[2]}\t\t {i[3]}")
        else:
            print("if you are not the chair man. you can't see the accounts.".title())


if __name__ == "__main__":
    obj = BankingSystem()
    obj.show_all_accounts()
