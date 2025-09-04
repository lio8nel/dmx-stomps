class Stomp:
    def __init__(self, id, name, state):
        self._id = id
        self.name = name
        self.state = state

    @property
    def id(self):
        return self._id

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
