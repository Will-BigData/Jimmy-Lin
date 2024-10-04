from .BasicDAO import BasicDAO
import datetime

class TransactionDAO:
    def __init__(self):
        self.basic = BasicDAO('Project-0/database/transaction.json')
        
    def getAllTransactions(self):
        return self.basic.read()
    
    def canUpdate(self, data):
        return (data.get("name") and data.get("amount") and data.get("type")) and data.get("owner_id")
    
    def getTransactionByID(self, id):
        found = [u for u in self.basic.read() if u.get('id') == id]
        if(len(found) > 0):
            return found[0]
        return None
    
    def getTransactionByUserID(self, user_id):
        found = [u for u in self.basic.read() if u.get('owner_id') == user_id]
        return found
    
    def createTransaction(self, **kwarg):
        data = {
            "user_id": kwarg["user_id"],
            "account_id": kwarg["account_id"],
            "update": kwarg["update"],
            "reason": kwarg.get("reason", "None Given"),
            "date": datetime.datetime.now()
        }
        if(self.canUpdate(data)):
            return self.basic.create(**data)
        return False
    
    def deleteTransaction(self, id):
        return self.basic.delete(id)
