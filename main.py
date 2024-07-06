from bank import BankingSystem
from cli import BankingSystemCli

if __name__ == "__main__":
    banking_system = BankingSystem
    cli = BankingSystemCli(banking_system)
    cli.cmdloop()
