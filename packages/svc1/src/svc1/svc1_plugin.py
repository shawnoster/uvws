
from core.core_api import PluginBase


class Svc1Plugin(PluginBase):
    """
    Plugin for svc1.
    """

    def collect(self, data: dict) -> str:
        """
        Process the input dictionary and return a modified dictionary.

        Args:
            data (Dict): Input data to be processed.

        Returns:
            Dict: Processed data.
        """
        if "svc1" not in data:
            raise "service one key is missing in the input data"
        return "svc1"

    def evaluate(self, data: dict) -> dict:
        """
        Evaluate the input dictionary and return a modified dictionary.

        Args:
            data (Dict): Input data to be evaluated.

        Returns:
            Dict: Evaluated data.
        """
        return {"svc1": "svc1"}
