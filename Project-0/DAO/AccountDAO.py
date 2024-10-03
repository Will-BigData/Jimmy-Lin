from .BasicDAO import BasicDAO

class AccountDAO:
    def __init__(self):
        self.basic = BasicDAO('Project-0/database/account.json')
        
    def getAllAccounts(self):
        return self.basic.read()
    
    def canUpdate(self, data, id=None):
        if not (data.get("name") and data.get("email") and data.get("password")):
            return False
        for u in self.getAllAccounts():
            print(u['id'])
            print(id)
            if id == u['id']:
                print("triggered")
                continue
            if u.get("name") == data.get("name") or u.get("email") == data.get("email"):
                return False
        return True
    
    def getAccountByID(self, id):
        found = [u for u in self.basic.read() if u.get('id') == id]
        if(len(found) > 0):
            return found[0]
        return None
    
    def createAccount(self, **kwarg):
        data = {
            "name": kwarg["name"],
            "email": kwarg["email"],
            "password": kwarg["password"]
        }
        if(self.canUpdate(data)):
            return self.basic.create(**data)
        return False
    
    def updateAccount(self, id, **kwarg):
        found = self.getAccountByID(id)
        if(not found):
            return False
        data = {
            "name": kwarg.get("name", found['name']),
            "email": kwarg.get("email", found['email']),
            "password": kwarg.get("password", found['password']),
        }
        if(self.canUpdate(data, id)):
            return self.basic.update(**data, id=id)
        return False
    
    def deleteAccount(self, id):
        return self.basic.delete(id)
