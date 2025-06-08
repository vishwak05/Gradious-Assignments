# Implementing a Transaction protocol to perform financial transactions

# Creating a transaction class for defining methods of protocol
class Transaction:
    # To execute the transaction
    def execute(self):
        pass
    
    # To update the balance of account
    def update_balances(self):
        pass

# Account class to represent a bank account
class Account:
    def __init__(self, owner:str, balance:float):
        self.owner = owner      # Name of account holder
        self.balance = balance  # Current balance in account
    
    # String representation of account
    def __repr__(self):
        return f"Account owner: {self.owner}, balance: {self.balance}"

# Deposit Transaction class to add money into account
class Deposit(Transaction):
    def __init__(self, account:Account, amount:float):
        self.account = account  # Account to deposit money into
        self.amount = amount    # Amount of money to deposit
    
    # Perform deposit and print the Transaction result
    def execute(self):
        self.update_balances()
        print(f"Amount {self.amount} deposited into {self.account.owner}'s account, balance: {self.account.balance}")
    
    # Add the deposit money to account balance
    def update_balances(self):
        self.account.balance += self.amount

# Withdraw Transaction class to remove money from account
class Withdraw(Transaction):
    def __init__(self, account:Account, amount:float):
        self.account = account  # Account to withdraw money from
        self.amount = amount    # Amount of money to withdraw
    
    # Perform withdraw and print the Transaction result
    def execute(self):
        # Check if account has enough money to withdraw
        if self.account.balance >= self.amount:
            self.update_balances()
            print(f"Amount {self.amount} withdrawn from {self.account.owner}'s account, balance: {self.account.balance}")
        else:
            print(f"Insufficient funds in account, balance: {self.account.balance}")
    
    # Remove the withdraw money from account balance
    def update_balances(self):
        self.account.balance -= self.amount

# Transfer funds Transaction class to move money from one account to another account
class Transfer_amount(Transaction):
    def __init__(self, from_acc:Account, to_acc:Account, amount:float):
        self.from_acc = from_acc    # Sender's account
        self.to_acc = to_acc        # Reciever's account
        self.amount = amount        # Amount to tranfer between accounts
    
    # Perform the transfer of funds
    def execute(self):
        # Check if sender's account has enough money to transfer
        if self.from_acc.balance > self.amount:
            self.update_balances()
            print(f"Amount {self.amount} transferred from {self.from_acc.owner}'s account, balance: {self.from_acc.balance} to {self.to_acc.owner}'s account, balance: {self.to_acc.balance}")
        else:
            print(f"Insufficient funds in sender {self.from_acc.owner}'s account, balance: {self.from_acc.balance}")
    
    # Update the account balances after transaction
    def update_balances(self):
        # Remove money from sender's account
        self.from_acc.balance -= self.amount
        # Add money to reciever's account
        self.to_acc.balance += self.amount

# Method to run the Unit Tests for all types of Transactions
def run_unit_tests():
    # Sample Accounts
    acc1 = Account("Sai", 20000)
    acc2 = Account("Shreya", 35000)
    acc3 = Account("Shobha", 45000)
    acc4 = Account("Shaani", 5000)

    # Test:1 Deposit amount (Transaction should be successful)
    d = Deposit(acc1, 5000)
    print("\nExecuting the unit tests:\n")
    d.execute()
    if acc1.balance == 25000:
        print("Test 1: Passed")
    else:
        print("Test 1: Failed")
    
    # Test 2: Withdraw amount (Transaction should be successful)
    w1 = Withdraw(acc2, 3000)
    print()
    w1.execute()
    if acc2.balance == 32000:
        print("Test 2: Passed")
    else:
        print("Test 2: Failed")
    
    # Test 3: Withdraw amount (Transaction should fail due to insufficient funds)
    w2 = Withdraw(acc4, 6000)
    print()
    w2.execute()
    if acc4.balance == 5000:
        print("Test 3: Passed")
    else:
        print("Test 3: Failed")
    
    # Test 4: Transfer amount (Transaction should be successful)
    t1 = Transfer_amount(acc1, acc3, 1500)
    print()
    t1.execute()
    if acc1.balance == 23500 and acc3.balance == 46500:
        print("Test 4: Passed")
    else:
        print("Test 4: Failed")
    
    # Test 5: Transfer amount (Transaction should fail due to insufficient funds)
    t2 = Transfer_amount(acc4, acc2, 5500)
    print()
    t2.execute()
    if acc4.balance == 5000 and acc2.balance == 32000:
        print("Test 5: Passed")
    else:
        print("Test 5: Failed")

# Executing the Transactions
if __name__ == "__main__":
    # Sample Accounts
    acc1 = Account("Sai", 20000)
    acc2 = Account("Shreya", 35000)
    acc3 = Account("Shobha", 45000)
    acc4 = Account("Shaani", 5000)

    # Creating transactions objects in a list
    txs = [
        Deposit(acc1, 5000),
        Withdraw(acc2, 3000),
        Transfer_amount(acc1, acc3, 1500)
    ]

    # Demostration of Duck Typing where all Transactions have same method execute()
    for tx in txs:
        tx.execute()

    # Running the unit tests
    run_unit_tests()