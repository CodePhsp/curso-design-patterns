from abc import ABC, abstractmethod


class userInterface:
    @abstractmethod
    def getUser(self, id_user: int, name: str, userName: str):...