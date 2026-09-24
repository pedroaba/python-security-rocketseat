from .user_register import UserRegister


class MockUserRepository:
    def __init__(self) -> None:
        self.registry_user_attributes = {}

    def registry_user(self, username, password) -> None:
        self.registry_user_attributes["username"] = username
        self.registry_user_attributes["password"] = password


def test_registry():
    repository = MockUserRepository()
    controller = UserRegister(repository)

    username = "olamundo"
    password = "mypassword"

    response = controller.register(username, password)

    assert response == {"type": "User", "count": 1, "username": "olamundo"}
    assert repository.registry_user_attributes["password"] is not None
    assert password != repository.registry_user_attributes["password"]
    assert username == repository.registry_user_attributes["username"]
