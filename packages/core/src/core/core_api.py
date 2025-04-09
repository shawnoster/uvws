from abc import ABC, abstractmethod

class PluginBase(ABC):
    """
    Base class for plugins. All plugins must inherit from this class
    and implement the `collect` method.
    """

    @abstractmethod
    def collect(self, data: dict) -> dict:
        """
        Process the input dictionary and return a modified dictionary.

        Args:
            data (Dict): Input data to be processed.

        Returns:
            Dict: Processed data.
        """
        pass
