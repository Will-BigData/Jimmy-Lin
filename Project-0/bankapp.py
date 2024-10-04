from DAO.UserDAO import UserDAO
from DAO.AccountDAO import AccountDAO
from DAO.TransactionDAO import TransactionDAO

users = UserDAO()
accounts = AccountDAO()
transactions = TransactionDAO()

class Bank:
    login_options = {
        "text": "Welcome to the app",
        "options": {
            "l":{"text":"Login", "func": lambda s:s.login()},
            "q":{"text":"Quit", "func": lambda s:s.exit()},
        }
    }
    list_options = {
        "text": "These are your accounts",
        "display": lambda s: print(s.accounts),
        "options": {
            "s": {"text":"Select Account", "func": lambda a:print("WIP")},
            "c": {"text":"Create Account", "func": lambda a:print("WIP")},
            "l": {"text":"Logout", "func": lambda s:s.logout()},
            "q": {"text":"Quit", "func": lambda s:s.exit()},
        }
    }
    account_options = {
        "text": "What do you want to do with this Account",
        "options": {
            "d": {"text":"Deposit", "func": lambda a:print("WIP")},
            "w": {"text":"Withdraw", "func": lambda a:print("WIP")},
            "v": {"text":"View Transactions", "func": lambda a:print("WIP")},
            "s": {"text":"Select Another Account", "func": lambda a:print("WIP")},
            "u": {"text":"Update Account", "func": lambda a:print("WIP")},
            "x": {"text":"Delete Account", "func": lambda a:print("WIP")},
            "l": {"text":"Logout", "func": lambda s:s.logout()},
            "q": {"text":"Quit", "func": lambda s:s.exit()},
        }
    }

    def __init__(self):
        self.state = 0
        self.user = None
        self.accounts = []
        self.selected = None

    def run(self):
        self.running = True
        self.current_options = self.login_options
        while(self.running):
            self.handle_options()
            
    def handle_options(self, current=None):
        if current == None:
            current = self.current_options
        text = current['text']
        options = current['options']
        display = current.get('display')
        print(text)
        if display:
            display(self)
        for l,o in options.items():
            print(f'{l}: {o["text"]}')
        while(True):
            letter = input("Please choose an option: ")
            try:
                self.current_options['options'][letter]['func'](self)
                return
            except KeyError as e:
                print("Not an option")

    def update_options(self):
        if not self.user:
            self.current_options = self.login_options
            return
        if self.user and not self.selected:
            self.current_options = self.list_options
            return
        self.current_options =  self.account_options

    def update_user(self, user):
        self.user = user
        self.accounts = accounts.getAccountByUserID(user['id']) if user else []
        self.update_options()
    
    def exit(self):
        print("Thanks for using our app")
        self.running = False

    def login(self):
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        user = users.getUserByEmail(email=email)
        if not user:
            print("user not found")
            return
        if user['password'] != password:
            print("Incorrect password")
            return
        self.update_user(user)
        print("Login Successful")

    def logout(self):
        self.update_user(None)
        print("You have successfully logged out")
        
        

    

    
