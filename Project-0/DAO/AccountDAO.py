from .BasicDAO import BasicDAO

class AccountDAO:
    def __init__(self):
        self.basic = BasicDAO('Project-0/database/account.json')
        
    def getAllAccounts(self):
        return self.basic.read()
    
    def canUpdate(self, data):
        return (data.get("name") and data.get("amount") and data.get("type")) and data.get("owner_id")
    
    def getAccountByID(self, id):
        found = [u for u in self.basic.read() if u.get('id') == id]
        if(len(found) > 0):
            return found[0]
        return None
    
    def getAccountByUserID(self, user_id):
        found = [u for u in self.basic.read() if u.get('owner_id') == user_id]
        return found if found else []
    
    def createAccount(self, **kwarg):
        data = {
            "owner_id": kwarg["owner_id"],
            "name": kwarg["name"],
            "amount": 0,
            "type": kwarg["type"],
        }
        if(self.canUpdate(data)):
            return self.basic.create(**data)
        return False
    
    def updateAccount(self, id, **kwarg):
        found = self.getAccountByID(id)
        if(not found):
            return False
        data = {
            "owner_id": kwarg.get("owner_id", found["owner_id"]),
            "name": kwarg.get("name", found["name"]),
            "amount": kwarg.get("amount", found["amount"]),
            "type": kwarg.get("type", found["type"]),
        }
        if(self.canUpdate(data)):
            return self.basic.update(**data, id=id)
        return False
    
    def deleteAccount(self, id):
        return self.basic.delete(id)
