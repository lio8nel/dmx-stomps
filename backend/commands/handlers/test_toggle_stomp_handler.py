from infrastructure import InMemoryStompRepository
from .toggle_stomp_handler import ToggleStompCommandHandler
from commands.toggle_stomp import ToggleStompCommand

class TestToggleStompCommand:
    def test_toggle_success(self):
        # Arrange
        repository = InMemoryStompRepository()
        sut = ToggleStompCommandHandler(repository)
        stomp_id = repository.get_stomps()[0].id

        # Act
        result = sut.execute(ToggleStompCommand(stomp_id, "on"))

        # Assert
        assert result is not None
        assert result.state == "on"
        saved = next(s for s in repository.stomps if s.id == stomp_id)
        assert saved.state == "on"

    def test_toggle_not_found_returns_none(self):
        # Arrange
        repository = InMemoryStompRepository()
        sut = ToggleStompCommandHandler(repository)

        # Act
        result = sut.execute(ToggleStompCommand("unknown-id", "off"))

        # Assert
        assert result is None
