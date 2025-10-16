from typing import Optional
from domain.stomp import Stomp
from domain.stomp_repository import StompRepository

class ToggleStompCommand:
    def __init__(self, stomp_id: str, new_state: str):
        self.stomp_id = stomp_id
        self.new_state = new_state
