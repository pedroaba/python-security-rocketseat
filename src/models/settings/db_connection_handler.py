import sqlite3


class __DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string: str = "storage.db"
        self.__connection = None

    def connect(self) -> None:
        self.__connection = sqlite3.connect(self.__connection_string)

    def get_connection(self) -> sqlite3.Connection:
        return self.__connection


db_connection_handler = __DBConnectionHandler()
