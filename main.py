from util.JSONAccess import JSONAccess
from DAO.BasicDAO import BasicDAO

dao = BasicDAO('database/user.json')
dao.create(name="apple", date="no")
print(dao.read())
dao.update(name="apple pie", id=1)
print(dao.read())
dao.delete(id=1)
print(dao.read())






