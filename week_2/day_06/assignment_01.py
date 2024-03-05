# # Bank Account Management

# ## Objective
# Create a class for managing a bank account, emphasizing encapsulation with private attributes and methods.

# ## Requirements
# 1. Create a class named BankAccount with private attributes:
#    - \_\_account_number: A unique identifier for the bank account.
#    - \_\_balance: The current balance of the bank account.
#    - \_\_owner: The owner's name.

# 2. Implement the following methods within the BankAccount class:
#    - A constructor `__init__` to initialize the attributes.
#    - Getter methods for each attribute (get_account_number, get_balance, get_owner).
#    - Setter methods for each attribute (set_balance, set_owner).
#    - A method `deposit` to add funds to the account.
#    - A method `withdraw` to deduct funds from the account.

# 3. Implement input validation in the setter methods:
#    - Ensure that the balance is a non-negative value.
#    - Ensure that the owner's name is not empty.

# 4. Implement input validation in the `withdraw` method:
#    - Ensure that the withdrawal amount is less than or equal to the current balance.

# 5. Demonstrate the usage of the BankAccount class in the main program by creating an instance, setting attributes, depositing and withdrawing funds, and displaying account information.

class BankAccount:
    def __init__(self, account_number, balance, owner):
        self._account_number = account_number
        self._balance = balance
        self._owner = owner
        
    def get_account_number(self):
        return self._account_number
    
    def get_balance(self):
        return self._balance
    
    def get_owner(self):
        return self._owner
    
    
    def set_balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            print('\nBalance cannot be negative.')
            
    def set_owner(self, owner):
        if owner:
            self._owner = owner
        else:
            print('\nOwner name must be filled. ')
            
    def deposit(self):
        deposit_amt = float(input('\nEnter the amount you want to deopsit: '))
        if deposit_amt > 0:
            self._balance += deposit_amt
            print(f'{deposit_amt} deposited successfully.')
            
        else:
            print("\nPrint valid amount")
            
    def withdraw(self):
        
        amount = float(input('Enter wd amount '))
        if amount > self._balance:
            print('Insufficient balance. ')
        else:
            self._balance -= amount
            print(f'Amount withdrawn: {amount}')
    def display(self):
        print(f'\nNet Available Balance is {self.balance}')

            
if __name__ == '__main__':
    account = BankAccount('167575', 5000, 'Jaggy')
    print(f'Owner: {account.get_owner()}')
    print(f'Bank account: {account.get_account_number()}')
    print(f'Balance: {account.get_balance()}')
    

    
    # set new record
    account.set_balance(10000)
    account.set_owner(10000)
    
    # deposit amount
    account.deposit()
    # amount withdrawn
    account.withdraw()
    
    # updated information
    print(f'Updated balance is {account.get_balance()}')
    
    
    
    
    
        
        
            
        

        
    