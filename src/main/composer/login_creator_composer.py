from src.controllers.login_creator import LoginCreator
from src.models.repositories.user_repository import UserRepository
from src.models.settings.db_connection_handler import db_connection_handler

from src.views.login_creator import LoginCreatorView


def login_creator_composer():
    connection = db_connection_handler.get_connection()
    repository = UserRepository(connection)

    controller = LoginCreator(repository)
    view = LoginCreatorView(controller)
    return view
