from domain.event_bus import EventBus
from domain.stomp_state_changed_event import StompStateChangedEvent

class Stomp:
    def __init__(self, id, name, state, event_bus: EventBus = None):
        self._id = id
        self.name = name
        self._state = state
        self._event_bus = event_bus or EventBus()

    @property
    def id(self):
        return self._id

    @property
    def state(self):
        return self._state

    def updateState(self, value):
        old_state = self._state
        self._state = value
        self._event_bus.publish(StompStateChangedEvent(self._id, old_state, value))
