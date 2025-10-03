from typing import Optional
from .stomp import Stomp
from .stomp_repository import StompRepository


class ToggleStompCommand:
    def __init__(self, stomp_repository: StompRepository):
        self.stomp_repository = stomp_repository

    def execute(self, stomp_id: str, new_state: str) -> Optional[Stomp]:
        stomps = self.stomp_repository.get_stomps()
        stomp = next((s for s in stomps if s.id == stomp_id), None)
        if stomp is None:
            return None
        stomp.updateState(new_state)
        self.stomp_repository.save(stomp)
        return stomp
