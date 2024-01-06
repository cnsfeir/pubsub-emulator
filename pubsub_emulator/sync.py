import json

from google.cloud.pubsub import PublisherClient, SubscriberClient

from pubsub_emulator.utils import to_snakecase, translate_url


def import_topics() -> None:
    """
    Imports topics from a JSON file to the local Pub/Sub emulator.
    """
    with open("topics.json", "r", encoding="utf-8") as file:
        topics = json.load(file)

    with PublisherClient() as publisher:
        for topic in topics:
            publisher.create_topic(request=to_snakecase(topic))


def import_subscriptions() -> None:
    """
    Imports subscriptions from a JSON file to the local Pub/Sub emulator.
    """
    with open("subscriptions.json", "r", encoding="utf-8") as file:
        subscriptions = json.load(file)

    with SubscriberClient() as subscriber:
        for subscription in subscriptions:
            if configuration := subscription.get("pushConfig"):
                configuration["pushEndpoint"] = translate_url(configuration["pushEndpoint"])
            subscriber.create_subscription(request=to_snakecase(subscription))


if __name__ == "__main__":
    import_topics()
    import_subscriptions()
