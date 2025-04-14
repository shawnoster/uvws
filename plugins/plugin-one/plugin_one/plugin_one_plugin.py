from sqa_api.plugin_interface import PluginBase, PluginInvalidCredentials, PluginInvalidInput


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
            raise PluginInvalidInput("Missing required field: serviceName")

        return "serviceName"

    def evaluate(self, data: dict) -> dict:
        """
        Evaluate the input dictionary and return a modified dictionary.

        Args:
            data (Dict): Input data to be evaluated.

        Returns:
            Dict: Evaluated data.
        """
        if "serviceName" not in data:
            raise PluginInvalidCredentials("Missing required field: serviceName")
                
        return {"serviceName": "test-four"}
