import os
from socket import socket, AF_INET, SOCK_STREAM


def check_connection() -> None:
    """
    Checks that the Pub/Sub emulator is running and the required environment variables are set.
    """
    if not (url := os.getenv("PUBSUB_EMULATOR_HOST")):
        raise EnvironmentError("Emulator environment variables are not set.")

    *_, port = url.split(":")
    with socket(AF_INET, SOCK_STREAM) as connection:
        if not connection.connect_ex(("localhost", int(port))):
            return

    raise ConnectionError("Pub/Sub emulator is not running.")
