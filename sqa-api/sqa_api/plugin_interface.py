from abc import ABC, abstractmethod

class PluginBase(ABC):
    """
    Base class for plugins. All plugins must inherit from this class
    and implement the `collect` and `evaluate` methods.
    """

    @abstractmethod
    def collect(self, data: dict) -> str:
        """
        Process the input dictionary and return a modified dictionary.

        Args:
            data (Dict): Input data to be processed.

        Returns:
            Dict: Processed data.
        """
        pass

    @abstractmethod
    def evaluate(self, data: dict) -> dict:
        """
        Evaluate the input dictionary and return a modified dictionary.

        Args:
            data (Dict): Input data to be evaluated.

        Returns:
            Dict: Evaluated data.
        """
        pass

    def _validate_input(self, data: dict) -> bool:
        """
        Validate the input data.

        Args:
            data (Dict): Input data to be validated.

        Returns:
            bool: True if valid, False otherwise.
        """
        # Placeholder for validation logic
        return True
    
    def _validate_credentials(self, credentials: dict) -> bool:
        """
        Validate the credentials.

        Args:
            credentials (Dict): Credentials to be validated.

        Returns:
            bool: True if valid, False otherwise.
        """
        # Placeholder for validation logic
        return True
