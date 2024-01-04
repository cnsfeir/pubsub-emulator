import json

from typer import Option, Typer

from managers import SubscriptionManager, TopicManager

app = Typer()


@app.command()
def create_topic(id_topic: str) -> None:
    """Creates a new Pub/Sub topic."""
    TopicManager.create(id_topic)


@app.command()
def fetch_topics() -> None:
    """Fetches all Pub/Sub topics."""
    for topic in TopicManager.fetch():
        print(topic)


@app.command()
def delete_topic(id_topic: str) -> None:
    """Deletes a Pub/Sub topic."""
    TopicManager.delete(id_topic)


@app.command()
def create_subscription(request: str) -> None:
    """Creates a new Pub/Sub subscription."""
    SubscriptionManager.create(json.loads(request))


@app.command()
def update_subscription(id_subscription: str, update: str) -> None:
    """Updates a new Pub/Sub subscription."""
    SubscriptionManager.update(id_subscription, json.loads(update))


@app.command()
def fetch_subscriptions(id_subscription: str = Option(None), id_topic: str = Option(None)) -> None:
    """Fetches all Pub/Sub subscriptions in a topic or project."""
    for subscription in SubscriptionManager.fetch(id_subscription, id_topic):
        print(subscription)


@app.command()
def delete_subscription(id_subscription: str) -> None:
    """Deletes a Pub/Sub subscription."""
    SubscriptionManager.delete(id_subscription)


if __name__ == "__main__":
    app()
