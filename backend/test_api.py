import pytest
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch
from api import app
from core import Stomp, StompRepository
from infrastructure import InMemoryStompRepository


class TestToggleStomps:
    """Test suite for toggle_stomps functionality"""
    
    @patch("infrastructure.InMemoryStompRepository")
    def test_toggle_stomp_success(self, mock_stomp_repository):
        """Test successful toggle of a stomp"""
        # Arrange
        stomp_id = "s-1"
        mock_stomp_repository.get_stomps.return_value = [
            Stomp(id="s-1", name="Stomp 1", state="on")
        ]
        app.dependency_overrides[InMemoryStompRepository] = lambda: mock_stomp_repository
        client = TestClient(app)

        # Act
        response = client.put(f"/stomps/{stomp_id}", json={"state": "off"})
        
        # Assert
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == stomp_id
        assert data["state"] == "off"
    
    @patch("infrastructure.InMemoryStompRepository")
    def test_toggle_stomp_notfound(self, mock_stomp_repository):
        """Test toggle of a stomp that does not exist"""
        # Arrange
        stomp_id = "s-1"
        mock_stomp_repository.get_stomps.return_value = []
        app.dependency_overrides[InMemoryStompRepository] = lambda: mock_stomp_repository
        client = TestClient(app)
        
        # Act
        response = client.put(f"/stomps/{stomp_id}", json={"state": "on"})
        
        # Assert
        assert response.status_code == 404
        data = response.json()
        assert data["detail"] == "Stomp not found"

    @patch("infrastructure.InMemoryStompRepository")
    def test_stomp_state_was_saved(self, mock_stomp_repository):
        """Test that stomp's state has been saved after toggle"""
        # Arrange
        stomp_id = "s-1"
        mock_stomp_repository.get_stomps.return_value = [
            Stomp(id="s-1", name="Stomp 1", state="on")
        ]
        app.dependency_overrides[InMemoryStompRepository] = lambda: mock_stomp_repository
        client = TestClient(app)
        
        # Act
        client.put(f"/stomps/{stomp_id}", json={"state": "off"})
        
        # Assert
        mock_stomp_repository.save.assert_called_once()
        saved_stomp = mock_stomp_repository.save.call_args[0][0]
        assert saved_stomp.id == "s-1"
        assert saved_stomp.state == "off"


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
