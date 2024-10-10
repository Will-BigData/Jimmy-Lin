from .BasicDAO import BasicDAO
import datetime

class TransactionDAO:
    def __init__(self):
        self.basic = BasicDAO('Project-0/database/transaction.json')
        
    def getAllTransactions(self):
        return self.basic.read()
    
    def getTransactionByID(self, id):
        found = [u for u in self.basic.read() if u.get('id') == id]
        if(len(found) > 0):
            return found[0]
        return None
    
    def getTransactionByUserID(self, user_id):
        found = [u for u in self.basic.read() if u.get('owner_id') == user_id]
        return found
    
    def getTransactionByAccountID(self, account_id):
        found = [u for u in self.basic.read() if u.get('account_id') == account_id]
        return found
    
    def createTransaction(self, **kwarg):
        data = {
            "user_id": kwarg["user_id"],
            "account_id": kwarg["account_id"],
            "update": kwarg["update"],
            "reason": kwarg.get("reason", "None Given"),
            "date": str(datetime.datetime.now())
        }
        return self.basic.create(**data)
    
    def deleteTransaction(self, id):
        return self.basic.delete(id)
    
    def deleteTransactionByAccount(self, account_id):
        return self.basic.customDelete(lambda a: a['account_id'] != account_id)