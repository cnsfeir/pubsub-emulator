import json
import re

from pubsub_emulator.constants import LOCAL_BASE_URL, SERVICE_MAPPINGS_PATH, SERVICE_NAME_PATTERN


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
