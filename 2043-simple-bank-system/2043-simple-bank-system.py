class Bank:
    def __init__(self, balance):
        self.balance = balance

    def transfer(self, account1, account2, money):
        if not self.accountNumberIsValid(account1) or not self.accountNumberIsValid(account2) or self.balance[account1 - 1] < money:   
            return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account, money):
        if not self.accountNumberIsValid(account):
            return False
        self.balance[account - 1] += money
        return True
    
    def withdraw(self, account, money):
        if not self.accountNumberIsValid(account) or self.balance[account - 1] < money: 
            return False
        self.balance[account - 1] -= money
        return True

    def accountNumberIsValid(self, account):
        if 1 <= account and account <= len(self.balance):
            return True
        return False