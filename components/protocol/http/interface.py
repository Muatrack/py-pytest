from abc import ABC, abstractmethod

# Define an abstract base class
class ClientIF(ABC):
    @abstractmethod
    def Get(url) -> dict:
        pass

    @abstractmethod
    def Post(url, headers:dict=0, payload:dict=0) -> dict:
        pass

