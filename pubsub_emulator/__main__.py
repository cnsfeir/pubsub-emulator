import json
import sys

from typer import Argument, Context, Option, Typer

from pubsub_emulator.constants import HELP_FLAG
from pubsub_emulator.middlewares import check_connection
from pubsub_emulator.repositories import SubscriptionRepository, TopicRepository
from pubsub_emulator.utils import Printer, to_snakecase, translate_url

app = Typer()


@app.callback()
def main(context: Context) -> None:
    """
    Checks the connection to the Pub/Sub emulator.
    """
    try:
        if HELP_FLAG not in sys.argv:
            check_connection()
    except OSError as error:
        Printer.print_error(error)
        context.exit()


@app.command()
def load(
    configuration: str = Argument(help="The path to the configuration file to load"),
    translate: bool = Option(False, hidden=True),
) -> None:
    """
    Imports a Pub/Sub configuration from a JSON file into the emulator.
    """
    with open(configuration, "r", encoding="utf-8") as file:
        data = json.load(file)

    for topic in data["topics"]:
        TopicRepository.create(request=to_snakecase(topic))

    for subscription in data["subscriptions"]:
        if translate and (push_configuration := subscription.get("pushConfig")):
            push_configuration["pushEndpoint"] = translate_url(push_configuration["pushEndpoint"])
        SubscriptionRepository.create(request=to_snakecase(subscription))


@app.command()
def create_topic(id_topic: str = Argument(help="The ID of the new topic")) -> None:
    """Creates a new topic."""
    TopicRepository.create(id_topic)


@app.command()
def fetch_topics() -> None:
    """Fetches all topics."""
    for topic in TopicRepository.fetch():
        Printer.print_topic(topic)


@app.command()
def delete_topic(id_topic: str = Argument(help="The ID of the topic to delete")) -> None:
    """Deletes a topic."""
    TopicRepository.delete(id_topic)


@app.command()
def delete_all_topics() -> None:
    """Deletes all topics."""
    TopicRepository.delete_all()


@app.command()
def create_subscription(
    request: str = Argument(help="""The JSON request for the new subscription."""),
) -> None:
    """Creates a new subscription."""
    SubscriptionRepository.create(json.loads(request))


@app.command()
def update_subscription(
    id_subscription: str = Argument(help="The ID of the subscription to be updated"),
    update: str = Argument(help="The JSON request for the updates to the subscription"),
) -> None:
    """Updates a new subscription."""
    SubscriptionRepository.update(id_subscription, json.loads(update))


@app.command()
def fetch_subscriptions(
    id_subscription: str = Option(None, help="The ID of the subscription to fetch"),
    id_topic: str = Option(None, help="The ID of the topic to fetch"),
) -> None:
    """Fetches all subscriptions in a topic or project."""
    for subscription in SubscriptionRepository.fetch(id_subscription, id_topic):
        Printer.print_subscription(subscription)


@app.command()
def delete_subscription(id_subscription: str = Argument(help="The ID of the subscription to delete")) -> None:
    """Deletes a subscription."""
    SubscriptionRepository.delete(id_subscription)


@app.command()
def delete_all_subscriptions() -> None:
    """Deletes all subscriptions."""
    SubscriptionRepository.delete_all()


if __name__ == "__main__":
    app()
