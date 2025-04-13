from sqa_api.plugin_interface import PluginBase


class PluginOnePlugin(PluginBase):
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
        if "serviceName" not in data:
            raise ValueError("service one key is missing in the input data")

        return "serviceName"

    def evaluate(self, data: dict) -> dict:
        """
        Evaluate the input dictionary and return a modified dictionary.

        Args:
            data (Dict): Input data to be evaluated.

        Returns:
            Dict: Evaluated data.
        """
        return {"svc1": "svc1"}
