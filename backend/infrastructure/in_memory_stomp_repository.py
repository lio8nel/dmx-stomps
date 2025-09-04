from core.stomp import Stomp
from core.stomp_repository import StompRepository
import copy


class InMemoryStompRepository(StompRepository):
    def __init__(self):
        self.stomps = [
            Stomp(id="s-1", name="Stomp 1", state="off"),
        ]

    def get_stomps(self):
        return copy.deepcopy(self.stomps)

    def save(self, stomp):
        existingStomp = next((s for s in self.stomps if s.id == stomp.id), None)

        if existingStomp is None:
            self.stomps.append(stomp)
        else:
            existingStomp.name = stomp.name
            existingStomp.state = stomp.state
