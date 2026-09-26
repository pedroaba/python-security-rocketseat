from abc import ABC, abstractmethod


class UserRegisterInterface(ABC):
    @abstractmethod
    def register(self, username: str, password: str) -> dict:
        raise NotImplementedError()
