from .BasicDAO import BasicDAO
import datetime

class UserDAO:
    def __init__(self):
        self.basic = BasicDAO('Project-0/database/user.json')
        
    def getAllUsers(self):
        return self.basic.read()
    
    def canUpdate(self, data, id=None):
        if not (data.get("name") and data.get("email") and data.get("password")):
            return False
        for u in self.getAllUsers():
            if id == u['id']:
                continue
            if u.get("name") == data.get("name") or u.get("email") == data.get("email"):
                return False
        return True
    
    def getUserByID(self, id):
        found = [u for u in self.basic.read() if u.get('id') == id]
        if(len(found) > 0):
            return found[0]
        return None
    
    def getUserByEmail(self, email):
        found = [u for u in self.basic.read() if u.get('email') == email]
        if(len(found) > 0):
            return found[0]
        return None
    
    def createUser(self, **kwarg):
        data = {
            "name": kwarg["name"],
            "email": kwarg["email"],
            "password": kwarg["password"]
        }
        if(self.canUpdate(data)):
            return self.basic.create(**data)
        return False
    
    def deleteUser(self, id):
        return self.basic.delete(id)
