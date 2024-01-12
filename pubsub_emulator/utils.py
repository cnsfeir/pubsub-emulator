import json
import re

from caseconverter import snakecase

from pubsub_emulator.constants import LOCAL_BASE_URL, SERVICE_MAPPINGS_PATH, SERVICE_NAME_PATTERN


def to_snakecase(original: dict) -> dict:
    """
    Changes the keys of a dictionary to snake_case.
    """
    new = {snakecase(key): value for key, value in original.items()}
    for key, value in new.items():
        if isinstance(value, dict):
            new[key] = to_snakecase(value)
    return new


def update_dictionary(original: dict, new: dict) -> dict:
    """
    Recursively merges the new dictionary into the original dictionary overwriting existing values.
    """
    for key, value in new.items():
        if key in original and isinstance(original[key], dict) and isinstance(value, dict):
            update_dictionary(original[key], value)
            continue

        original[key] = value
    return original


def translate_url(url: str) -> str:
    """
    Translates the Cloud service URL to their local equivalent.
    """
    if not (match := re.search(SERVICE_NAME_PATTERN, url)):
        raise ValueError(f"Invalid URL {url}")

    service = match.group(1)
    endpoint = url[len(match.group(0)) :]

    with open(SERVICE_MAPPINGS_PATH, "r", encoding="utf-8") as file:
        service_mappings = json.load(file)

    if not (port := service_mappings.get(service)):
        raise ValueError(f"Unknown local URL for service {service}")

    return LOCAL_BASE_URL.format(port=port) + endpoint
