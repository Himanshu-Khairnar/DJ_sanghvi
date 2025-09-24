class BankingError(Exception):
    """Base class for banking exceptions"""
    pass

class InsufficientFundsError(BankingError):
    def __init__(self, balance, amount):
        super().__init__(f"❌ Withdrawal failed! Balance = {balance}, Attempted = {amount}")

class NegativeAmountError(BankingError):
    def __init__(self, amount):
        super().__init__(f"❌ Invalid amount: {amount}. Amount must be positive.")

class AccountNotFoundError(BankingError):
    def __init__(self, acc_no):
        super().__init__(f"❌ Account {acc_no} not found.")


class BankAccount:
    def __init__(self, acc_no, holder, balance=0):
        self.acc_no = acc_no
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise NegativeAmountError(amount)
        self.balance += amount
        print(f"✅ {amount} deposited. New Balance = {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise NegativeAmountError(amount)
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"💸 {amount} withdrawn. New Balance = {self.balance}")

    def check_balance(self):
        print(f"💰 Balance for {self.holder} (Acc {self.acc_no}) = {self.balance}")
        return self.balance


# ---- Bank Class ----
class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, acc):
        self.accounts[acc.acc_no] = acc
        print(f"🏦 Account created for {acc.holder}, Acc No: {acc.acc_no}")

    def get_account(self, acc_no):
        if acc_no not in self.accounts:
            raise AccountNotFoundError(acc_no)
        return self.accounts[acc_no]


if __name__ == "__main__":
    bank = Bank()

    acc1 = BankAccount(101, "Himanshu", 5000)
    acc2 = BankAccount(102, "Priya", 10000)

    bank.add_account(acc1)
    bank.add_account(acc2)

    try:
        acc = bank.get_account(101)
        acc.check_balance()
        acc.deposit(2000)
        acc.withdraw(3000)

        acc.withdraw(10000)

    except BankingError as e:
        print(e)

    try:
        acc.deposit(-500)
    except BankingError as e:
        print(e)

    try:
        bank.get_account(999)
    except BankingError as e:
        print(e)
