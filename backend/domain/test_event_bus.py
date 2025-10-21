import pytest
from domain.event_bus import EventBus
from domain.domain_event import DomainEvent
from domain.stomp_state_changed_event import StompStateChangedEvent

class TestEventBus:
    def setup_method(self):
        sut = EventBus()
        sut.clear_handlers()

    def test_should_publish_event_to_subscribed_handler(self):
        # Arrange
        sut = EventBus()
        received_events = []

        def handler(event):
            received_events.append(event)

        sut.subscribe(StompStateChangedEvent, handler)
        event = StompStateChangedEvent("stomp1", "off", "on")

        # Act
        sut.publish(event)

        # Assert
        assert len(received_events) == 1
        assert received_events[0] == event

    def test_should_publish_event_to_multiple_handlers(self):
        # Arrange
        sut = EventBus()
        handler1_calls = []
        handler2_calls = []

        sut.subscribe(StompStateChangedEvent, lambda e: handler1_calls.append(e))
        sut.subscribe(StompStateChangedEvent, lambda e: handler2_calls.append(e))
        event = StompStateChangedEvent("stomp1", "off", "on")

        # Act
        sut.publish(event)

        # Assert
        assert len(handler1_calls) == 1
        assert len(handler2_calls) == 1

    def test_should_not_call_handler_for_different_event_type(self):
        # Arrange
        sut = EventBus()
        received_events = []

        class OtherEvent(DomainEvent):
            pass

        sut.subscribe(StompStateChangedEvent, lambda e: received_events.append(e))
        event = OtherEvent()

        # Act
        sut.publish(event)

        # Assert
        assert len(received_events) == 0

    def test_should_work_as_singleton(self):
        # Arrange
        bus1 = EventBus()
        bus2 = EventBus()

        # Assert
        assert bus1 is bus2
