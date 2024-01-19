import json
from pathlib import Path


class JSONFileHandler:
    @staticmethod
    def load(path: str) -> dict:
        """
        Loads a JSON file.

        Args:
            path (str): The path to the JSON file.

        Returns:
            dict: The JSON file as a dictionary.
        """
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def dump(path: str, data: dict) -> None:
        """
        Dumps a dictionary to a JSON file.

        Args:
            path (str): The path to the JSON file.
            data (dict): The dictionary to dump.
        """
        Path(path).parent.mkdir(exist_ok=True, parents=True)
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
