import json

class JSONAccess:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as file:
            return json.load(file)
        
    def write(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)