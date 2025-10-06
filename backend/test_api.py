from fastapi.testclient import TestClient
from unittest.mock import Mock, patch
from api import app
from core import Stomp, StompRepository
from infrastructure import InMemoryStompRepository, DmxDeamon


class TestToggleStomps:
    """Test suite for toggle_stomps functionality"""

    @patch("api.ToggleStompCommand")
    def test_toggle_stomp_success_calls_command(self, mock_command_cls):
        """When toggling, the command is invoked with id and state"""
        # Arrange
        stomp_id = "s-1"
        mock_command = Mock()
        mock_command.execute.return_value = Stomp(id=stomp_id, name="Stomp 1", state="off")
        mock_command_cls.return_value = mock_command
        app.dependency_overrides[InMemoryStompRepository] = lambda: Mock()
        client = TestClient(app)

        # Act
        response = client.put(f"/stomps/{stomp_id}", json={"state": "off"})

        # Assert
        assert response.status_code == 200
        mock_command_cls.assert_called_once()
        mock_command.execute.assert_called_once_with(stomp_id, "off")
        data = response.json()
        assert data["id"] == stomp_id
        assert data["state"] == "off"

    @patch("api.ToggleStompCommand")
    def test_toggle_stomp_notfound_returns_404(self, mock_command_cls):
        """When command returns None, API responds 404"""
        # Arrange
        stomp_id = "s-1"
        mock_command = Mock()
        mock_command.execute.return_value = None
        mock_command_cls.return_value = mock_command
        app.dependency_overrides[InMemoryStompRepository] = lambda: Mock()
        client = TestClient(app)

        # Act
        response = client.put(f"/stomps/{stomp_id}", json={"state": "on"})

        # Assert
        assert response.status_code == 404
        mock_command.execute.assert_called_once_with(stomp_id, "on")
        data = response.json()
        assert data["detail"] == "Stomp not found"


class TestGetStomps:
    """Test suite for get_stomps endpoint"""

    @patch("infrastructure.InMemoryStompRepository")
    def test_get_stomps_uses_mocked_repository(self, mock_stomp_repository):
        """Test retrieval of stomps comes from mocked InMemoryStompRepository"""
        # Arrange
        mock_stomp_repository.get_stomps.return_value = [
            Stomp(id="s-1", name="Mocked Stomp 1", state="on"),
            Stomp(id="s-2", name="Mocked Stomp 2", state="off"),
        ]
        app.dependency_overrides[InMemoryStompRepository] = lambda: mock_stomp_repository
        client = TestClient(app)

        # Act
        response = client.get("/stomps")

        # Assert
        assert response.status_code == 200
        data = response.json()
        assert "stomps" in data
        assert isinstance(data["stomps"], list)
        assert len(data["stomps"]) == 2
        assert data["stomps"][0]["id"] == "s-1"
        assert data["stomps"][0]["name"] == "Mocked Stomp 1"
        assert data["stomps"][0]["state"] == "on"
        assert data["stomps"][1]["id"] == "s-2"
        assert data["stomps"][1]["name"] == "Mocked Stomp 2"
        assert data["stomps"][1]["state"] == "off"


class TestDeamonRoutes:
    """Test suite for /deamon/start endpoint"""

    class FakeDmxDeamon(DmxDeamon):
        def __init__(self):
            self._running = False
            self.start_calls = 0
            self.stop_calls = 0

        def start(self) -> None:
            self.start_calls += 1
            self._running = True

        def stop(self) -> None:
            self.stop_calls += 1
            self._running = False

        def isRunning(self) -> bool:
            return self._running

    def test_start_triggers_dmx_deamon(self):
        """When POST /deamon/start, the DmxDeamon.start is invoked"""
        # Arrange
        fake = self.FakeDmxDeamon()
        app.dependency_overrides[DmxDeamon] = lambda: fake

        sut = TestClient(app)

        # Act
        response = sut.post("/deamon/start")

        # Assert
        assert response.status_code == 200
        assert fake.start_calls == 1
        assert fake.isRunning() is True

    def test_start_does_not_trigger_when_already_running(self):
        """When POST /deamon/start and daemon is running, start is not invoked"""
        # Arrange
        fake = self.FakeDmxDeamon()
        app.dependency_overrides[DmxDeamon] = lambda: fake

        sut = TestClient(app)
        sut.post("/deamon/start")

        # Act
        response = sut.post("/deamon/start")

        # Assert
        assert response.status_code == 200
        assert fake.start_calls == 1
        assert fake.isRunning() is True

    def test_stop_triggers_dmx_deamon(self):
        """When POST /deamon/stop, the DmxDeamon.stop is invoked"""
        # Arrange
        fake = self.FakeDmxDeamon()
        app.dependency_overrides[DmxDeamon] = lambda: fake

        sut = TestClient(app)
        response = sut.post("/deamon/start")

        # Act
        response = sut.post("/deamon/stop")

        # Assert
        assert response.status_code == 200
        assert fake.stop_calls == 1
        assert fake.isRunning() is False

    def test_stop_does_not_trigger_when_already_stopped(self):
        """When POST /deamon/stop and daemon not running, stop is not invoked"""
        # Arrange
        fake = self.FakeDmxDeamon()
        fake.running = False
        app.dependency_overrides[DmxDeamon] = lambda: fake

        sut = TestClient(app)

        # Act
        response = sut.post("/deamon/stop")

        # Assert
        assert response.status_code == 200
        assert fake.stop_calls == 0
        assert fake.isRunning() is False