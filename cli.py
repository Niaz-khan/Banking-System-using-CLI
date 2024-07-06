import cmd
import sqlite3


class BankingSystemCli(cmd.Cmd):
    prompt = "Bank System->"
    intro = """welcome to the banking system Command Line interface\nwhere you can create account, deposit money, withdraw money and alot. \njust write help to learn the app.\n""".title()

    def __init__(self, banking_system):
        super().__init__()
        self.banking_system = banking_system
        self.conn = sqlite3.connect("bankingSystem.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS accounts (account_number INTEGER PRIMARY "
                            "KEY, account_holder_name TEXT, address TEXT, balance REAL)")
        self.conn.commit()
        self.chair_man = "Niaz"
        self.password = "this is pass"

    def do_show_accounts(self, line):
        """
        show all accounts
        :param line:
        :return:
        """
        self.banking_system.show_all_accounts(self)

    def do_create_account(self, line):
        """
        create a new account
        :param line:
        :return:
        """
        self.banking_system.create_account(self)

    def do_deposit_money(self, line):
        """
        deposit funds into an account
        """
        self.banking_system.deposit_money(self)

    def do_withdraw_money(self, line):
        """
        withdraw money
        :param line:
        :return:
        """
        self.banking_system.withdraw_money(self)

    def do_check_balance(self, line):
        """
        check balance
        """
        self.banking_system.check_balance(self)

    def do_exit(self, line):
        """
        Exit the CLI
        """
        return True
