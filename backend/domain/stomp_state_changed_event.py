from domain.domain_event import DomainEvent

class StompStateChangedEvent(DomainEvent):
    def __init__(self, stomp_id: str, old_state: str, new_state: str):
        super().__init__()
        self.stomp_id = stomp_id
        self.old_state = old_state
        self.new_state = new_state

    def __repr__(self):
        return f"StompStateChangedEvent(stomp_id={self.stomp_id}, old_state={self.old_state}, new_state={self.new_state}, occurred_at={self.occurred_at})"
