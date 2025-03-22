from abc import ABC, abstractmethod

import psycopg


class DatabaseConnector(ABC):
    @abstractmethod
    def connection(self) -> "psycopg.connection":
        pass

    @abstractmethod
    def execute(self, query):
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass