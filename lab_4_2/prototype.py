from abc import ABC, abstractmethod


class IPrototype(ABC):
    """
    Interface for prototype pattern implementation
    ...

    """
    @abstractmethod
    def clone(self):
        pass
