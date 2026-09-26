from src.controllers.interfaces.user_register import UserRegisterInterface
from src.models.interfaces.user_repository import UserRepositoryInterface
from src.drivers.password_handler import PasswordHandler


class UserRegister(UserRegisterInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__repository = user_repository
        self.__password_handler = PasswordHandler()

    def register(self, username: str, password: str) -> dict:
        hashed_password = self.__create_hash_password(password)
        self.__register_new_user(username, hashed_password)

        return self.__format_response(username)

    def __create_hash_password(self, password: str) -> str:
        return self.__password_handler.encrypt_password(password)

    def __register_new_user(self, username: str, hashed_password: str) -> None:
        self.__repository.registry_user(username, hashed_password)

    def __format_response(self, username: str) -> dict:
        return {"type": "User", "count": 1, "username": username}
