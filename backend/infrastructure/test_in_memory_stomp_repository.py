import pytest
from core.stomp_repository import StompRepository
from infrastructure.in_memory_stomp_repository import InMemoryStompRepository
from core.stomp import Stomp


class TestInMemoryStompRepository:
    """Test suite for InMemoryStompRepository class"""

    def test_initialization_creates_default_stomps(self):
        """Test that InMemoryStompRepository initializes with default stomps"""
        # Arrange & Act
        sut = InMemoryStompRepository()

        # Assert
        assert len(sut.stomps) == 1
        assert sut.stomps[0].id == "s-1"
        assert sut.stomps[0].name == "Stomp 1"
        assert sut.stomps[0].state == "off"

    def test_save_persist_new_stomps(self):
        """Test that save method accepts a stomp parameter without error"""
        # Arrange
        sut = InMemoryStompRepository()
        test_stomp = Stomp("s-2", "Test Stomp", "on")

        # Act
        sut.save(test_stomp)

        # Assert
        stomps = sut.get_stomps()
        assert len(sut.stomps) == 2
        assert sut.stomps[1].id == "s-2"
        assert sut.stomps[1].state == "on"

    def test_save_update_existing_stomp(self):
        """Test that save method accepts a stomp parameter without error"""
        # Arrange
        sut = InMemoryStompRepository()
        test_stomp = Stomp("s-1", "Foo", "on")

        # Act
        sut.save(test_stomp)

        # Assert
        stomps = sut.get_stomps()
        assert sut.stomps[0].id == "s-1"
        assert sut.stomps[0].state == "on"
        assert sut.stomps[0].name == "Foo"

    def test_get_stomps_returns_deep_copy(self):
        """Given get_stomps, when result is mutated, then repo state remains unchanged"""
        # Arrange
        sut = InMemoryStompRepository()

        # Act
        returned = sut.get_stomps()
        returned.append(Stomp("s-x", "Injected", "on"))
        returned[0].name = "Mutated Name"
        returned[0].updateState("on")

        # Assert
        assert len(sut.stomps) == 1
        assert sut.stomps[0].id == "s-1"
        assert sut.stomps[0].name == "Stomp 1"
        assert sut.stomps[0].state == "off"
        assert returned[0] is not sut.stomps[0]
