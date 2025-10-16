from abc import ABC, abstractmethod
from .stomp import Stomp


class StompRepository(ABC):
    @abstractmethod
    def get_stomps(self):
        pass

    @abstractmethod
    def save(self, stomp: Stomp):
        pass
