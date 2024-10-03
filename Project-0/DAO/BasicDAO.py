from util.JSONAccess import JSONAccess

class BasicDAO:
    def __init__(self, filename):
        self.connection = JSONAccess(filename)
        self.jsondata = self.connection.read()
        if not self.jsondata:
            self.jsondata = []
            self.write()
        pass

    def getNewID(self):
        id = -1
        for u in self.jsondata:
            id = max(id,u.get('id', -1))
        return id+1
    
    def match(self):
        self.jsondata = self.connection.read()

    def read(self):
        return self.jsondata
    
    def write(self):
        self.connection.write(self.jsondata)
    
    def create(self, **data):
        data['id'] = self.getNewID()
        self.jsondata.append(data)
        self.write()
        

    def update(self, id, **data):
        self.jsondata = list(map(lambda x:{**x, **data} if x.get('id') == id else x, self.jsondata))
        self.write()

    def delete(self, id):
        self.jsondata = list(filter(lambda x:x.get('id') != id, self.jsondata))
        self.write()