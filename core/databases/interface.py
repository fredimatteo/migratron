from abc import ABC, abstractmethod

class DatabaseConnector(ABC):
    @abstractmethod
    def execute(self, query):
        pass

    @abstractmethod
    def rollback(self):
        pass