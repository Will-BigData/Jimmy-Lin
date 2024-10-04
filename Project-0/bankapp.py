from DAO.UserDAO import UserDAO
from DAO.AccountDAO import AccountDAO
from DAO.TransactionDAO import TransactionDAO
import pandas as pd

users = UserDAO()
accounts = AccountDAO()
transactions = TransactionDAO()

class Bank:
    login_options = {
        "text": "Welcome to the app",
        "options": {
            "s":{"text":"Signup", "func": lambda s:s.signup()},
            "l":{"text":"Login", "func": lambda s:s.login()},
            "q":{"text":"Quit", "func": lambda s:s.exit()},
        }
    }
    list_options = {
        "text": "These are your accounts",
        "display": lambda s: s.display_accounts(),
        "options": {
            "s": {"text":"Select Account", "func": lambda s:s.select_account()},
            "c": {"text":"Create Account", "func": lambda s:s.create_account()},
            "l": {"text":"Logout", "func": lambda s:s.logout()},
            "q": {"text":"Quit", "func": lambda s:s.exit()},
        }
    }
    account_options = {
        "text": "What do you want to do with this Account",
        "display": lambda s: s.display_accounts(),
        "options": {
            "d": {"text":"Deposit", "func": lambda a:print("WIP")},
            "w": {"text":"Withdraw", "func": lambda a:print("WIP")},
            "c": {"text":"Cancel", "func": lambda s:s.unselect()},
            "v": {"text":"View Transactions", "func": lambda a:print("WIP")},
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
        self.transactions = []

    def run(self):
        self.running = True
        self.current_options = self.login_options
        while(self.running):
            self.handle_options()
            
    def handle_options(self, current=None, display=True):
        if current == None:
                current = self.current_options
        options = current['options']
        if display:
            text = current['text']
            display = current.get('display')
            print(text)
            if display:
                display(self)
            for l,o in options.items():
                print(f'{l}: {o["text"]}')
        while(True):
            letter = input("Please choose an option: ")
            try:
                current['options'][letter]['func'](self)
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

    def update_selected(self, selected):
        self.selected = selected
        self.transactions = transactions.getTransactionByAccountID(account_id=selected['id']) if selected else []
        self.update_options()
    
    def exit(self):
        print("Thanks for using our app")
        self.running = False

    #user related
    def signup(self):
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        user = users.createUser(email=email, password=password, name=name)
        if not user:
            print("This name or email is already in use")
            return
        self.update_user(user)
        print(user)
        print("SignUp Successful")

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
    #user related ends
    #Account List Related
    def display_accounts(self, selectedonly=False):
        data = {
            "index": [],
            "name": [],
            "amount": [],
            "type": []
        }
        for i, a in enumerate(self.accounts):
            if not selectedonly or a['id'] == self.selected['id']:
                data['index'].append(i)
                data['name'].append(a['name'])
                data["amount"].append(f'${a["amount"]:.2f}')
                data["type"].append(a['type'])
        print(pd.DataFrame(data))

    def create_account(self):
        name = input("Enter Account name")
        t = input("Enter Account Type:\nc: Checking\ns: Saving")
        types = {"c":"Checking", "s":"Saving"}
        while(t not in types.keys()):
            t = input("Please Enter a valid option:")
        acc_type = types[t]
        acc = accounts.createAccount(owner_id=self.user['id'], name=name, type=acc_type)
        self.accounts.append(acc)
        print("Account Successfully created")

    def select_account(self):
        if not len(self.accounts):
            print("You have no accounts")
        index = input("Select an Account by Index: ")
        try:
            self.update_selected(self.accounts[int(index)])
        except Exception as e:
            if index == 'b':
                print("Action cancelled")
                return
    #Account List Related Ends
            
    def unselect(self):
        self.update_selected(None)

        
        
        
        
        

    

    
