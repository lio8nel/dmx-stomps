import pytest
from core.stomp import Stomp


class TestStomp:
    """Test suite for Stomp class"""

    def test_stomp_initialization_with_valid_parameters(self):
        """Test Stomp initialization with valid parameters"""
        # Arrange
        stomp_id = "s-1"
        name = "Test Stomp"
        state = "on"

        # Act
        sut = Stomp(stomp_id, name, state)

        # Assert
        assert sut.id == stomp_id
        assert sut.name == name
        assert sut.state == state
