from account import Account

class User(Account):
    def __init__(self,name,password, email, document):
        super().__init__(name,password,email,document)