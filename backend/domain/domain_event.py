from abc import ABC
from datetime import datetime
from typing import Any

class DomainEvent(ABC):
    def __init__(self):
        self.occurred_at = datetime.now()

    def __repr__(self):
        return f"{self.__class__.__name__}(occurred_at={self.occurred_at})"
