from infrastructure.dmx_deamon import DmxDeamon


class TestDmxDeamon:
    def test_should_return_false_when_not_started(self):
        # Arrange
        sut = DmxDeamon()
        
        # Act
        result = sut.isRunning()
        
        # Assert
        assert result is False

    def test_should_return_true_after_starting(self):
        # Arrange
        sut = DmxDeamon()
        
        # Act
        sut.start()
        result = sut.isRunning()
        
        # Assert
        assert result is True

    def test_should_maintain_state_across_instances(self):
        # Arrange
        sut1 = DmxDeamon()
        sut2 = DmxDeamon()
        
        # Act
        sut1.start()
        result = sut2.isRunning()
        
        # Assert
        assert result is True
