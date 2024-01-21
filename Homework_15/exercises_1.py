class BankAccount:
    def __init__(self,account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def d_deposit(self,amount):
        self.balance += amount
    
    def p_withdraw(self,amount):
        self.balance -= amount
        
    def p_get_balance(self):      
        return f"{self.account_number} {self.balance}"
    
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance,interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def p_deposit(self, amount):
        self.balance += amount + (amount*(self.interest_rate/100))
        return self.balance


class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_fee):
        super().__init__(account_number, balance)      
        self.overdraft_fee = overdraft_fee

    def p_withdraw(self,amount):
        if amount > self.balance:
            self.balance -= (amount + self.overdraft_fee)
        return self.balance    
   
    
x = SavingsAccount("Abc0107",0,10)
x.p_deposit(100)
print(x.p_get_balance())
        