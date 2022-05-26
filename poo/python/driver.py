from account import Account

class Driver(Account):
    def __init__(self,name,password, email, document):
        super().__init__(name,password,email,document)