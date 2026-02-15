from user import User
from userProxy import UserProx


service = User()
mineProxy = UserProx(service)


print(mineProxy.getUser(1, 'Sabrina', 'Sah03'), end='\n\n\n')
print(mineProxy.getUser(1, 'Sabrina', 'Sah03'))
