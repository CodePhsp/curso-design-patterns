from userInterface import userInterface
import time


class User(userInterface):
    def getUser(self, id_user: int, name: str, userName: str) -> dict:
        print('Buscando usuário(a) na base de dados...')
        time.sleep(2)
        user = {
            'id': id_user,
            'name': name,
            'userName': userName
        }
        
        return user