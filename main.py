from DAO.JSONAccess import JSONAccess

userReader = JSONAccess('database/user.json')
users = userReader.read()

updated = userReader.write([{"new":"data"}])

# with open('database/user.json', 'r') as userfile:
#     users = json.load(userfile)

# # users.append({"this": "loser"})
# users = [{**u, "checked":True} for u in users if u['this']!="winner"]

# with open('database/user.json', 'w') as writefile:
#     json.dump(users, writefile, indent=4)
#     # newusers = list(filter(lambda x:x["this"]!="winner", users))

#     # json.dumps(newusers)



print(users)
print(updated)
print(type(users))

