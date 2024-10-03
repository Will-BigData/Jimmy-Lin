from .BasicDAO import BasicDAO

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
            "owner_id": kwarg["owner_id"],
            "name": kwarg["name"],
            "amount": kwarg["amount"],
            "type": kwarg["type"],
        }
        if(self.canUpdate(data)):
            return self.basic.create(**data)
        return False
    
    def updateTransaction(self, id, **kwarg):
        found = self.getTransactionByID(id)
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
    
    def deleteTransaction(self, id):
        return self.basic.delete(id)
