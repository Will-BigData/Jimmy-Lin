# from util.JSONAccess import JSONAccess
import math
from DAO.UserDAO import UserDAO
from DAO.AccountDAO import AccountDAO

dao = AccountDAO()
user = UserDAO()
# dao.createUser(name="apple", email="no", password="no")
# print(dao.getAllUsers())
# dao.updateUser(id=0, name="apple pie")
# print(dao.getAllUsers())
# dao.update(name="apple pie", id=1)
# print(dao.read())
# dao.delete(id=0)
# print(dao.read())
# dao.delete(id=2)
# print(dao.read())
# dao.delete(id=3)
# print(dao.read())
li = [[1,2,3],[2,3,4],[3,4]]

li2 = [x for y in li for x in y]
print(li2)







