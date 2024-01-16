import json

from typer import Argument, Context, Option, Typer

from pubsub_emulator.managers import SubscriptionManager, TopicManager
from pubsub_emulator.middlewares import check_connection
from pubsub_emulator.utils import Printer, to_snakecase, translate_url

app = Typer()


@app.callback()
def main(context: Context) -> None:
    """
    Checks the connection to the Pub/Sub emulator.
    """
    try:
        check_connection()
    except OSError as error:
        Printer.print_error(error)
        context.exit()


@app.command(hidden=True)
def sync() -> None:
    """
    Syncs the local Pub/Sub emulator with the cloud Pub/Sub configuration.
    """
    with open("topics.json", "r", encoding="utf-8") as file:
        topics = json.load(file)

    for topic in topics:
        TopicManager.create(request=to_snakecase(topic))

    with open("subscriptions.json", "r", encoding="utf-8") as file:
        subscriptions = json.load(file)

    for subscription in subscriptions:
        if configuration := subscription.get("pushConfig"):
            configuration["pushEndpoint"] = translate_url(configuration["pushEndpoint"])
        SubscriptionManager.create(request=to_snakecase(subscription))


@app.command()
def create_topic(id_topic: str = Argument(help="The ID of the new topic")) -> None:
    """Creates a new topic."""
    TopicManager.create(id_topic)


@app.command()
def fetch_topics() -> None:
    """Fetches all topics."""
    for topic in TopicManager.fetch():
        Printer.print_topic(topic)


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
        Printer.print_subscription(subscription)


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
