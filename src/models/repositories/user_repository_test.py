from src.models.settings.db_connection_handler import db_connection_handler
from .user_repository import UserRepository


def test_repository():
    db_connection_handler.connect()
    repository = UserRepository(db_connection_handler.get_connection())

    username = "Bob Esponja"
    password = "123Rocket!"

    repository.registry_user(username, password)
    user = repository.get_user_by_username(username)

    print()
    print(user)
