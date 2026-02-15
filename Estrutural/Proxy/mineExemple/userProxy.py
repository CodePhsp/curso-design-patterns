from user import userInterface


class UserProx(userInterface):
    def __init__(self, service: userInterface):
        self._service = service
        self._userCache = {}
        
    def getUser(self, id_user, name, userName) -> dict:
        if id_user in self._userCache:
            print('Proxy: Do cache após nova consulta')
            return self._userCache[id_user]
        
        print(f'Proxy: {name} não foi encontrado(a) no cache')
        newUser = self._service.getUser(id_user, name, userName)
        self._userCache[id_user] = newUser
            
        return newUser