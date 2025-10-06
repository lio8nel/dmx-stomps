class DmxDeamon:
    _instance = None
    _isRunning = False
    def __new__(class_):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_)
        return class_._instance

    def start(self) -> None:
        self._isRunning = True
        pass

    def stop(self) -> None:
        pass
    
    def isRunning(self) -> bool:
        return self._isRunning
