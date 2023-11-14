from abc import ABC, abstractmethod

class tire(ABC):
    @abstractmethod
    def needs_service(self):
        pass
