from abc import ABC, abstractmethod

class PluginBase(ABC):
    """
    Base class for plugins. All plugins must inherit from this class
    and implement the `collect` and `evaluate` methods.
    """

    @abstractmethod
    def collect(self, data: str) -> str:
        """
        Process the input dictionary and return a modified dictionary.

        Args:
            data (Dict): Input data to be processed.

        Returns:
            Dict: Processed data.
        """
        pass

    @abstractmethod
    def evaluate(self, data: str) -> dict:
        """
        Evaluate the input dictionary and return a modified dictionary.

        Args:
            data (Dict): Input data to be evaluated.

        Returns:
            Dict: Evaluated data.
        """
        pass
