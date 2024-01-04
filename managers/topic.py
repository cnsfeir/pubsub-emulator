from google.cloud.pubsub import PublisherClient

from constants import PROJECT_ID


class TopicManager:
    """
    Manages Pub/Sub topics.
    """

    @staticmethod
    def create(id_topic: str) -> None:
        """Creates a new Pub/Sub topic."""
        with PublisherClient() as publisher:
            topic_path = publisher.topic_path(PROJECT_ID, id_topic)
            publisher.create_topic(request={"name": topic_path})

    @staticmethod
    def fetch() -> list[str]:
        """Fetches all Pub/Sub topics"""
        with PublisherClient() as publisher:
            return publisher.list_topics(request={"project": f"projects/{PROJECT_ID}"})

    @staticmethod
    def delete(id_topic: str) -> None:
        """Deletes a Pub/Sub topic"""
        with PublisherClient() as publisher:
            topic_path = publisher.topic_path(PROJECT_ID, id_topic)
            publisher.delete_topic(request={"topic": topic_path})
