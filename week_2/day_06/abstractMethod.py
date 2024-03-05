
from abc import ABC, abstractmethod

class BankingApp(ABC):
    def database(self):
        print(f'Connect')
        
    @abstractmethod
    def security(self):
        pass
    
class MobileApp(BankingApp):
    def login(self):
        print(f'Login to mobile')
        
    def security(self):
        print('Securty is good')

if __name__ == '__main__':
    # bank = BankingApp()
    # bank.database()
    mobileApp = MobileApp()
    print(mobileApp)