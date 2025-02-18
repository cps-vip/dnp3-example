from enum import Enum
from abc import ABC, abstractmethod


class DeviceState(Enum):
    INITIALIZED = 0
    ACTIVE = 1
    INACTIVE = 2


class Device(ABC):
    def __init__(self, name: str):
        self._name = name

    @abstractmethod
    def activate(self) -> None:
        """
        Sets the device state to active and starts or restarts communication, depending on if coming from inactive or initialized state
        """
        pass

    @abstractmethod
    def deactivate(self) -> None:
        """
        Sets the device state to inactive and stops communication
        """
        pass

    @property
    def name(self) -> str:
        return self._name

    @property
    def state(self) -> DeviceState:
        return self._state

    @state.setter
    def state(self, new_state: DeviceState) -> None:
        self._state = new_state

