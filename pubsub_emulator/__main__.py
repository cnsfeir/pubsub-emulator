import json

from typer import Option, Typer, Argument
from pubsub_emulator.managers import SubscriptionManager, TopicManager

app = Typer()


@app.command()
def create_topic(id_topic: str = Argument(help="The ID of the new topic")) -> None:
    """Creates a new topic."""
    TopicManager.create(id_topic)


@app.command()
def fetch_topics() -> None:
    """Fetches all topics."""
    for topic in TopicManager.fetch():
        print(topic)


@app.command()
def delete_topic(id_topic: str = Argument(help="The ID of the topic to delete")) -> None:
    """Deletes a topic."""
    TopicManager.delete(id_topic)


@app.command()
def delete_all_topics() -> None:
    """Deletes all topics."""
    TopicManager.delete_all()


@app.command()
def create_subscription(
    request: str = Argument(help="""The JSON request for the new subscription."""),
) -> None:
    """Creates a new subscription."""
    SubscriptionManager.create(json.loads(request))


@app.command()
def update_subscription(
    id_subscription: str = Argument(help="The ID of the subscription to be updated"),
    update: str = Argument(help="The JSON request for the updates to the subscription"),
) -> None:
    """Updates a new subscription."""
    SubscriptionManager.update(id_subscription, json.loads(update))


@app.command()
def fetch_subscriptions(
    id_subscription: str = Option(None, help="The ID of the subscription to fetch"),
    id_topic: str = Option(None, help="The ID of the topic to fetch"),
) -> None:
    """Fetches all subscriptions in a topic or project."""
    for subscription in SubscriptionManager.fetch(id_subscription, id_topic):
        print(subscription)


@app.command()
def delete_subscription(id_subscription: str = Argument(help="The ID of the subscription to delete")) -> None:
    """Deletes a subscription."""
    SubscriptionManager.delete(id_subscription)


@app.command()
def delete_all_subscriptions() -> None:
    """Deletes all subscriptions."""
    SubscriptionManager.delete_all()


if __name__ == "__main__":
    app()
