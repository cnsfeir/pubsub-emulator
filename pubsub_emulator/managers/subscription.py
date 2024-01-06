from google.cloud.pubsub import PublisherClient, SubscriberClient
from google.cloud.pubsub_v1.types import FieldMask, Subscription

from pubsub_emulator.constants import PROJECT_ID
from pubsub_emulator.utils import to_snakecase, update_dictionary

MAX_ATTEMPTS = 5


class SubscriptionManager:
    """
    Manages Pub/Sub subscriptions.
    """

    @staticmethod
    def create(request: dict) -> None:
        """Creates a new Pub/Sub subscription."""
        with SubscriberClient() as subscriber:
            subscriber.create_subscription(request=to_snakecase(request))

    @classmethod
    def update(cls, id_subscription: str, update: dict) -> None:
        """Updates an existing Pub/Sub subscription."""
        update = to_snakecase(update)
        paths = set(update.keys())

        with SubscriberClient() as subscriber:
            path = subscriber.subscription_path(PROJECT_ID, id_subscription)
            subscription = subscriber.get_subscription(subscription=path)

            mapping = update_dictionary(original=Subscription.to_dict(subscription), new=update)
            subscriber.update_subscription(
                subscription=Subscription(mapping),
                update_mask=FieldMask(paths=paths),
            )

    @staticmethod
    def delete(id_subscription: str) -> None:
        """Deletes a Pub/Sub subscription."""
        with SubscriberClient() as subscriber:
            subscription_path = subscriber.subscription_path(PROJECT_ID, id_subscription)
            subscriber.delete_subscription(request={"subscription": subscription_path})

    @staticmethod
    def delete_all() -> None:
        """Deletes all Pub/Sub subscriptions."""
        with SubscriberClient() as subscriber:
            for subsciption in subscriber.list_subscriptions(request={"project": f"projects/{PROJECT_ID}"}):
                subscriber.delete_subscription(request={"subscription": subsciption.name})

    @classmethod
    def fetch(cls, id_subscription: str | None = None, id_topic: str | None = None) -> list[Subscription]:
        """Fetches all Pub/Sub subscriptions in a topic or project."""
        if id_subscription:
            return [cls._fetch_one(id_subscription)]
        if id_topic:
            return cls._fetch_in_topic(id_topic)
        return cls._fetch_in_project()

    @staticmethod
    def _fetch_one(id_subscription: str) -> Subscription:
        """Fetches a single Pub/Sub subscription."""
        with SubscriberClient() as subscriber:
            subscription_path = subscriber.subscription_path(PROJECT_ID, id_subscription)
            return subscriber.get_subscription(subscription=subscription_path)

    @staticmethod
    def _fetch_in_topic(id_topic: str) -> list[Subscription]:
        """Fetches all Pub/Sub subscriptions in a topic."""
        with PublisherClient() as publisher:
            topic_path = publisher.topic_path(PROJECT_ID, id_topic)
            return publisher.list_topic_subscriptions(request={"topic": topic_path})

    @staticmethod
    def _fetch_in_project() -> list[Subscription]:
        """Fetches all Pub/Sub subscriptions in a project."""
        with SubscriberClient() as subscriber:
            return subscriber.list_subscriptions(request={"project": f"projects/{PROJECT_ID}"})
