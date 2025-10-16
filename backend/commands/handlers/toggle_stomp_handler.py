from typing import Optional
from domain.stomp import Stomp
from domain.stomp_repository import StompRepository
from commands.toggle_stomp import ToggleStompCommand

class ToggleStompCommandHandler:
    def __init__(self, stomp_repository: StompRepository):
        self.stomp_repository = stomp_repository

    def execute(self, command: ToggleStompCommand) -> Optional[Stomp]:
        stomps = self.stomp_repository.get_stomps()
        stomp = next((s for s in stomps if s.id == command.stomp_id), None)
        if stomp is None:
            return None
        stomp.updateState(command.new_state)
        self.stomp_repository.save(stomp)
        return stomp
